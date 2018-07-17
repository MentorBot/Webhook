from mentorbot.settings.base import *

DEBUG = True

# SECRET_KEY = config('SECRET_KEY')
SECRET_KEY ="hsjdjfjbsdjhfbjhfbdjhbfjdshbfjhsdbfjhsdbfjhsbd"

DATABASES = {
    'default': dj_database_url.config()
}
