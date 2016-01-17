'''
@title    buyme ... reaction.py
@version: v04
  
@module   React when user has paid, send email, etc.
  
@summary  Coinbase Payments made easy
          Django app to buy time, with BTC payments 
          - how to: 
              Coinbase checkouts, 
              webhooks, 
              thankYou & cancel pages, 
              etc.
  
@license:   (C) 2016 Andreas Krueger
@attention: If you like this, show it: [BTC] 1NvfRSDzXmwUdTjeqN8MAfmPCNHgwB8eiC  
@since      Created on 15 Jan 2016
@author:    Andreas Krueger  - github.com/drandreaskrueger/buyme
'''

if __name__ == "__main__": 
  from tools import settings_hack
  settings_hack()

from config import EMAIL_ALERT_ME, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_SENDER
from config import DEBUG_MESSAGES, PRODUCTION
from tools import amountCurrency
from buyme.models import paid, newBuy

from django.core.mail import send_mail

import os, json
from pprint import pformat


def react_saveAsPaid(notif):
  "extracts most useful payment data from notification, and stores into DB"
  p = paid()
  p.amount = amountCurrency (notif['data']['resource']['amount'])
  p.amount_BTC = amountCurrency (notif['data']['resource']['bitcoin_amount'])
  p.status = notif['data']['resource']['status']
  
  
  # p.newBuy_id = notif['data']['resource']['metadata']['id']
  newBuy_id = notif['data']['resource']['metadata']['id']
  p.newBuy_related = newBuy.objects.get(pk=newBuy_id)
  
  p.metadata =  notif['data']['resource']['metadata']
  # if more info needed, recover it by requesting this transaction:
  p.tx = notif['data']['resource']['transaction']['id']
  
  # redundant, but lazy style, easier for admin pages:
  # p.email = newBuy.objects.filter(id=p.newBuy_id) 
  p.save()
  
  return p


def sendMail(recipient, subject, body):
  """
  The django routine 'send_mail' is partly configured in djangoproject.settings !
  """
  try:
    result = send_mail (subject, body, 
                        from_email = EMAIL_SENDER, 
                        recipient_list = [recipient],
                        auth_password=EMAIL_HOST_PASSWORD, auth_user = EMAIL_HOST_USER, 
                        fail_silently=False)
    return result
  
  except Exception as e: 
    print "exception: ", type(e), e
    return False


def react_sendMeEmail(p, request, hookname, dbg=DEBUG_MESSAGES):
  """
  When a notification on a webhook is received, alert me by email.
  
  TODO: Extract useful information from the notification, 
        and include _only_that_ into the email body.
  """

  if EMAIL_ALERT_ME=="":
    if dbg: print "Email recipient not set. Not sending email."
    return False
  
  # most important data
  paid = pformat (p, indent=3)
  
  # whole notification
  body = json.loads(request.body)
  body = pformat(body, indent=3) # pretty print
  
  body = paid + "\n" + "-" * 40 + "\n" + body
  
  subject="Coinbase checkout notification received on webhook %s" % hookname
  if PRODUCTION:
    subject="[REAL] "+subject
  else:
    subject="[TESTNET] "+subject
  
  return sendMail(EMAIL_ALERT_ME, subject, body)
  


# testing:

def test_react_saveAsPaid():
  for filename in ("notification_correctPayment.txt", "notification_mispayment.txt"):
    with open(os.path.join("..","output",filename), "r") as f:
      text=f.read()
    notif = json.loads(text)
    p=react_saveAsPaid(notif)
    print p.id, type(p.id)


def test_sendMail():
  print sendMail(EMAIL_ALERT_ME, "test-subject", "test-body")

  
if __name__ == "__main__":
  settings_hack()
  # test_sendMail()
  test_react_saveAsPaid()
  
  