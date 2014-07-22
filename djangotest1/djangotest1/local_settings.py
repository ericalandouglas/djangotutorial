"""
Django settings for djangotest1 project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import dj_database_url
from settings2 import BASE_DIR
import os
#BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'x3tl-tp7nh)-9nf2y70kdk^63n(8_@v)oyn1)t_222)q5ptpmx'

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
    'article',
    'south',
    'django.contrib.formtools',
    'userprofile',
    'storages',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'djangotest1.urls'

WSGI_APPLICATION = 'djangotest1.wsgi.application'

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, 'templates'),
    os.path.join(BASE_DIR, 'article/templates'),
    os.path.join(BASE_DIR, 'userprofile/templates'),
)


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(
        default='sqlite:////%s/storage.db' % BASE_DIR
    )
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Los_Angeles'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Media files

MEDIA_ROOT = os.path.join(BASE_DIR, 'static/')


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

# root used to collect static content
STATIC_ROOT = BASE_DIR

STATIC_URL = '/assets/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static')),
)

AUTH_PROFILE_MODULE = 'userprofile.UserProfile'

# Email settings

EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'ericalandouglas@gmail.com'
EMAIL_HOST_PASSWORD = 'fallen262'
EMAIL_PORT = 587

UPLOAD_FILE_PATTERN = "uploaded_files/%s_%s"

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'
        }
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/mylog.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'logs/django_request.log',
            'maxBytes': 1024*1024*5, # 5 MB
            'backupCount': 5,
            'formatter': 'standard'
        }
    },
    'loggers': {
        '': {
            'handlers': ['default'],
            'level': 'DEBUG',
            'propogate': True
        }
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'DEBUG',
            'propagate': False
        }
    }
}