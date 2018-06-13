web: gunicorn mentorbot.wsgi --log-file -
web: cd mentorbot && python manage.py collectstatic
init: cd mentorbot && python manage.py db makemigrations
migrate: cd mentorbot && python manage.py db migrate
upgrade: cd mentorbot && python mentorbot.manage.py db upgrade
