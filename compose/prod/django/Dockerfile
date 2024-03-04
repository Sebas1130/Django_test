FROM python:3.8.15-alpine

LABEL maintainer="sebaspenagos11@gmail.com"

RUN apk update \
    && pip install -U pip \
    && apk add --no-cache gettext libffi libffi-dev libressl-dev postgresql-dev \
    && mkdir -p /app/ \
    && mkdir -p /home/data/www

COPY ./requirements.txt /app/
RUN set -ex \
    && apk add --no-cache --virtual .build-deps build-base \
    && pip install psycopg2 \
    && pip install -r /app/requirements.txt \
    && apk del .build-deps

COPY ./compose/dev/django/start /
RUN chmod +x /start

COPY ./compose/dev/django/entrypoint /
RUN chmod +x /entrypoint

# ADD proyect to docker
COPY ./proyect/* /app/
COPY ./registry/* /app/
COPY ./TestPython/* /app/
COPY ./manage.py /app/

WORKDIR /app

ENTRYPOINT [ "/entrypoint" ] 

CMD ["/start"]