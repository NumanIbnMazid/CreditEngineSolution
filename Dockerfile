# pull official base image
FROM python:3.8-alpine

# set work directory
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DEBUG 0

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev jpeg-dev zlib-dev openssl-dev cargo \
    && apk add postgresql-dev gcc python3-dev musl-dev jpeg-dev zlib-dev openssl-dev cargo \
    && apk del build-deps \
    && apk --no-cache add bash musl-dev libffi-dev linux-headers g++

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# collect static files
RUN python manage.py collectstatic --noinput

# add and run as non-root user
RUN adduser -D myuser
USER myuser

# run gunicorn
CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT