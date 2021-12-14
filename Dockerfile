# Base Image
FROM python:3.8.3-alpine

# set working directory
WORKDIR /usr/src/

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive 

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add bash musl-dev linux-headers g++ libffi-dev


# install environment dependencies
RUN pip install --upgrade pip 
RUN pip install psycopg2 pipenv

# Install project dependencies
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r requirements.txt

# copy project to working dir
COPY . /usr/src/

CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT