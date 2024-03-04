FROM python:3.8.15-alpine

LABEL maintainer="sebaspenagos11@gmail.com"

RUN apk update \
    && apk add --no-cache build-base libressl-dev postgresql-dev \
    && pip install -U pip \
    && mkdir -p /app/ \
    && mkdir -p /home/data/www


COPY ../../../../requirements.txt /app/

RUN  pip install -r /app/requirements.txt
    #set -ex \
    #&& apk add --no-cache --virtual .build-deps build-base \
    #&& pip install psycopg2 \ 
    #&& apk del .build-deps

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