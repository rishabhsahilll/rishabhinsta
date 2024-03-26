#!/bin/bash

# Starting build process
echo "BUILD START"

# Installing dependencies
python3.9 -m pip install -r requirements.txt 

# Making migrations
echo "Make Migration"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput 

# Collecting static files
echo "Collect Static"
python3.9 manage.py collectstatic --noinput 

echo "Build process completed successfully"
