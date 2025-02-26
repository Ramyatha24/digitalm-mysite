import environ
import os
from pathlib import Path

# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

BASE_DIR = Path(__file__).resolve().parent.parent

# Security settings
SECRET_KEY = env('SECRET_KEY', default='django-insecure-+#@@8#hjqz+9^@vi6rd+2g$(362a_4h%zg#h#3b&1ud!k5#uwz')
DEBUG = False  # Set to False in production

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

# Application definition
INSTALLED_APPS = [
    'myapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'whitenoise.runserver_nostatic',  # Ensures Whitenoise is used in development
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True

# Static files settings
STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'myapp' / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Media files (for user uploads)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Login/logout settings
LOGIN_URL = 'login'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Razorpay settings
RAZORPAY_KEY_ID = env('RAZORPAY_KEY_ID', default='rzp_test_KUuSPp457DO8fX')
RAZORPAY_KEY_SECRET = env('RAZORPAY_KEY_SECRET', default='Na2dCbSZApOHVEDz3Op9i1Dp')

# PayU Payouts settings
PAYU_PAYOUTS = {
    'API_KEY': env('PAYU_API_KEY', default='75DMsQ'),
    'SALT': env('PAYU_SALT', default=''),
    'CLIENT_ID': env('PAYU_CLIENT_ID', default='702f87fed2e6b5f0316de199901d56043abec58c917af25b437154cc331f75df'),
    'CLIENT_SECRET': env('PAYU_CLIENT_SECRET', default='65258bfdf5c5fff37c01b0bf6f8243051b56139cd40cf3cc9c317f3323f98f6d'),
    'BASE_URL': 'https://uat-api.payu.in',
}

# Serving media files in development
to_append = []
if DEBUG:
    from django.conf.urls.static import static
    to_append += static(MEDIA_URL, document_root=MEDIA_ROOT)
    urlpatterns = [] + to_append
