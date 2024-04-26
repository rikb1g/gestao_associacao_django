from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
from celery.schedules import crontab
from django.conf import settings

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'associacao.settings')

app = Celery('associacao')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'verificar_mensalidade_em_atraso': {
        'task': 'verificar_mensalidade_em_atraso',
        'schedule': crontab(minute=0, hour=0),
    },
}

# Define o nível de log para 'INFO'
app.conf.update(
    task_track_started=True,
    worker_log_format='%(asctime)s - %(levelname)s - %(message)s',
)
