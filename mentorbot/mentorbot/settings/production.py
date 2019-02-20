from mentorbot.settings.base import *

DEBUG = True


DATABASES = {
    'default': dj_database_url.config()
}
