FROM python:alpine3.7

COPY requirements.txt /
RUN pip3 install -r /requirements.txt

COPY . /AppServer
WORKDIR /AppServer

ENV FLASK_APP=AppServer

ENTRYPOINT ["./gunicorn_starter.sh"]
