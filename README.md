# Admin dashboard for Gawaipos services.

This is used for our internal staff. This connects to all of our other services directly. It needs to connect to MySQL.

## Pre-requisites

### Python 3.9

`$ brew install python3`

`$ pip install -r /path/to/requirements.txt`

``` sh
$ python manage.py migrate
$ python manage.py createsuperuser # this will lets you login to the admin section`
$ python manage.py runserver
