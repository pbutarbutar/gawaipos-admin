FROM python:3.9.6 AS base

#RUN apk add gcc musl-dev mariadb-connector-c-dev

ENV PYTHONUNBUFFERED 1

RUN mkdir /gawaipos

WORKDIR /gawaipos

COPY . .

COPY ./requirements.txt /requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip

#RUN pip install --upgrade setuptools

#RUN pip install Pillow

RUN pip install -r /requirements.txt


# Run the binary program produced by ``
CMD ["bash", "-c", "source /gawaipos/env"]