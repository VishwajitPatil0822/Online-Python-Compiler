#!/bin/bash
python3.9 manage.py collectstatic --noinput

mkdir -p staticfiles_build
cp -r static/* staticfiles_build/

