"""
Django settings for upwards project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from .celery import app as celery_app

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'SECRET_KEY'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    'django_extensions',
    'rest_framework',
    'common.apps.CommonConfig',
    'social.apps.SocialConfig',
    'customer.apps.CustomerConfig',
    'eligibility.apps.EligibilityConfig',
    'pan.apps.PanConfig',
    'aadhaar.apps.AadhaarConfig',
    'documents.apps.DocumentsConfig',
    'messenger.apps.MessengerConfig',
    'activity.apps.ActivityConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'upwards.urls'

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

WSGI_APPLICATION = 'upwards.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'
MEDIA_ROOT = './media/'
MEDIA_URL = '/media/'
BASE_URL = 'BASE_URL'

FACEBOOK = {
    'data_url': 'https://graph.facebook.com/me?fields=id,cover,name,first_name,last_name,age_range,link,gender,locale,picture,timezone,updated_time,verified,email&access_token={platform_token}',
}
REQUIRES_FB_REVIEW = ['user_birthday', 'user_education_history', 'user_hometown',
                      'user_location', 'user_managed_groups', 'user_relationships', 'user_work_history']

GOOGLE = {
    'data_url': 'https://www.googleapis.com/oauth2/v3/tokeninfo?id_token=={platform_token}',
}

LINKEDIN = {
    'auth_url': 'https://www.linkedin.com/oauth/v2/accessToken',
    'auth_header': {
        'Content-Type': 'application/x-www-form-urlencoded',
        'grant_type': 'authorization_code',
        'code': '{auth_code}',
        'redirect_uri': BASE_URL + 'customer/linkedin_auth',
        'client_id': 'client_id',
        'client_secret': 'client_secret'
    },
    'data_url': 'https://api.linkedin.com/v1/people/~:(id,first-name,last-name,maiden-name,formatted-name,phonetic-first-name,phonetic-last-name,formatted-phonetic-name,headline,industry,current-share,num-connections,num-connections-capped,specialties,positions,picture-url,picture-urls::(original),site-standard-profile-request,api-standard-profile-request,public-profile-url,location:(name),summary)?format=json',
    'data_auth': {
        'Authorization': 'Bearer {platform_token}',
    }


}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'nimesh.aug11@gmail.com'
SERVER_EMAIL = 'nimesh.aug11@gmail.com'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'nimesh.aug11@gmail.com'
EMAIL_HOST_PASSWORD = 'password'
EMAIL_USE_TLS = True


CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = 'Asia/Kolkata'


CELERY_DEFAULT_QUEUE = 'sqs_queue_name'
CELERY_QUEUES = {
    CELERY_DEFAULT_QUEUE: {
        'exchange': CELERY_DEFAULT_QUEUE,
        'binding_key': CELERY_DEFAULT_QUEUE,
    }
}

BROKER_TRANSPORT = 'sqs'
BROKER_TRANSPORT_OPTIONS = {
    'region': 'region',
}
BROKER_USER = AWS_ACCESS_KEY_ID
BROKER_PASSWORD = AWS_SECRET_ACCESS_KEY


POST_OTP_MESSAGE = " is your Upwards App OTP"
SMS_GATEWAY_USER_NAME = ""
SMS_GATEWAY_API_KEY = ""
SMS_SENDER_NAME = "Upwards"
SMS_GATEWAY_URL = "http://api.textlocal.in/send/?"


DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
AWS_S3_ACCESS_KEY_ID = 'AWS_S3_ACCESS_KEY_ID'
AWS_S3_SECRET_ACCESS_KEY = 'AWS_S3_SECRET_ACCESS_KEY'
AWS_STORAGE_BUCKET_NAME = 'AWS_STORAGE_BUCKET_NAME'
