FROM python:3
LABEL website='https://github.com/EISerova/weather-app-api'
LABEL desc='This weather-project create for studing'
LABEL email='katyaserova@yandex.ru'

ENV PYTHONUNBUFFERED 1

EXPOSE 8000

WORKDIR /usr/scr/weather-drf/

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt


COPY . /usr/scr/weather-drf/

