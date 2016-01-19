


def LOGGING_level(LEVEL='DEBUG', dbg=True): 
  LOGGING = {
      'version': 1,
      'disable_existing_loggers': False,
      'handlers': {
          'console': {
              'class': 'logging.StreamHandler',
          },
      },
      'loggers': {
          'django': {
              'handlers': ['console'],
              'level': LEVEL,
          },
      },
  }
  if dbg: print "logging level: %s" % LOGGING['loggers']['django']['level'] 
  return LOGGING

