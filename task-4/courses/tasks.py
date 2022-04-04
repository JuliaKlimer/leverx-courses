from celery import Task
from .celery_main import app


# periodic task
class PeriodicTask(Task):
    def send_email(self, email):
        print(f'Message is sent to {email}')


# static task
class StaticTask(Task):
    def run(self, *args, **kwargs):
        print('Static task is completed')


app.register_task(StaticTask)
app.register_task(PeriodicTask)
