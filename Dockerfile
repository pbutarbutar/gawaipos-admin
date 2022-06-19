FROM python:3.9-alpine

RUN apk add gcc musl-dev mariadb-connector-c-dev

ENV PYTHONUNBUFFERED 1

RUN mkdir /gawaipos

WORKDIR /gawaipos

COPY . .

COPY ./requirements.txt /requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip

RUN pip install --upgrade setuptools

RUN pip install -r /requirements.txt

# Create a user that can run your container
RUN adduser -D user
USER user