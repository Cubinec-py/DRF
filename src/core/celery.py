import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings.dev')

app = Celery('core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'change_truck_location': {
        'task': 'api.truck.tasks.change_truck_location',
        'schedule': crontab(minute='*/3'),
    }
}
