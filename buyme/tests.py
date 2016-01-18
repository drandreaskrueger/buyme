from django.test import TestCase

# Unready.


# TODO!

from coinbase import createCoinbaseCheckout

def someTests():
  # print checkIPcorrect("54.175.255.207",COINBASE_CORRECT_IP)
  # print checkIPcorrect("192.168.0.14",COINBASE_CORRECT_IP)  
  
  checkout=createCoinbaseCheckout()
  print checkout