from mentorbot.settings.base import *

DEBUG = True

# SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': 'postgres://jktfggrohrfhyd:dfb17db90e4dc829dd04582d10f1664d8c1b9eca4e5340c2ab9ff92d22b3af12@ec2-50-19-86-139.compute-1.amazonaws.com:5432/d4fmv6idbe7bn3'
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
