web: gunicorn mentorbot.wsgi --log-file -
web: python mentorbot.manage.py collectstatic
init: python mentorbot.manage.py db makemigrations
migrate: python mentorbot.manage.py db migrate
upgrade: python mentorbot.manage.py db upgrade
