"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""
import environ

# Initialise environment variables
env = environ.Env()
# Reading the .env file
environ.Env.read_env()

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

SECRET_KEY = env('SECRET_KEY', default='django-insecure-+#@@8#hjqz+9^@vi6rd+2g$(362a_4h%zg#h#3b&1ud!k5#uwz')
DEBUG = True

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '356f-2401-4900-1c26-65f5-19ff-f806-9a9e-3867.ngrok-free.app',
    'digitalm-mysite.onrender.com',
    '.render.com',
]

CSRF_TRUSTED_ORIGINS=[
    'https://356f-2401-4900-1c26-65f5-19ff-f806-9a9e-3867.ngrok-free.app',
    'https://digitalm-mysite.onrender.com',
    'https://*.render.com',
]


# Application definition

INSTALLED_APPS = [
    'myapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# Static files (CSS, JavaScript, Images)

import os

# STATIC FILES
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# MEDIA FILES
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

import os
import environ
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Initialize environment variables
env = environ.Env()
environ.Env.read_env(BASE_DIR / ".env") # Load variables from .env

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env.bool("DEBUG", default=False)

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '356f-2401-4900-1c26-65f5-19ff-f806-9a9e-3867.ngrok-free.app',
    'digitalm-mysite.onrender.com',
    '.render.com',
]

CSRF_TRUSTED_ORIGINS = [
    'https://356f-2401-4900-1c26-65f5-19ff-f806-9a9e-3867.ngrok-free.app',
    'https://digitalm-mysite.onrender.com',
    'https://*.render.com',
]

# Razorpay & Cashfree credentials (DO NOT HARDCODE)
RAZORPAY_KEY_ID = env('RAZORPAY_KEY_ID', default='rzp_test_KUuSPp457DO8fX')
RAZORPAY_KEY_SECRET = env('RAZORPAY_KEY_SECRET', default='Na2dCbSZApOHVEDz3Op9i1Dp')

CASHFREE_CLIENT_ID = env('CASHFREE_CLIENT_ID', default='CF10495031CUVNK0VSI14C73EO7R10')
CASHFREE_CLIENT_SECRET = env('CASHFREE_CLIENT_SECRET',default='cfsk_ma_test_c1906312d59e66f661f75fe0d7e81d8d_c9527439')
CASHFREE_PAYOUT_BASE_URL = env("CASHFREE_PAYOUT_BASE_URL", default="https://payout-api.cashfree.com/payout/v1/")


# Database (use SQLite by default)
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}

# Static & Media files
STATIC_URL = "/static/"
STATICFILES_DIRS = [os.path.join(BASE_DIR, "static")]

MEDIA_URL = "/media/"
MEDIA_ROOT = os.path.join(BASE_DIR, "media")

# Default primary key field type
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
