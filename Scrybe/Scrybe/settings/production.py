from .base import *

DEBUG = False
ALLOWED_HOSTS = ['app.scrybe.com', ]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('PROD_DATABASE_NAME', ''),
        'USER': os.environ.get('PROD_DATABASE_USER', ''),
        'PASSWORD': os.environ.get('PROD_DATABASE_PASSWORD', ''),
        'HOST': os.environ.get('PROD_DATABASE_HOST', ''),
        'PORT': os.environ.get('PROD_DATABASE_PORT', ''),
    }
}