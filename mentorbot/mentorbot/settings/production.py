from mentorbot.settings.base import *

DEBUG = True

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': dj_database_url.config()
}

# DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'mentor-bots',
#        'USER': 'jus_machungwa',
#        'PASSWORD': 'Okusimba@1',
#        'HOST': 'localhost',
#        'PORT': '',
# }}
