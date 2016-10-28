FROM python:2
MAINTAINER yanzhao <649038269@qq.com>

RUN groupadd -r celery && useradd -r -g celery celery
RUN pip install celery redis
WORKDIR /practice/
COPY demo /practice/demo
COPY cmd.sh /

USER celery
CMD ["/cmd.sh"]
