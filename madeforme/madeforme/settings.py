"""
Django settings for madeforme project.

"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
PROJECT_PATH = os.path.dirname(BASE_DIR)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY KEYS
import json
from django.core.exceptions import ImproperlyConfigured

with open(os.path.join(PROJECT_PATH,"keys.json")) as f:
    keys = json.loads(f.read())

def get_keys(setting, keys=keys):
    try:
        return keys[setting]
    except KeyError:
        error_msg = "Set the {0} environment variable".format(setting)
        raise ImproperlyConfigured

SECRET_KEY = get_keys("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'authtools',
    'betterforms',
    'crispy_forms',
    'customer',
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

ROOT_URLCONF = 'madeforme.urls'

WSGI_APPLICATION = 'madeforme.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)

STATIC_URL = '/static/'
MEDIA_URL = '/media/'


# Path structure for template and static files

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'templates', 'homepage'),
    os.path.join(BASE_DIR, 'templates', 'registration'),
)

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    os.path.join(BASE_DIR, "static", "css"),
    os.path.join(BASE_DIR, "static", "js"),
    os.path.join(BASE_DIR, "static", "images"),
    os.path.join(BASE_DIR, "static", "fonts"),
)


# User model for madeforme set to django-authtools email based authentication
SITE_ID = 1
AUTH_USER_MODEL = 'authtools.User'
LOGIN_REDIRECT_URL = '/customer/redirect'

# Template packs used by django_crispy_forms
CRISPY_TEMPLATE_PACK = 'bootstrap3'

# Email backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
