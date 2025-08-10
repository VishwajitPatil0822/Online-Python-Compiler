#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Run collectstatic
python3 manage.py collectstatic --noinput

# Ensure the static build folder exists
mkdir -p staticfiles_build

# Move collected static files to the build folder
cp -r staticfiles/. staticfiles_build/
