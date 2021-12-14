""" # Project Common Settings # """
from pathlib import Path
import os
from dotenv import load_dotenv


""" *** Project Directory Configurations *** """
BASE_DIR = Path(__file__).resolve().parent.parent.parent

""" *** Read Project Environment File *** """
env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(dotenv_path=env_path)

""" *** Application Secret Key *** """
SECRET_KEY = os.environ.get('SECRET_KEY')

""" *** DEBUG Configurations *** """
# DEBUG = False if eval(str(os.environ.get('IS_PRODUCTION'))) or eval(str(os.environ.get('IS_STAGING'))) else True
DEBUG = True


""" *** Database URL Configurations *** """
if eval(str(os.environ.get('IS_PRODUCTION'))) and os.environ.get('PRODUCTION_DATABASE_URL'):
    DYNAMIC_DATABASE_URL = os.environ.get('PRODUCTION_DATABASE_URL')
elif eval(str(os.environ.get('IS_STAGING'))) and os.environ.get('STAGING_DATABASE_URL'):
    DYNAMIC_DATABASE_URL = os.environ.get('STAGING_DATABASE_URL')
elif os.environ.get('DEVELOPMENT_DATABASE_URL'):
    DYNAMIC_DATABASE_URL = os.environ.get('DEVELOPMENT_DATABASE_URL')
else:
    DYNAMIC_DATABASE_URL = None


""" *** Application Definitions *** """
THIRD_PARTY_APPS = [
    # Django Crispy Forms
    "crispy_forms",
    # Django Rosetta
    "rosetta",
    # Django Select2
    "django_select2",
    # Django Allauth
    "allauth",
    "allauth.account",
    # Django Corsheaders
    "corsheaders",
]

LOCAL_APPS = [
    "users",
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # Django WhiteNoise
    "whitenoise.runserver_nostatic",
    'django.contrib.staticfiles',
    'django.contrib.sites',
] + THIRD_PARTY_APPS + LOCAL_APPS


""" *** Authentication Definitions *** """
AUTH_USER_MODEL = 'users.User'
AUTHENTICATION_BACKENDS = [
    'allauth.account.auth_backends.AuthenticationBackend',
]


""" *** Middlewares Definitions *** """
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # Django Whitenoise Middleware
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    # Middleware for Locale
    'django.middleware.locale.LocaleMiddleware',
    # Django Corsheaders Middleware
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

""" *** Template Definitions *** """
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

""" *** Authentication Password Validators *** """
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

""" *** Localization Configuration *** """
LOCALE_PATHS = [os.path.join(BASE_DIR, 'locale')]
LANGUAGES = [
    ('en', 'English'),
    ('bn', 'Bengali'),
    ('ja', 'Japan')
]
LANGUAGE_CODE = 'bn' #'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

""" *** Static & Media Files Configurations *** """
STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'staticfiles'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

""" *** Other Definitions *** """
SITE_ID = 1
ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'
# ASGI_APPLICATION = "config.routing.application"
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
HOME_URL = "/"
ADMIN_LOGIN_URL = "/accounts/login"
LOGIN_URL = ADMIN_LOGIN_URL
SITE_DOMAIN = "creditenginesolution.herokuapp.com"

"""
----------------------- * Django WhiteNoise Configurations * -----------------------
"""

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


"""
----------------------- * Rosetta Configurations * -----------------------
"""

ROSETTA_SHOW_AT_ADMIN_PANEL = True


"""
----------------------- * Crispy Form Configurations * -----------------------
"""

CRISPY_FAIL_SILENTLY = not DEBUG
CRISPY_TEMPLATE_PACK = 'bootstrap5'
CRISPY_CLASS_CONVERTERS = {'textinput': "textinput"}
help_text_inline = False
error_text_inline = False
html5_required = True
form_show_labels = True

"""
----------------------- * Cache Configurations * -----------------------
"""

REDIS_HOST = os.environ.get('REDIS_HOST', '127.0.0.1')
REDIS_PORT = os.environ.get('REDIS_PORT', '6379')

SESSIONS_ENGINE = 'django.contrib.sessions.backends.cache'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    },
    "select2": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": f"redis://{REDIS_HOST}:{REDIS_PORT}/2",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
        }
    }
}

"""
----------------------- * Django Allauth Configurations * -----------------------
"""
LOGIN_REDIRECT_URL = '/'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'none'  # mandatory, optional, none
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 7
ACCOUNT_USER_MODEL_EMAIL_FIELD = "email"
ACCOUNT_USER_MODEL_USERNAME_FIELD = "username"
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 300
ACCOUNT_EMAIL_SUBJECT_PREFIX = 'Credit Engine Solution Account Confirmation'


"""
----------------------- * Django Cors Header Configurations * -----------------------
"""
# CORS_ALLOWED_ORIGINS = [
#     "http://localhost:8080",
#     "http://127.0.0.1:9000",
#     "http://127.0.0.1:8000",
#     "http://0.0.0.0:8000",
#     "http://0.0.0.0:9000",
#     # open weather
#     "https://creditenginesolution.herokuapp.com",
#     "http://creditenginesolution.herokuapp.com",
#     "https://api.openweathermap.org",
#     "http://api.openweathermap.org",
#     "https://openweathermap.org",
#     "http://openweathermap.org",
# ]

CORS_ALLOW_ALL_ORIGINS = True

CORS_ALLOW_METHODS = [
    "DELETE",
    "GET",
    "OPTIONS",
    "PATCH",
    "POST",
    "PUT",
]
