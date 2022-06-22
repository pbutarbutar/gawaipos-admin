FROM python:3.9.6 AS base

#RUN apk add gcc musl-dev mariadb-connector-c-dev

ENV PYTHONUNBUFFERED 1

RUN mkdir /gawaipos

WORKDIR /gawaipos

COPY . .

COPY ./requirements.txt /requirements.txt

RUN /usr/local/bin/python -m pip install --upgrade pip


RUN pip install -r /requirements.txt

RUN test -d /etc/vault && echo "vault directory exists" || mkdir /etc/vault
RUN test -f /etc/vault/env && echo "vault env exists" || touch /etc/vault/env


# Run the binary program produced by ``
CMD ["bash", "-c", "source /etc/vault/env"]