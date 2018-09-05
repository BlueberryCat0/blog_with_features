from core.celery import app
# from celery.task import task
from celery.schedules import crontab
from celery.decorators import periodic_task
from datetime import timedelta


# @app.task
# @periodic_task(run_every=(crontab(minute='*/1')))
@periodic_task(run_every=timedelta(seconds=30))
def run():
    print('Hello world every 60 seconds')
