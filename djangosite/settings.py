"""
###########################################################
THIS FILE: AUTO-GENERATED BY DJANGO. My changes see bottom.
###########################################################

Django settings for djangosite project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ab%z5!cfg$x=!(-tttttt*=-8@$m=@t)@=erterr13^g^1*ee('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles'
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'djangosite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'djangosite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

######################################################################

# All the above was generated automatically by django-admin.
# Only this was added by me:

PRODUCTION=False

if PRODUCTION:
  ALLOWED_HOSTS = ['208.68.38.174'] # ["*"]
  DEBUG = False
  # to find the nasty coinbase bug, see 'HOST-header_empty.md'
  import loggingDebug 
  LOGGING=loggingDebug.LOGGING_level('DEBUG')

# sending email:
EMAIL_HOST="smtp.gmail.com"
EMAIL_USE_TLS, EMAIL_USE_SSL, EMAIL_PORT = True, False, 587

# location for static files (images, etc.)
STATIC_ROOT = os.path.join(BASE_DIR, "static", "djangosite")

# register the app:
INSTALLED_APPS=list(INSTALLED_APPS)
INSTALLED_APPS.append('buyme')
INSTALLED_APPS=tuple(INSTALLED_APPS)


########################################################

# the following is only for generating UML diagrams.

## for UML-diagrams via dia 
## https://github.com/neumond/django-dia
## pip install django-dia
# INSTALLED_APPS.append('django-dia')   

## for UML-diagrams via django-extensions 
## http://django-extensions.readthedocs.org/en/latest/graph_models.html
## pip install django-extensions
## pip install pyparsing==1.5.7
## pip install pydot
# INSTALLED_APPS.append('django_extensions')
## python manage.py graph_models -a -g -o buyme.png

## UML-diagrams via pygraphviz
## pip install wheel 
## pip install pylint pygraphviz
## pip remove pygraphviz
#### bug in pygraphviz installer, reported.
  
