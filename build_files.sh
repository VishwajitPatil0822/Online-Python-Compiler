#!/bin/bash
python manage.py collectstatic --noinput

mkdir -p staticfiles_build
cp -r static/* staticfiles_build/

