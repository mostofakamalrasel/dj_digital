from .base import *

################################
##     BASE CONFIGURATION     ##
################################

DEBUG = True

ALLOWED_HOSTS = config('ALLOWED_HOSTS')

################################
##      WSGI CONFIGURATION    ##
################################

WSGI_APPLICATION = 'djdigital.wsgi.application'

################################
##    DATABASE CONFIGURATION  ##
################################

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}