# Admin dashboard for Gawaipos services.

This is used for our internal staff. This connects to all of our other services directly. It needs to connect to MySQL.

## Pre-requisites

### Python 3.9

`$ brew install python3`

### Poetry

`$ sudo pip3 install poetry`

## Project setup (for the first time)

`$ poetry install`

`$ poetry run python manage.py migrate`

`$ poetry run python manage.py createsuperuser # this will lets you login to the admin section`

## Run the project

``` sh
$ poetry shell
$ python manage.py runserver