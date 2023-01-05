FROM python:3.11.0

RUN apt-get update && apt-get install -y postgresql-client

ENV PYTHONBUFFERED 1

RUN mkdir -p app/

COPY ./requirements.txt app/requirements.txt
RUN pip install -r /app/requirements.txt

WORKDIR /app
