#!/bin/bash
pip install --upgrade pip setuptools wheel distutils-pytest
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput

mkdir -p staticfiles_build
cp -r static/* staticfiles_build/

