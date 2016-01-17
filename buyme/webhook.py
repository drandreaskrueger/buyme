'''
@title    buyme ... webhook.py
@version: v04
  
@module   hook for coinbase callbacks
  
@summary  Coinbase Payments made easy
          Django app to buy time, with BTC payments 
          - how to: 
              Coinbase checkouts, 
              webhooks, 
              thankYou & cancel pages, 
              etc.
  
@license:   (C) 2016 Andreas Krueger
@attention: If you like this, show it: [BTC] 1NvfRSDzXmwUdTjeqN8MAfmPCNHgwB8eiC  
@since      Created on 13 Jan 2016
@author:    Andreas Krueger  - github.com/drandreaskrueger/buyme
'''

from config import COINBASE_CORRECT_IP # config for coinbase
from config import HOOKS, METAKEYS # config for my app
from config import DEBUG_MESSAGES

from tools import htmlBodyTags
from models import hookInbox, paid

from reaction import react_saveAsPaid, react_sendMeEmail

from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

import json
import iptools  # pip install iptools


def hook_reactToTrustedCallbackData(request, hookname, dbg):
  """Here is where the magic happens!
  
     Receiving the correct data on the hook can mean, 
     that the customer has paid, and wants to be served.
     
     So:
     Email me, 
     update the database with 'xyz has paid',
     email him, 
     suggest skype call dates already, 
     etc.  
  """

  # N.B.: Correspondence of metadata.id with primary key of form submission object 
  # [paid].metadata.id == [newBuy].id
  p=react_saveAsPaid(json.loads(request.body)) 
  
  r=react_sendMeEmail(p, request, hookname, dbg) # so that I know that I got money :-)
  if dbg: print "sending email success = %s" % r
  
  # TODO: Many more reactions are possible.
  #
  # * send a confirmation to the customer
  # * already suggest several dates for a first skype interview
  # * etc. 
  
  pass


def checkIPcorrect(IP, IPpattern=COINBASE_CORRECT_IP, dbg=DEBUG_MESSAGES):
  "callbacks should come from Coinbase"
  if (IP in iptools.IpRangeList(IPpattern)):
    if dbg: print "'%s' is a coinbase IP, all cool." % IP
    return True
  else:
    if dbg: print "'%s' is NOT a coinbase IP!" % IP
    return False


def hook_storeCallbackDataIntoDatabase(request, hookname, trust):
  """Stores the whole answer into database. 
     Useful during the learning process, but creates much data.
  """
  hooked=hookInbox()
  hooked.hookname=hookname # to distinguish where from it got sent.
  hooked.TRUST=trust # came from Coinbase IP address
  hooked.meta=dict( [(meta, request.META[meta]) for meta in METAKEYS] )
  
  # N.B.: much unnecessary data, perhaps not needed to keep all?
  hooked.body=request.body 
  
  hooked.save()
  

@csrf_exempt  
# disables the CSRF cookie (Cross Site Request Forgery protection)

def hook_URL(request, hookname, dbg=DEBUG_MESSAGES):
  "URL: receiving webhook, to digest Coinbase answers."
  
  if dbg: print "Received request on 'hook/name' : ", hookname, type(hookname)
  
  if (hookname not in HOOKS) or (request.method != 'POST'):
    answer="How dare you fiddle around here. Go away."
    return HttpResponseBadRequest(htmlBodyTags(answer)) 

  # Did it from Coinbase?
  trust=checkIPcorrect(request.META['REMOTE_ADDR'])
   
  # Store all. Regardless. Later switch off? 
  hook_storeCallbackDataIntoDatabase(request, hookname, trust) 

  # If the notification is really coming from coinbase, do fancy stuff:
  if trust: 
    # TODO: Especially if more reactions are added, then this could be done in 
    # its own thread, to be able to quickly answer back to Coinbase: (200, OK)
    hook_reactToTrustedCallbackData(request, hookname, dbg)
  
  return HttpResponse(htmlBodyTags( "Thanks." )) # (200, OK)



if __name__ == "__main__":
    print "N.B.: This is not run directly, but whole project as 'django runserver'."
  
  
