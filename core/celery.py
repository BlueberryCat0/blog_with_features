from celery import Celery
from django.conf import settings
# from datetime import timedelta
from celery.schedules import crontab
import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
app = Celery('core')
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

# CELERY_BEAT_SCHEDULE = {
#     'print_hello_world': {
#         'task': 'apps.posts.PrintHelloWorld',
#         'shedule': crontab(minute='*/1'),
#     }
# }

# app.conf.beat_schedule = {
#     'print_hello_world': {
#         'task': 'apps.posts.PrintHelloWorld',
#         'shedule': crontab(minute='*/1'),
#     }
# }
