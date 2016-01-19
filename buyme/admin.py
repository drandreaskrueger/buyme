'''
@title    buyme ... admin.py
@version: v07
  
@summary   Admin models for the django backend admin pages. 
           To better understand the data structure, see _how-to/README.md
  
@license:   (C) 2016 Andreas Krueger
@attention: If you like this, show it: [BTC] 1JjSXcUKEmZGTvdC9BGbM6RrkGVdApape5  
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
    if obj.NewBuy==None: return "None"
    else: return obj.NewBuy.id
  
admin.site.register(paid,paidAdmin)

class paidInline(admin.TabularInline): # TabularInline # StackedInline
  model = paid
  fields= (  "status", "amount","amount_BTC", "tx", "dateCreated", "metadata")
  readonly_fields= fields

class newBuyAdmin(admin.ModelAdmin):
  inlines = [
        paidInline,
  ]

  list_display = (  'id', "paids", "email","skypename","message","dateCreated","duration")
  
  def paids(self, obj):
    return obj.paid_set.count() # counts the number of foreign_key objects point here
  
admin.site.register(newBuy,newBuyAdmin)
