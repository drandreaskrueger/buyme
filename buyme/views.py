'''
@title    buyme ... views.py
@version: v04
  
@module   views: generate webpages, link to coinbase
  
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

from config import API_KEY, API_SECRET, API_URL, WWW_URL, COINBASE_CORRECT_IP # config for coinbase
from config import PRODUCTS, CURRENCY, SERVER, APPNAME, HOOKS, HOOK2, METAKEYS # config for my app
from config import PAGEHEADER, OTHER_VERSION_HTML # HTML snippets for mainnet <-> testnet
from config import DEBUG_MESSAGES

from models import newBuyForm, hookInbox

from reaction import react_sendMeEmail

from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from coinbase.wallet.client import Client

from pprint import pprint, pformat
import iptools  # pip install iptools



def htmlBodyTags(body):
  return ("<html><body>%s</body></html>" % body)

def home(request):
  return HttpResponse(htmlBodyTags( "Hello World!" ))

def checkIPcorrect(IP, IPpattern=COINBASE_CORRECT_IP, dbg=DEBUG_MESSAGES):
  if (IP in iptools.IpRangeList(IPpattern)):
    if dbg: print "'%s' is a coinbase IP, all cool." % IP
    return True
  else:
    if dbg: print "'%s' is NOT a coinbase IP!" % IP
    return False

def hook_storeCallbackDataIntoDatabase(request, hookname, trust):
  """Stores the whole answer into database
     Useful during the learning process.
  """
  hooked=hookInbox()
  hooked.hookname=hookname # to distinguish where from it got sent.
  hooked.TRUST=trust # came from Coinbase IP address
  hooked.meta=dict( [(meta, request.META[meta]) for meta in METAKEYS] )
  
  # N.B.: much unnecessary data, perhaps not needed to keep all?
  hooked.body=request.body 
  
  hooked.save()

def hook_reactToTrustedCallbackData(request, hookname, dbg):
  """Here is where the magic happens!
  
     Receiving the correct data on the hook can mean, 
     that the customer has paid, and wants to be served.
     
     So:
     Email me, 
     update the database with 'xyz has paid', 
     suggest skype call dates already, 
     etc.  
  """
  
  r=react_sendMeEmail(request, hookname, dbg)
  if dbg: print "sending email successful: %s" % r
  
  # TODO: Many other reactions are possible.
  pass


@csrf_exempt  
# disables the CSRF cookie (Cross Site Request Forgery protection)

def hook_URL(request, hookname, dbg=DEBUG_MESSAGES):
  "URL: receiving webhook, to digest Coinbase answers."
  
  if dbg: print "Received request on 'hook/name' : ", hookname, type(hookname)
  
  if (hookname not in HOOKS) or (request.method != 'POST'):
    answer="How dare you fiddle around here. Go away."
    return HttpResponseBadRequest(htmlBodyTags(answer)) 

  trust=checkIPcorrect(request.META['REMOTE_ADDR']) # of it came from Coinbase
  hook_storeCallbackDataIntoDatabase(request, hookname, trust) # later switch off?

  if True: # placeholder for threading
    #...............................................................
    # TODO: This block could be done in its own thread,
    # to be able to quickly answer back to Coinbase: (200, OK)
    if trust: hook_reactToTrustedCallbackData(request, hookname, dbg)
    #...............................................................
  
  answer="I got your message. Thanks."
  return HttpResponse(htmlBodyTags( answer )) # (200, OK)



def createCoinbaseCheckout(amount=59, metadata={"id": 42, "product" : "8 hours"}, 
                           hook=None, amount_presets=None, dbg=DEBUG_MESSAGES):
  """Access the Coinbase API, 
     to create a 'checkout', 
     and be given an 'embed_code'
  """
  
  client = Client(API_KEY, API_SECRET, base_api_uri=API_URL)
  
  # ONLY called if the customer presses the "Back to ..." button after payment
  success_url="%s/%s/thankyou/" % (SERVER, APPNAME) # after successful payment
  cancel_url= "%s/%s/cancel/"   % (SERVER, APPNAME)   # after timeout (15 minutes)
  
  parameters={ "amount": "%.2f" % amount,
               "currency": CURRENCY,
               "name": "Time with a BitCoin Expert",
               "description": "Buy time, and I skype with you.",
               "type": "order",
               "style": "buy_now_large",
               "customer_defined_amount": "false",
               "amount_presets": amount_presets,
               "collect_email": "false",
               "metadata": metadata,
               "success_url" : success_url,
               "cancel_url" : cancel_url,
               }
  
  if amount_presets!=None:
    parameters["amount_presets"]=amount_presets

  if hook!=None:
    notifications_url = "%s/%s/hook/%s/" % (SERVER, APPNAME, hook)
    if dbg: print "Callback: Using notifications_url='%s' for callback." % notifications_url
    parameters["notifications_url"]=notifications_url
  else:
    if dbg: print "Callback: using default from API-key definition."  
    
  checkout = client.create_checkout(**parameters)
  return checkout


def renderBuyForm(request, form):
  """take template, fill in data, and send to user browser.
  """
  return render(request, 'buy.html', {'form': form,
                                      'base_url': SERVER+"/"+APPNAME,
                                      'pageheader': PAGEHEADER,
                                      'linkToOtherVersion': OTHER_VERSION_HTML})

def buy_URL(request, dbg=DEBUG_MESSAGES):
  """URL: webpage with form.
     First access (GET): Send form to user browser.
     Second access (POST, but invalid): Send form with red missing fields.
     Third access (POST, valid): Create Coinbase checkout, redirect there.
  """
  
  if request.method=='GET':
    if dbg: print "showing webpage with form to input credentials"
    form = newBuyForm() 
    return renderBuyForm(request, form)
  
  elif request.method=='POST':
    if dbg: print "POST request received."
    form = newBuyForm(request.POST)

    if not form.is_valid(): # then report the missing fields:
      if dbg: print "Form validation failed." 
      return renderBuyForm(request, form)
    
    else: # form entries are valid, hooray :-)
      
      if dbg: print "Valid. Taking form entries, and creating a coinbase checkout."
      duration  = form.cleaned_data['duration']
      price = [ p["price"] for p in PRODUCTS if p["name"]==duration ] [0]
      
      newbuy=form.save()  # save to get a primary key which is later used to identify payment.
      metadata={"id": newbuy.id, "duration": duration}
      
      presets=[p["price"] for p in PRODUCTS]
      checkout=createCoinbaseCheckout(amount=price, metadata=metadata, amount_presets=presets) #, hook=HOOK2)
      # checkout=createCoinbaseCheckout(amount=price, metadata=metadata) # if you do not want to give all choices again.
      # print checkout
      
      # TODO: How to check if creating the checkout succeeded? Probably this will throw an exception:
      embed_code=checkout["embed_code"]
      
      payment_url='%s/checkouts/%s' % (WWW_URL, embed_code)
      if dbg: print "redirecting to coinbase: %s" % payment_url 
      
      return redirect(payment_url)


def printRequestGETasPRE(request):
  "Takes the request.GET query, transforms to dict, and pretty-prints it."
  answer="<pre>"
  # as dict (N.B.: if duplicates then take only one!):
  G=request.GET.dict()
  # pprint(G)  
  answer+=pformat(G, indent=3)
  answer+="</pre>"
  return answer
  

def thankYou_URL(request):
  """URL: thankyou
  """
  answer="This page gets called when the blue 'Return to ...' button is pressed after payment."

  # TODO: Do some fancy reaction 'Hooray you have paid'.
  answer+="<h1>Thank you for your purchase:</h1>"
  answer+=printRequestGETasPRE(request)
  return HttpResponse(htmlBodyTags( answer ))

def cancel_URL(request):
  """URL: cancel
  """
  answer="This page gets called when the blue 'Return to ...' button is pressed there was no payment for 15 minutes."

  # TODO: Do some fancy reaction 'You waited too long'.
  answer+="<h1>Checkout was cancelled:</h1>"
  answer+=printRequestGETasPRE(request)  
  return HttpResponse(htmlBodyTags( answer ))


if __name__ == "__main__":
    print "N.B.: This is not run directly, but whole project as 'django runserver'."
  
  