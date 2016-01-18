'''
Created on 15 Jan 2016

@author: Andreas
'''

#from django.http import HttpResponse
from pprint import pformat

def htmlBodyTags(body):
  return ("<html><body>%s</body></html>" % body)

#def home(request):
#  return HttpResponse(htmlBodyTags( "Hello World!" ))

def amountCurrency(money):
  return "%s %s" % (money["amount"], money["currency"])

def printDictAsHtmlPRE(G):
  "Takes the request.GET query, transforms to dict, and pretty-prints it."
  answer="<pre>"
  # pprint(G)  
  answer+=pformat(G, indent=3)
  answer+="</pre>"
  return answer

def settings_hack():
  """
  If this file is called directly (and not through runserver), then 
  the djangoproject.settings cannot be found. This hack fixes that.
  """
  import os, sys
  root_path = os.path.dirname(__file__)
  root_path = os.path.dirname(root_path) # one up
  # print root_path
  sys.path.insert(0, root_path)
  sys.path.insert(0, os.path.join(root_path, "djangosite"))
  
  import django; django.setup()
  
  