'''
Created on 15 Jan 2016

@author: Andreas
'''

from django.http import HttpResponse
from pprint import pformat

def htmlBodyTags(body):
  return ("<html><body>%s</body></html>" % body)

def home(request):
  return HttpResponse(htmlBodyTags( "Hello World!" ))

def printDictAsHtmlPRE(G):
  "Takes the request.GET query, transforms to dict, and pretty-prints it."
  answer="<pre>"
  # pprint(G)  
  answer+=pformat(G, indent=3)
  answer+="</pre>"
  return answer