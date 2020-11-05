# pip install celery to make it working

import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pricetracker.settings')

app = Celery('pricetracker')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()