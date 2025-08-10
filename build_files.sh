#!/bin/bash

# Install dependencies
pip install -r requirements.txt

# Collect static files
python3.9 manage.py collectstatic --noinput

# Copy static files to a build folder for Vercel
mkdir -p staticfiles_build
cp -r staticfiles/* staticfiles_build/
