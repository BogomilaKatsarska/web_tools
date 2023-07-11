"""
2:23
TODO for project: pip freeze > requirements.txt

1.Cashing(Django's cache framework): to save somewhere a pubic state for something so that we load it easy.
To cache something is to save the result of an expensive calculation so that you don't have to perform the
calculation next time.
Makes the app more stable. Gives better user experience.

60*15 = 15min -> the cache is saved for 15minutes. 60seconds x 15

cache = []

def fib(n):
    if len(cache) >= n:
        return cache[n]
    cache[n] = fib(n-1) + fib(n-2)

TODO for project(or below): add Memcached in settings.py
It is app for caching data. It is entirely memory-based cache server
TODO for project: add Redis - in memory DB that can be used for caching
TODO: pip install redis

You will need a Redis server running either locally or on a remote machine
used for message field

2.Cookies:
small file of plain text with no executable code, used to store information

3.Sessions(Django's sessions framework):
The sessions help you to store and retreive arbitrary data on a per-site-visitor basis
- keep track of the 'state' between the site and the particular browser
- they are made through cookies(small file of plain text with no executable code, used to store information)
- used for warning messages, last viewed items, basket
- authentication works through sessions

4.Middleware:
A framework of hooks into Django's request/response processing
Go through them before and after each request
Ordering of middlewares matters
#TODO add middleware.py

5.Signals:
Execute a code when an event has occured

6.Pagination:

"""

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%0p!gbep+7o^p8khnkanwn1o6@5%jdlsazgbkt=u%f%y^=+7m7'

DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'web_tools.web',
]

MIDDLEWARE = [
    'web_tools.web.middleware.measure_time_middleware',
    'web_tools.web.middleware.MeasureTimeMiddleware',
    #first and last adds cache to all views - does not work well with dynamic data
    #'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'web_tools.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates']
        ,
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

WSGI_APPLICATION = 'web_tools.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# CACHES = {
#     "default": {
#         "BACKEND": "django.core.cache.backends.memcached.PyMemcacheCache",
#         "LOCATION": "127.0.0.1:11211",
#     }
# }
if DEBUG:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.dummy.DummyCache",
        }
    }
else:
    CACHES = {
        "default": {
            "BACKEND": "django.core.cache.backends.redis.RedisCache",
            "LOCATION": "redis://127.0.0.1:6379",
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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
