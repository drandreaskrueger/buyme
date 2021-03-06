'''
@title    buyme ... webhook.py
@version: v0.14
  
@summary  hook for coinbase callbacks

          now with: individual generated hooknames instead of hardcoded placeholders  
  
@license:   (C) 2016 Andreas Krueger
@attention: If you like this, show it: [BTC] 1JjSXcUKEmZGTvdC9BGbM6RrkGVdApape5  
@since      Created on 13 Jan 2016
@author:    Andreas Krueger  - github.com/drandreaskrueger/buyme
'''

from config import METAKEYS # config for my app  # HOOKS, 
from config import DEBUG_MESSAGES

from tools import htmlBodyTags
from models import hookname, hookInbox

import paymentGateway

import reactions #  <-- called when received data all ok!


from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt


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
  

def allHooknames():
  "get all hookname.name from database"
  hooks=[obj.name for obj in hookname.objects.all()]
  return hooks
  

def canHookDataBeTrusted(request, hookname, dbg=DEBUG_MESSAGES):
  "checks hookname, IP, signature"
  
  if (hookname not in allHooknames() ):
    if dbg: print "Data arriving on an unrecognized hook: %s." % hookname
    trustHook=False
  else:
    if dbg: print "Hookname recognized."
    trustHook=True 
  if dbg: print "trustHook=%s" % trustHook

  # Did it from Coinbase?
  trustIP=paymentGateway.checkIPcorrect(request.META['REMOTE_ADDR'])
  if dbg: print "trustIP=%s" % trustIP
  
  # Is the signature correct? TODO!
  # trustSig=paymentGateway.verifyCallbackAuthenticity(request)
  # if dbg: print "trustSig=%s" % trustSig
  trustSig = True # client.verify_callback() broken, see verifyCallbackAuthenticity 
  
  trust = trustIP and trustSig and trustHook
  
  return trust


@csrf_exempt  
# disables the CSRF cookie (Cross Site Request Forgery protection)

def hook_URL(request, hookname, dbg=DEBUG_MESSAGES, DROP_ALL_BUT_POST = False):
  "URL: receiving webhook, to digest Coinbase answers."
  
  if dbg: print "Received %s request on /hook/%s/" %(request.method, hookname)
  
  if DROP_ALL_BUT_POST and (request.method != 'POST'):
    answer="How dare you fiddle around here. Go away."
    return HttpResponseBadRequest(htmlBodyTags(answer))

  trust = canHookDataBeTrusted(request, hookname, dbg=DEBUG_MESSAGES)
   
  # Store all. Regardless. Later switch off? 
  hook_storeCallbackDataIntoDatabase(request, hookname, trust) 

  # If the notification is really coming from coinbase, do all the fancy stuff:
  if trust: 
    # TODO: Especially if more reactions are added, then this could be done in 
    # its own thread, to be able to quickly answer back to Coinbase: (200, OK)
    if dbg: print "Request is trusted. Calling reactions:" 
    reactions.ifTrustedCallbackData(request, hookname, dbg)
  
  return HttpResponse(htmlBodyTags( "Thanks." )) # (200, OK)



if __name__ == "__main__":
    print "N.B.: This is not run directly, but whole project as 'django runserver'."
    
  
