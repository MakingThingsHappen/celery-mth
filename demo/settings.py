# -*- coding: utf-8 -*-
BROKER_URL = 'redis://192.168.1.120:6379//1'
CELERY_RESULT_BACKEND = 'redis://192.168.1.120:6379//0'
CELERY_ACCEPT_CONTENT = ['pickle', 'json', 'msgpack', 'yaml']


