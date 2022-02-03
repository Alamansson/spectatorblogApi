from __future__ import absolute_import
import os
from celery import Celery
from django.conf import settings


# установите модуль настроек Django по умолчанию для программы «сельдерей»
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blogapi.settings')
app = Celery('blogapi')


# Использование здесь строки означает, что обработчику не нужно будет
# замариновать объект при использовании Windows.
app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)


@app.task(bind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))
