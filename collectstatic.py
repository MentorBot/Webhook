from apscheduler.schedulers.blocking import BlockingScheduler

sched = BlockingScheduler()

@sched.scheduled_job('interval', minutes=3)
def times_job():
    return 'heroku run cd mentorbot && python manage.py collectstatic'

sched.start()
