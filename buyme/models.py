'''
@title    buyme ... models.py
@version: v04
  
@module   Database models    
  
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

from django.db import models

from django import forms
from django.forms import ModelForm
from django.utils import timezone

## sudo pip install jsonfield
from jsonfield import JSONField

from config import PRODUCTS, CURRENCY, HOOKS, APPNAME

# the user choices for the product
max_length_choice=max([len(p["name"]) for p in PRODUCTS])
choices=[(p["name"], "%s (%s %s)" % (p["name"],p["price"],CURRENCY) ) for p in PRODUCTS]

EMAILLENGTH=254
SKYPENAMELENGTH=32
MESSAGELENGTH=1000

AMOUNT_LENGTH = 16    # "999999999.00 VND"
AMOUNT_BTC_LENGTH = 16 # "999.12345678 BTC"
STATUS_LENGTH =7 # # "expired", "paid"
TX_LENGTH = 36 # "616124b5-db6f-5038-99a5-196aec516ec8"

HOOKNAMELENGTH=max([len(h) for h in HOOKS])

class hookInbox(models.Model):
  "for storing received callback data arriving on hooks"
  dateCreated = models.DateTimeField('created', default = timezone.now)
  body = JSONField() 
  meta = JSONField() 
  hookname = models.CharField(max_length=HOOKNAMELENGTH)
  TRUST = models.BooleanField(default=True)
  class Meta:
    app_label = APPNAME



class newBuy(models.Model):
  "for form for buying"
  
  email     = models.EmailField(max_length=EMAILLENGTH, blank=False)
  skypename = models.CharField(max_length=SKYPENAMELENGTH, blank=True)
  message   = models.TextField (max_length=MESSAGELENGTH, blank=True)
  dateCreated = models.DateTimeField('created', default = timezone.now)
  duration  = models.CharField(max_length=max_length_choice, choices=choices)
  
  
class newBuyForm(ModelForm):
  "form for buying"
  error_css_class    = 'error'
  required_css_class = 'required'
  
  class Meta:
    model=newBuy
    fields=['duration','email', 'skypename', 'message']
    labels={'email':'Your email address', 
            'skypename':'(optional) Your skype name', 
            'duration': 'How much time:',
            'message':'(optional) Message to me'}
    help_texts={'email':'I will send suggestions when I can have time for you.',
                'skypename':'Get a skype name at login.skype.com/join (only *-fields have to be filled in).',
                'duration':'Try to estimate how much time you need. The longer the cheaper it gets.',
                'message':'Perhaps already give me an idea what you want to talk about.'}
    choices=[(p["name"],p["name"]) for p in PRODUCTS]
    widgets = {'email': forms.TextInput(attrs={'size': 30}),
               'skypename': forms.TextInput(attrs={'size': 30}),
               'message': forms.Textarea (attrs = {'cols':'31', 'rows':'3'} )}
    

class paid(models.Model):
  "for storing money data received via webhook"
  dateCreated = models.DateTimeField('created', default = timezone.now)
  
  # newBuy_id = models.IntegerField() 
  newBuy_related = models.ForeignKey(newBuy)
  
  metadata=JSONField()
  amount=models.CharField(max_length=AMOUNT_LENGTH)
  amount_BTC=models.CharField(max_length=AMOUNT_BTC_LENGTH)
  status=models.CharField(max_length=STATUS_LENGTH)
  tx=models.CharField(max_length=TX_LENGTH)
  
  # redundant, but lazy style, easier for admin pages:
  # email     = models.EmailField(max_length=EMAILLENGTH, blank=False)
  