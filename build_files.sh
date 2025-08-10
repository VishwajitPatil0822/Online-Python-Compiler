#!/bin/bash

pip install -r requirements.txt

python3.9 manage.py collectstatic

# Ensure the static build folder exists
mkdir -p staticfiles_build

# Move collected static files to the build folder
cp -r static/. static_build/
