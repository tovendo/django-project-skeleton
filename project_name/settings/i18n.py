# Django imports
from django.utils.translation import gettext_lazy as _

# project imports
from .common import PROJECT_ROOT, MIDDLEWARE


# ##### INTERNATIONALIZATION ##############################

# https://docs.djangoproject.com/en/{{ docs_version }}/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Maceio'

# Internationalization
USE_I18N = True

# enable timezone awareness by default
USE_TZ = True

# This list of languages will be provided
LANGUAGES = (
    ('pt-br', _('Brazilian Portuguese')),
    ('en', _('English')),
)

# Look for translations in these locations
LOCALE_PATHS = (
    PROJECT_ROOT.joinpath('locale'),
)

# Inject the localization middleware into the right position
MIDDLEWARE = [y for i, x in enumerate(MIDDLEWARE) for y in (
    ('django.middleware.locale.LocaleMiddleware', x) if MIDDLEWARE[i - 1] == \
    'django.contrib.sessions.middleware.SessionMiddleware' else (x, ))]
