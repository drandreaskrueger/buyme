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

from models import hookInbox, newBuy, paid

class hookInboxAdmin(admin.ModelAdmin):
  list_display = ('TRUST', 'id', 'dateCreated', 'meta', 'body', 'hookname')

admin.site.register(hookInbox, hookInboxAdmin)

class paidAdmin(admin.ModelAdmin):
  list_display = (  'id', "amount","amount_BTC","status", "newBuy_related", "metadata", "tx", "dateCreated")
  
  def newBuy_related(self, obj):
        return obj.NewBuy.id
  
admin.site.register(paid,paidAdmin)

class paidInline(admin.TabularInline): # TabularInline # StackedInline
  model = paid
  fields= (  "status", "amount","amount_BTC", "tx", "dateCreated", "metadata")

class newBuyAdmin(admin.ModelAdmin):
  inlines = [
        paidInline,
  ]

  list_display = (  'id', "paids", "email","skypename","message","dateCreated","duration")
  
  def paids(self, obj):
    return obj.paid_set.count() # counts the number of foreign_key objects point here
  
admin.site.register(newBuy,newBuyAdmin)
