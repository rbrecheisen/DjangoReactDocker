#!/bin/bash

python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

gunicorn django_project.wsgi:application -w 2 -b 0.0.0.0:8000 -t 81240