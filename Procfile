web: gunicorn mentorbot.wsgi --log-file -
web: python manage.py collectstatic
init: python manage.py db makemigrations
migrate: python manage.py db migrate
upgrade: python manage.py db upgrade
