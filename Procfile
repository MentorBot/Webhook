web: gunicorn mentorbot.wsgi --log-file -
web: python manage.py collectstatic
init: cd mentorbot && python manage.py makemigrations
migrate: cd mentorbot && python manage.py migrate
upgrade: cd mentorbot && python mentorbot.manage.py upgrade
