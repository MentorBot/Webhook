from mentorbot.settings.base import *

DEBUG = False

SECRET_KEY = config('SECRET_KEY')

DATABASES = {
    'default': dj_database_url.config()
}
