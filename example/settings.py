import os
from environs import Env

env = Env()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'sqlite3.db',
    }
}

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    'statics',
]

SECRET_KEY = 'not-secret'

MIDDLEWARE = [
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
]

ROOT_URLCONF = 'example.urls'
WSGI_APPLICATION = 'example.wsgi.application'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
    },
]

INSTALLED_APPS = [
    'django.contrib.staticfiles',
]
INSTALLED_APPS += env.list("ADDITIONAL_APPS")
