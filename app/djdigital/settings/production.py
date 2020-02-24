from .base import *

################################
##     BASE CONFIGURATION     ##
################################

DEBUG = False

ALLOWED_HOSTS = config('ALLOWED_HOSTS').split(' ')

################################
##      WSGI CONFIGURATION    ##
################################

WSGI_APPLICATION = 'djdigital.wsgi.application'

################################
##    DATABASE CONFIGURATION  ##
################################

DATABASES = {
    'default': {
        'ENGINE': config('SQL_ENGINE'),
        'NAME': config('SQL_DATABASE'),
        'USER': config('SQL_USER'),
        'PASSWORD': config('SQL_PASSWORD'),
        'HOST': config('SQL_HOST'),
        'PORT': config('SQL_PORT'),
    }
}

################################
##      AUTH CONFIGURATION    ##
################################

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