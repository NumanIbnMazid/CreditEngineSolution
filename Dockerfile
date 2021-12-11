FROM python:3.8-alpine as base

# set environment variables
ENV CREDIT_ENGINE=/home/app/credit_engine
ENV APP_USER=credit_engine_user

# set environment variables
ENV PYTHONFAULTHANDLER=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONHASHSEED=random
ENV PYTHONUNBUFFERED=1

RUN addgroup -S $APP_USER && adduser -S $APP_USER -G $APP_USER
# set work directory

RUN mkdir -p $CREDIT_ENGINE
RUN mkdir -p $CREDIT_ENGINE/static

# where the code lives
WORKDIR $CREDIT_ENGINE

FROM base as builder

ENV PIP_DEFAULT_TIMEOUT=100 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    POETRY_VERSION=1.1.11

RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql-dev gcc python3-dev musl-dev \
    && apk del build-deps \
    && apk --no-cache add musl-dev libffi-dev linux-headers g++

RUN pip install --upgrade pip

# copy project
COPY . $CREDIT_ENGINE

RUN pip install --no-cache-dir -r requirements.txt
COPY ./entrypoint.sh $CREDIT_ENGINE

CMD ["/bin/bash", "/home/app/credit_engine/entrypoint.sh"]