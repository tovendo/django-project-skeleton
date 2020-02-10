# Python imports
from os.path import join

# project imports
from .common import *

# uncomment the following line to include i18n
from .i18n import *


# ##### DEBUG CONFIGURATION ###############################

DEBUG = True

# allow all hosts during development
ALLOWED_HOSTS = ['*']


# ##### DATABASE CONFIGURATION ############################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': join(PROJECT_ROOT, 'run', 'dev.sqlite3'),
    }
}


# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS


try:
    from .local_settings import *
except ImportError:
    pass
