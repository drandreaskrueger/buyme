'''
@title    buyme ... paymentGateway.py
@version: v07
  
@summary  coinbase checkout
  
@license:   (C) 2016 Andreas Krueger
@attention: If you like this, show it: [BTC] 1NvfRSDzXmwUdTjeqN8MAfmPCNHgwB8eiC  
@since      Created on 13 Jan 2016
@author:    Andreas Krueger  - github.com/drandreaskrueger/buyme
'''

from config import API_KEY, API_SECRET, API_BACKEND_URL # config for coinbase
from config import PRODUCTNAME, PRODUCTDESCRIPTION
from config import CURRENCY, SERVER, APPNAME # config for my app
from config import DEBUG_MESSAGES, PRODUCTNAME

from coinbase.wallet.client import Client



def createCoinbaseCheckout(amount=59, metadata={"id": 42, "product" : "8 hours"}, 
                           hook=None, amount_presets=None, dbg=DEBUG_MESSAGES):
  """Access the Coinbase API, 
     to create a 'checkout', 
     and be given an 'embed_code'
  """
  
  client = Client(API_KEY, API_SECRET, base_api_uri=API_BACKEND_URL)
  
  # ONLY called if the customer presses the "Back to ..." button after payment
  success_url="%s/%s/thankyou/" % (SERVER, APPNAME) # after successful payment
  cancel_url= "%s/%s/cancel/"   % (SERVER, APPNAME)   # after timeout (15 minutes)
  
  parameters={ "amount": "%.2f" % amount,
               "currency": CURRENCY,
               "name": PRODUCTNAME,
               "description": PRODUCTDESCRIPTION,
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
    if dbg: print "Callback: using default from API-key definition."  ## Coinbase Bug: Not working
    
  checkout = client.create_checkout(**parameters)
  return checkout

def verifyCallbackAuthenticity(request):
  """https://github.com/coinbase/coinbase-python#merchant-callbacks
  
  verify_callback() IS BROKEN!
  See 
  https://github.com/drandreaskrueger/coinbaseTestbed/blob/master/output/BUGS_verify_callback.md
  
  """

 
  try:  
    client = Client(API_KEY, API_SECRET, base_api_uri=API_BACKEND_URL)
    verify=client.verify_callback(request.body, request.META['X-Signature'])
  except Exception as e:
    print "verify_callback EXCEPTION: ", type(e), e
    return False
  
  return verify


if __name__ == "__main__":
    print "N.B.: This is not run directly, but whole project as 'django runserver'."
  
  