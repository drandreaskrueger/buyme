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

from configPrivate import EMAIL_ALERT_ME, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_SENDER
from config import DEBUG_MESSAGES

from django.core.mail import send_mail

import os, sys, json
from pprint import pformat

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
    print result
    return result
  
  except Exception as e: 
    print "exception: ", type(e), e
    return False


def react_sendMeEmail(request, hookname, dbg=DEBUG_MESSAGES):
  """
  When a notification on a webhook is received, alert me by email.
  
  TODO: Extract useful information from the notification, 
        and include only that into the email body.
  """

  if EMAIL_ALERT_ME=="":
    if dbg: print "Email recipient not set. Not sending email."
    return False
  
  body = json.loads(request.body)
  body=pformat(body, indent=3) # pretty print
  
  subject="Coinbase checkout notification received on webhook %s" % hookname
  
  return sendMail(EMAIL_ALERT_ME, subject, body)
  

# testing:

def settings_hack():
  """
  If this file is called directly (and not through runserver), then 
  the djangoproject.settings cannot be found. This hack fixes that.
  """
  root_path = os.path.dirname(__file__)
  root_path = os.path.dirname(root_path) # one up
  sys.path.insert(0, root_path)

def test_sendMail():
  settings_hack()
  print sendMail(EMAIL_ALERT_ME, "test-subject", "test-body")

  
if __name__ == "__main__":
  test_sendMail()
  
  