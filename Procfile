web: gunicorn mentorbot.mentorbot.wsgi --log-file -
web: python manage.py collectstatic
init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade
