LEVEL='DEBUG'

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
import logging.config
logging.config.dictConfig(LOGGING)

print "logging level set to %s" % LEVEL