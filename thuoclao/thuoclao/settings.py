"""
Django settings for thuoclao project.

Generated by 'django-admin startproject' using Django 2.0.4.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.0/ref/settings/
"""
import os


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#
# PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))
#
# sys.path.append(os.path.join(PROJECT_PATH, 'lib/'))
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_ttj5t!3fo03!k(w!o85ml0wk5$eb$%#!cg(^67x3h54&!vqw2'

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
    'check',
    'accounts',
    'lib',
    'rest_framework',
    'thuoclao',
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

ROOT_URLCONF = 'thuoclao.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates'))],
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

WSGI_APPLICATION = 'thuoclao.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'thuoclao',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'db',
#        'NAME': 'thuoclao',
#        'USER': 'thuoclao',
#        'PASSWORD': 'thuoclao',
#        'HOST': '192.168.30.61',
#        'PORT': '3306'
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/
# STATIC_ROOT = os.path.join(BASE_DIR, "static")
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
    ('check', os.path.join(BASE_DIR, 'check', 'static')),
    ('accounts', os.path.join(BASE_DIR, 'accounts', 'static')),
]

LOGIN_REDIRECT_URL = 'index'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'thuoclao/media')

# Email send notification
FROM_EMAIL = 'poisonous1205@gmail.com'
PASSWD_MAIL = 'minhnguyen'
SMTP_SERVER = 'smtp.gmail.com:587'

# Telegram token
TOKEN = '518593888:AAExHxExaTD9XzY9WAkRnIDexjbkGDhsnO4'

# Influx config
INFLUXDB_DB = 'thuoclao'
INFLUXDB_USER = 'admin'
INFLUXDB_USER_PASSWORD = 'admin'
INFLUXDB_HOST = 'influxdb'
INFLUXDB_PORT = "8086"

# Authentication
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    )
}


# MTicket
MTICKET_TOKEN = "c84964fd0ab36e4b044f7f4672e3fa7ce4fecf830343eeef"
MTICKET_SERVER = "192.168.100.23"
LIST_TOPIC_LINK = "http://{}/api/list_topic".format(MTICKET_SERVER)
CREATE_TOPIC_LINK = "http://{}/api/tk_create".format(MTICKET_SERVER)

# Redis
REDIS_SERVER = 'redis:6379'
