#!/bin/bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
python3.9 manage.py collectstatic --noinput

