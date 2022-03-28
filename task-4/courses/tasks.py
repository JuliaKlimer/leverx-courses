import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'courses.settings')

app = Celery('courses', broker='CELERY_BROKER_URL')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

#schedule
app.conf.beat_schedule = {
    'every-10-seconds': {
        'task': 'notifications.tasks.send_email',
        'schedule': 10,
        'args': ('klimava27@gmail.com',)
    }
}
