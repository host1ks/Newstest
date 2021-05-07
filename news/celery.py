import os

from celery import Celery

from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news.settings')

app = Celery('news')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'printing': {
        'task': 'main.tasks.upvote_clean',
        'schedule': crontab(hour='1'),
    }
}
