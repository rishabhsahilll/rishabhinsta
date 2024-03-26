#!/bin/bash

# Virtual environment create karna
python3.9 -m venv myenv

# Virtual environment activate karna
source myenv/bin/activate

# Dependencies install karna

python3.9 -m pip install asgiref==3.7.2
python3.9 -m pip install boto3==1.14.32
python3.9 -m pip install botocore==1.17.32
python3.9 -m pip install channels==4.0.0
python3.9 -m pip install daphne
python3.9 -m pip install Django==5.0.1
python3.9 -m pip install django-appconf==1.0.4
python3.9 -m pip install django-crispy-forms==1.9.2
python3.9 -m pip install django-imagekit
python3.9 -m pip install django-storages
python3.9 -m pip install django-taggit
python3.9 -m pip install docutils
python3.9 -m pip install gunicorn
python3.9 -m pip install jmespath
python3.9 -m pip install pilkit
python3.9 -m pip install pillow
python3.9 -m pip install python-dotenv
python3.9 -m pip install pytz
python3.9 -m pip install s3transfer
python3.9 -m pip install six
python3.9 -m pip install sqlparse
python3.9 -m pip install urllib3
python3.9 -m pip install django-cloudinary-storage
python3.9 -m pip install dj-database-url
python3.9 -m pip install psycopg2-binary


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
