FROM python:3.9-slim

ENV APP_HOME /app
WORKDIR $APP_HOME

ENV PYTHONUNBUFFERED 1

RUN apt-get update -y && apt-get install -y -- \
    gettext \
    git \
    build-essential \
    libpq-dev

COPY ./requirements.txt requirements.txt
COPY ./src .

RUN pip install -r requirements.txt


ENV PORT=8000
EXPOSE $PORT

CMD uvicorn src.app.main:app --reload --host 0.0.0.0 --port $PORT