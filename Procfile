web: gunicorn mentorbot.wsgi --log-file -
web: python manage.py collectstatic –noinput
init: python manage.py db init
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade
