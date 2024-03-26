#!/bin/bash

# Virtual environment create karna
python3.9 -m venv myenv

# Virtual environment activate karna
source myenv/bin/activate

# Dependencies install karna
python3.9 -m pip install -r requirements.txt 

# Django install karna
python3.9 -m pip install django

# Migrations banana
echo "Make Migration"
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinput 

# Static files collect karna
echo "Collect Static"
python3.9 manage.py collectstatic --noinput 

# Virtual environment deactivate karna
deactivate

echo "Build process completed successfully"
