import os

import countdown as countdown
from celery import Celery
from celery.contrib.pytest import celery_app

from .tasks import PeriodicTask
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courses.settings')

app = Celery('courses', broker='CELERY_BROKER_URL')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

# schedule
app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'notifications.tasks.send_email',
        'schedule': 10,
        'args': ('klimava27@gmail.com',)
    }
}

send_mail_task = PeriodicTask.send_email('klimava27@gmail.com')
send_mail_task.apply_async(
    ('klimava27@gmail.com',),
    countdown=10
)

# Tasks queue
celery_app.conf.task_routes = {
    'courses.celery_main.send_mail_task': {'queue': 'mail', }
}
