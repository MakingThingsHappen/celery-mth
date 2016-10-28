# -*- coding: utf-8 -*-
from __future__ import absolute_import
from . import settings
from celery import Celery

app = Celery('worker1')
app.config_from_object(settings)

# 之所以是demo是因为-A demo
app.autodiscover_tasks(('demo',))
