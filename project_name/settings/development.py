# Python imports
from decouple import config, Csv
from dj_database_url import parse as db_url

# project imports
from .common import *

# uncomment the following line to include i18n
from .i18n import *


# ##### DEBUG CONFIGURATION ###############################

DEBUG = config('DJANGO_DEBUG', default=True, cast=bool)
HOMOLOG = config('DJANGO_HOMOLOG', default=True, cast=bool)

# allow all hosts during development
ALLOWED_HOSTS = config('DJANGO_ALLOWED_HOSTS', default='127.0.0.1', cast=Csv())


# ##### DATABASE CONFIGURATION ############################

CONN_HEALTH_CHECKS = True

# https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#databases

DATABASES = {
    'default': db_url(
        config(
            'DJANGO_DATABASE_URL',
            default='sqlite:///' + PROJECT_ROOT.joinpath('run', 'db.sqlite3')),
        conn_max_age=30,
        conn_health_checks=True)
}

AMQP_URL = config('DJANGO_AMQP_URL', '')


# ##### APPLICATION CONFIGURATION #########################

INSTALLED_APPS = DEFAULT_APPS


# e-mail
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = config('DJANGO_EMAIL_HOST', default='127.0.0.1')
EMAIL_PORT = config('DJANGO_EMAIL_PORT', default=1025, cast=int)
EMAIL_HOST_USER = config('DJANGO_EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = config('DJANGO_EMAIL_HOST_PASSWORD', default='')
EMAIL_USE_TLS = config('DJANGO_EMAIL_USE_TLS', default=False, cast=bool)
DEFAULT_FROM_EMAIL = config('DJANGO_DEFAULT_FROM_EMAIL', default='')
EMAIL_SUBJECT_PREFIX = '[{{ project_name }}] '

ADMINS = config(
    'DJANGO_ADMIN_EMAIL', cast=Csv(cast=lambda v: tuple(v.split('|'))))


# ##### DJANGO RUNNING CONFIGURATION ######################

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': config(
            'DJANGO_CACHES_LOCATION', default='/var/tmp/django_cach'),
        'TIMEOUT': 60,
        'OPTIONS': {
            'MAX_ENTRIES': 1000
        }
    }
}

CORS_ALLOWED_ORIGIN_REGEXES = []

if HOMOLOG:
    CORS_ALLOWED_ORIGIN_REGEXES.extend([
        # Homologação
        r'^https?://127\.0\.0\.1(:[3|4|5|8|9][0-9]{3})?$',
        r'^https?://localhost(:[3|4|5|8|9][0-9]{3})?$',
        r'^https?://172\.17\.0\.1(:[3|4|5|8|9][0-9]{3})?$',
        r'^https?://(\w+\.)+local(:[3|4|5|8|9][0-9]{3})?$',
    ])
else:
    CORS_ALLOWED_ORIGIN_REGEXES.extend([
        # Produção
        r'^https?://(\w+\.)+exemplo\.com$',
    ])

CORS_ALLOW_ALL_ORIGINS = False


# ##### CRON CONFIGURATION ################################
CRONJOBS = config(
    'DJANGO_CRONS', cast=Csv(cast=lambda v: tuple(v.split(';')), delimiter='|'))
