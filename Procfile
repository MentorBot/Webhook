web: cd mentorbot && gunicorn mentorbot.wsgi --log-file -
web: cd mentorbot && python manage.py collectstatic
init: cd mentorbot && python manage.py makemigrations
migrate: cd mentorbot && python manage.py migrate
upgrade: cd mentorbot && python mentorbot.manage.py upgrade
