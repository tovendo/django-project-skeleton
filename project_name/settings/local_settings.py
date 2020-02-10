# for now fetch the development settings only
from .development import *


# ##### DEBUG CONFIGURATION ###############################

DEBUG = True

INTERNAL_IPS = []

# You will have to determine, which hostnames should be served by Django
ALLOWED_HOSTS = ['*']


# ##### DATABASE CONFIGURATION ############################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases
# DATABASES['default'].update({
#     # 'NAME': '',
#     # 'USER': '',
#     # 'PASSWORD': '',
#     # 'HOST': ''
# })


# ##### EMAIL CONFIGURATION ###############################

# This backend is not intended for use in production
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
