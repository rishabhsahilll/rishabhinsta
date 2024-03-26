#!/bin/bash

# Starting build process
echo "BUILD START"

# Installing dependencies
python3.9 -m pip install -r requirements.txt 

# Step 3: Update Dependencies
python3.9 -m pip install --upgrade urllib3 cloudinary

# Step 5: Check Dependencies
python3.9 -m pip list | grep urllib3
python3.9 -m pip list | grep cloudinary


# Making migrations
echo "Make Migration"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput 

# Collecting static files
echo "Collect Static"
python3.9 manage.py collectstatic --noinput 

echo "Build process completed successfully"