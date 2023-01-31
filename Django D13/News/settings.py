import logging
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-ru*iebk_nkn6%!u=h%p9hpmg)2r@mwo+ydf*cm_xtm(%@v_8h4'

DEBUG = True

ALLOWED_HOSTS = []

LOGIN_REDIRECT_URL = "/news"

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'

SITE_ID = 1


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
]

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'True': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
        'False': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'formatters': {
        'for_debug': {
            'format': '{asctime} - {levelname} - {module} - {message}',
            'style': '{',
        },
        'for_warning': {
            'format': '{asctime} - {levelname} - {module} - {message} - {pathname}',
            'style': '{',
        },
        'for_error_and_critical': {
            'format': '{asctime} - {levelname} - {module} - {message} - {pathname} - {exc_info}',
            'style': '{',
        }
    },
    'handlers': {
        'console': {
            'filters': ['True'],
            'class': 'logging.StreamHandler',
            'formatter': 'for_debug',
        },
        'general': {
            'filters': ['False'],
            'class': 'logging.FileHandler',
            'formatter': 'for_debug',
            'filename': 'general.log',
        },
        'errors': {
            'class': 'logging.FileHandler',
            'formatter': 'for_error_and_critical',
            'filename': 'errors.log',
        },
        'security': {
            'class': 'logging.FileHandler',
            'formatter': 'for_error_and_critical',
            'filename': 'security.log',
        },
        'mail_admins': {
            'filters': ['False'],
            'class': 'django.utils.log.AdminEmailHandler',
            'formatter': 'for_warning',
        }
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'general'],
            'level': 'INFO',
            'propagate': True,
        },
        'django.request': {
            'handlers': ['errors', 'mail_admins'],
            'level': 'ERROR',
        },
        'django.server': {
            'handlers': ['errors', 'mail_admins'],
            'level': 'ERROR',
        },
        'django.security': {
            'handlers': ['security'],
            'level': 'INFO',
        },
        'django.template': {
            'handlers': ['errors'],
            'level': 'ERROR',
        },
        'django.db.backends': {
            'handlers': ['errors'],
            'level': 'ERROR',
        },
    },
}

ROOT_URLCONF = 'News.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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


WSGI_APPLICATION = 'News.wsgi.application'


AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'table',
    'django_filters',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.yandex',
    "django_apscheduler",
]


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': os.path.join(BASE_DIR, 'cache_files'),
        'TIMEOUT': 60,
    }
}


LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_HOST = 'smtp.yandex.ru'

EMAIL_PORT = 465

EMAIL_HOST_USER = 'solomonovyegor'

EMAIL_HOST_PASSWORD = 'zojgec-vocFuj-9codna'

EMAIL_USE_SSL = True

DEFAULT_FROM_EMAIL = 'solomonovyegor@yandex.ru'

ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

ACCOUNT_EMAIL_REQUIRED = True

ACCOUNT_AUTHENTICATION_METHOD = 'email'

APSCHEDULER_DATETIME_FORMAT = "N j, Y, f:s a"
APSCHEDULER_RUN_NOW_TIMEOUT = 25

CELERY_BROKER_URL = 'redis://localhost:6379'
CELERY_RESULT_BACKEND = 'redis://localhost:6379'
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
