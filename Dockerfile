# Base Image
FROM python:3.8.3-alpine

ENV CREDIT_ENGINE=/usr/src/

# set working directory
WORKDIR $CREDIT_ENGINE

# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV LANG C.UTF-8
ENV APP_USER=creditengine

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add bash musl-dev linux-headers g++ libffi-dev


# install environment dependencies
RUN pip install --upgrade pip 

# RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER
# USER $APP_USER

# Install project dependencies
COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install -r requirements.txt

# copy project to working dir
COPY . $CREDIT_ENGINE

# Use In Production Mode
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT