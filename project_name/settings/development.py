# Python imports
from decouple import config
from dj_database_url import parse as db_url
from os.path import join

# project imports
from .common import *

# uncomment the following line to include i18n
from .i18n import *


# ##### DEBUG CONFIGURATION ###############################

DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)
HOMOLOG = config('DJANGO_HOMOLOG', default=True, cast=bool)

# allow all hosts during development
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')])


# ##### DATABASE CONFIGURATION ############################

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': config(
        'DJANGO_DATABASE_URL',
        default='sqlite:///' + join(PROJECT_ROOT, 'run', 'db.sqlite3'),
        cast=db_url
    )
}


# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS
