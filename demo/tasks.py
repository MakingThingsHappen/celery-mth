# -*- coding: utf-8 -*-
from .celery import app


@app.task(name='train.train')
def train(x, y):
    return x + y
