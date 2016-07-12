"""
Django settings for reagents_db project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS as TCP
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'hem0_iqe0n22bnug_bj^rubjea=15!+w(@9#l&hqgjb!z9*(#p'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'suit',
    'reagents',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'reagents_db.urls'

WSGI_APPLICATION = 'reagents_db.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'reagents',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'




TEMPLATE_CONTEXT_PROCESSORS = TCP + (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)


AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,"templates"),
)
MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static', "img"),
    os.path.join(BASE_DIR,'static', "css"),
    os.path.join(BASE_DIR,'static', "js"),
)

SUIT_CONFIG= {
    'MENU_EXCLUDE': ('reagents.enzymetype','reagents.growthstrains','reagents.vectortype','reagents.antibioticresistance', 'reagents.lab', 'reagents.supplier',),
}

BASE_URL = 'http://cnp-intranet.champalimaud.pt:8383'
LOGIN_URL = "/accounts/login/"
LOGIN_REDIRECT_URL = '/'
SOCIALACCOUNT_ADAPTER = "cfauth.CFAccountAdapter.CFSocialAccountAdapter"
ACCOUNT_ADAPTER              = "cfauth.CFAccountAdapter.CFAccountAdapter"
ACCOUNT_EMAIL_REQUIRED       = True
SOCIALACCOUNT_AUTO_SIGNUP    = True
ACCOUNT_CONFIRM_EMAIL_ON_GET = False
SITE_ID = 1


PROFILE_GUEST = 'PROFILE: Guest'

try:
    exec (open("reagents_db/dev-settings.cfg").read())
except:
    pass

try:
    exec( open( "/etc/swpprjs/reagents.cfg" ).read() )
except: pass
