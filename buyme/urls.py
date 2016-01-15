'''
@title    buyme ... urls.py
@version: v04

@module   URL dispatcher definitions

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

from django.conf.urls import include, url
from django.contrib import admin

from views import buy_URL, hook_URL, thankYou_URL, cancel_URL

urlpatterns = [
    # Examples:
    # url(r'^$', 'djangosite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^$', 'buyme.views.home', name='home'),
    url(r'^$', buy_URL, name='buy'),
    url(r'^hook/(\d+)/$', hook_URL, name='hook'),
    url(r'^thankyou/$', thankYou_URL, name='thankYou'),
    url(r'^cancel/$', cancel_URL, name='cancel'),
]








