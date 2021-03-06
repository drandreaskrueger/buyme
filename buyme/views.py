'''
@title    buyme ... views.py
@version: v13
  
@summary  All the html pages for the app.

          (N.B.: The POST-webhook is in webhook.py)
  
          Coinbase Payments made easy
          Django app to buy time, with BTC payments 
          - learning how to: 
              create Coinbase checkouts, 
              receive data an webhooks, 
              thankYou & cancel pages, 
              etc.
  
@license:   (C) 2016 Andreas Krueger
@attention: If you like this, show it: [BTC] 1JjSXcUKEmZGTvdC9BGbM6RrkGVdApape5  
@since      Created on 13 Jan 2016
@author:    Andreas Krueger  - github.com/drandreaskrueger/buyme
'''

from config import API_FRONTEND_URL
from config import PRODUCTNAME, PRODUCTDESCRIPTION, CHOICES, CURRENCY, SHOW_ALL_PRICES_AGAIN 
from config import VERSION, SERVER, APPNAME  # config for my app # , HOOK2
from config import STYLE, PAGEHEADER, OTHER_VERSION_HTML # HTML snippets for mainnet <-> testnet
from config import DEBUG_MESSAGES

from models import newBuyForm, hookname # from buyme.models
from tools import htmlBodyTags, printDictAsHtmlPRE
from paymentGateway import createCoinbaseCheckout

from django.http import HttpResponse
from django.shortcuts import redirect
from django.shortcuts import render

def renderBuyForm(request, form):
  """take template, fill in data, and send to user browser.
  """
  return render(request, 'buy.html', {'form': form,
                                      'base_url': SERVER+"/"+APPNAME,
                                      'pageheader': PAGEHEADER,
                                      'productname': PRODUCTNAME,
                                      'productdescription': PRODUCTDESCRIPTION,
                                      'linkToOtherVersion': OTHER_VERSION_HTML,
                                      'version' : VERSION,
                                      'style': STYLE})

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
      
      newbuy=form.save()  
      
      if dbg: print "Valid. Saved. Taking form entries, and creating a coinbase checkout."
      duration  = form.cleaned_data['duration']
      price = [ p["price"] for p in CHOICES if p["name"]==duration ] [0] # take first!

      metadata={"id": newbuy.id, # primary key can later be used to identify (paid --> newbuy) 
                "duration": duration, "price": "%s %s" % (price, CURRENCY)} # most important data into payment
      
      presets=None if not SHOW_ALL_PRICES_AGAIN else [p["price"] for p in CHOICES]

      hook=hookname() # automatically creates new random .name
      hook.NewBuy=newbuy # set foreign key, then
      hook.save()
            
      try: 
        checkout=createCoinbaseCheckout(amount=price, metadata=metadata, amount_presets=presets,
                                        hook=hook.name)
      except Exception as e:
        answer="Problem. Please tell us: (%s) %s" % (str(type(e)), e)
        print answer
        return HttpResponse(htmlBodyTags( answer ))
      
      if dbg: print "client.create_checkout.warnings=%s" % checkout.warnings
      # print checkout
      embed_code=checkout["embed_code"]
      
      payment_url='%s/checkouts/%s' % (API_FRONTEND_URL, embed_code)
      if dbg: print "redirecting to coinbase: %s" % payment_url 
      
      return redirect(payment_url)


def addHeader():
  s='<style type="text/css">%s</style>' % STYLE
  s+=PAGEHEADER
  s+="<p>This page gets called when the blue 'Return to ...' button is pressed "
  return s

def thankYou_URL(request):
  """URL: thankyou
  """
  answer=addHeader()
  answer+= "after payment.</p>"

  # TODO: Do some fancy reaction 'Hooray you have paid'.
  answer+="<h1>Thank you for your purchase:</h1>"
  answer+=printDictAsHtmlPRE(request.GET.dict())
  return HttpResponse(htmlBodyTags( answer ))


def cancel_URL(request):
  """URL: cancel
  """
  
  answer=addHeader()
  answer+="after there was no payment for 15 minutes.</p>"

  # TODO: Do some fancy reaction 'You waited too long'.
  answer+="<h1>Checkout was cancelled:</h1>"
  answer+=printDictAsHtmlPRE(request.GET.dict())  
  return HttpResponse(htmlBodyTags( answer ))


# hook_URL --> see webhook.py


if __name__ == "__main__":
    print "N.B.: This is not run directly, but whole project as 'django runserver'."
  
  