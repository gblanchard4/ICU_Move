#!/bin/bash

# Remove DB and migrations
rm db.sqlite3
rm samples/migrations/0*_*.py

## Fake it till you make it
./manage.py migrate
./manage.py makemigrations samples
./manage.py sqlmigrate samples 0001
./manage.py migrate
./manage.py createsuperuser
