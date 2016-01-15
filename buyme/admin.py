'''
@title    buyme ... admin.py
@version: v04
  
@module   admin models for the django backend admin pages
  
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


from django.contrib import admin

from models import hookInbox, newBuy

class hookInboxAdmin(admin.ModelAdmin):
  list_display = ('TRUST', 'id', 'dateCreated', 'meta', 'body', 'hookname')

admin.site.register(hookInbox, hookInboxAdmin)


class newBuyAdmin(admin.ModelAdmin):
  list_display = (  'id', "email","skypename","message","dateCreated","duration")
  
admin.site.register(newBuy,newBuyAdmin)