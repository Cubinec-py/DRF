import os

from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'src.core.settings.dev')

app = Celery('src.core')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'change_truck_location': {
        'task': 'src.api.truck.tasks.change_truck_location',
        'schedule': crontab(minute='*/3'),
    }
}
