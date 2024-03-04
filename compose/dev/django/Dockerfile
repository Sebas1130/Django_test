FROM python:3.8.15-alpine

LABEL maintainer="sebaspenagos11@gmail.com"

RUN apk update \
    && apk add build-base postgresql-dev libffi-dev openssl-dev \
    && pip install -U pip \
    && mkdir -p /app/ \
    && mkdir -p /home/data/www


COPY ../../../../requirements.txt /app/

RUN set -ex \
    && apk add build-base \
    && pip install -r /app/requirements.txt 
#    && apk del .build-deps

COPY ./compose/dev/django/ssh/config /root/.ssh/config

COPY ./compose/dev/django/keys/ /root/.ssh/
RUN chmod 600 /root/.ssh/*

COPY ./compose/dev/django/start /
RUN chmod +x /start

COPY ./compose/dev/django/entrypoint /
RUN chmod +x /entrypoint

WORKDIR /app

ENTRYPOINT [ "/entrypoint" ] 

CMD ["/start"]