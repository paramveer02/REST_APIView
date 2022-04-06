FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN mkdir /apidir

WORKDIR /apidir

ADD . /apidir/

RUN pip install -r requirements.txt

