'''
@title    buyme ... config.py
@version: v08
  
@summary  configuration, parameters, constants
          adapt this to your needs.
  
@license:   (C) 2016 Andreas Krueger
@attention: If you like this, show it: [BTC] 1NvfRSDzXmwUdTjeqN8MAfmPCNHgwB8eiC  
@since      Created on 13 Jan 2016
@author:    Andreas Krueger  - github.com/drandreaskrueger/buyme
'''

from configPrivate import API_KEY, API_SECRET, EMAIL_ALERT_ME, EMAIL_HOST_USER, EMAIL_HOST_PASSWORD, EMAIL_SENDER

VERSION="v08"

SERVER_IP="208.68.38.174"

PRODUCTNAME="Buy Time with a Specialist in Cryptocurrencies."
PRODUCTDESCRIPTION="Let us SKYPE: I can CODE for you, RESEARCH your topics, ANALYZE your DATA, etc."

CURRENCY="USD"
CHOICES=[
          {"name": "5 minutes", "price" : 9},
          {"name": "15 minutes", "price" : 19},
          {"name": "1 hour", "price" : 60},
          {"name": "4 hours", "price" : 200},
          {"name": "1 day", "price" : 349},
          ]
SHOW_ALL_PRICES_AGAIN = True # True to show all these prices again in coinbase checkout dialogue 

PRODUCTION=True
DEBUG_MESSAGES=True

# TODO: automatic process, with individualized obfuscated hook names. Until then, change manually:
HOOK1 = "0000000847283492041" # set when API key created https://sandbox.coinbase.com/settings/api
HOOK2 = "9999999876543765456" # set in individual checkout. Only this seems to work, the above not. 
HOOKS = (HOOK1, HOOK2) 

STYLE=("ul.errorlist {list-style-type: none; display:inline; margin-left: 0; padding-left: 0;}"
       "ul.errorlist li {display: inline; color:red; }"
       ".required { font-weight: bold; }"
       "form table tr td {vertical-align: top;}"
       "body {font-family:Verdana,Arial,sans-serif;margin-top:0;}")

######################################################
# you probably do not want to change much below this. 
######################################################

APPNAME="buyme"

SANDBOX_URLS = ('https://api.sandbox.coinbase.com', 'https://sandbox.coinbase.com')
PRODUCTION_URLS=(      'https://api.coinbase.com' , 'https://coinbase.com')
API_BACKEND_URL,API_FRONTEND_URL=PRODUCTION_URLS if PRODUCTION else SANDBOX_URLS 

COINBASE_CORRECT_IP="54.175.255.192/27"

# only want to store these from the hook callback answer 'request.META':
METAKEYS=['REMOTE_ADDR', 'REMOTE_HOST', 'PATH_INFO', 'SERVER_PROTOCOL', 
          'CONTENT_TYPE', 'CONTENT_LENGTH', ]

if PRODUCTION:
  SERVER_PORT=8001
  PAGEHEADER=""
  SERVER_OTHER_NAME, SERVER_OTHER="testnet3", "http://%s:8000" % SERVER_IP
  # SENTENCE=""
  SENTENCE="You can try out the '%s' version, if you do not want to spend real money."
  
else:
  SERVER_PORT=8000
  PAGEHEADER=('<div style="width:100%; height:29px; color:white; background-color:' 
              '#E07400; text-align:center; padding-top:11px;}">'
              'This is a sandboxed environment for' 
              ' testing and development purposes; all BTC values are testnet.</div>')
  SERVER_OTHER_NAME, SERVER_OTHER="mainnet", "http://%s:8001" % SERVER_IP
  SENTENCE="This uses testnet3 money. Go to the '%s' version, to spend real money, and buy real time from me."
  
OTHER_VERSION_HTML=""
if SENTENCE!="":
  OTHER_VERSION_HTML=SENTENCE % ('<a href="%s" target="_blank">%s</a>' % (SERVER_OTHER, SERVER_OTHER_NAME))
  OTHER_VERSION_HTML="<small>"+OTHER_VERSION_HTML+"</small>"

SERVER="http://%s:%s" % (SERVER_IP, SERVER_PORT) # TODO: https
