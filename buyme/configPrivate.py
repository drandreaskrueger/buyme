# Private credentials. Careful with this information. 
# Yes, the filename 'configPrivate.py' is in .gitignore
# but perhaps there are more secure ways. Tell me, thx.

PRODUCTION=False  

# Coinbase API credentials:

if not PRODUCTION:
  # Sandbox 
  API_KEY=""
  API_SECRET=""

else:
  # PRODUCTION
  API_KEY = ""
  API_SECRET =""

SANDBOX_URLS = ('https://api.sandbox.coinbase.com', 'https://sandbox.coinbase.com')
PRODUCTION_URLS=(      'https://api.coinbase.com' , 'https://coinbase.com')
API_BACKEND_URL, API_FRONTEND_URL=PRODUCTION_URLS if PRODUCTION else SANDBOX_URLS 

# optional:
# where to send the alert "customer paid!" to?
EMAIL_ALERT_ME=""   # if this is =="" then no email is sent.  

# I use gmail to send alerts: 
EMAIL_HOST_USER=""      # gmail username
EMAIL_HOST_PASSWORD=""  # gmail password
EMAIL_SENDER=EMAIL_HOST_USER


