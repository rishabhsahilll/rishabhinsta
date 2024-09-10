import os
import dj_database_url
import cloudinary_storage
from dotenv import load_dotenv

# # .env file ka path set karein
load_dotenv()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = os.environ.get('SEKRET_KEY')
SECRET_KEY = '<Key>'

DEBUG = True

ALLOWED_HOSTS = ['rishabhinsta.pythonanywhere.com','*']


INSTALLED_APPS = [

    # channels
    'daphne',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Cloudinary_storage
    'cloudinary_storage',
    'cloudinary',


    # My_apps.
    'blog',
    'users.apps.UsersConfig',
    'footer',
    'chat',

    # Third_party_apps.
    'crispy_forms',
    # taggit
    'taggit',
    #forthumbnails
    'imagekit',
    'storages',


]

if not DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
    
DBBACKUP_STORAGE = 'django.core.files.storage.FileSystemStorage'
DBBACKUP_STORAGE_OPTIONS = {'location':  os.path.join(BASE_DIR, 'backup')}

ASGI_APPLICATION = 'blog_project.asgi.application'

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels.layers.InMemoryChannelLayer',
    }
}

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware'
]

ROOT_URLCONF = 'blog_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'blog_project.wsgi.application'




# Local DataBase

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}




# Cloud DataBase

# DATABASES = {
#     'default': dj_database_url.config(
#         default=os.environ.get('DATA_BASE')
#     )
# }



AUTH_PASSWORD_VALIDATORS = [
    # {
    #     'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    # },
]


LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True



STATIC_URL = '/static/'
MEDIA_URL = '/media/'

# STATICFILES_DIRS = os.path.join(BASE_DIR, 'static')

# STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'), ]

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles", "static")

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'

CRISPY_TEMPLATE_PACK = 'bootstrap4'

LOGIN_REDIRECT_URL = 'blog:home'
LOGIN_URL = 'login'

ADMIN_SITE_HEADER = "RISHABH INSTA"

TIME_ZONE =  'Asia/Kolkata'


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'  # Replace with your email provider's SMTP server
EMAIL_PORT = 587  # Port for Gmail, might vary depending on your provider
EMAIL_USE_TLS = True
EMAIL_HOST_USER = '<@email>'  # Replace with your email
EMAIL_HOST_PASSWORD = '<pass>'  # Replace with your email password or an app-specific password
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER


# Cloud Image DataBase

# CLOUDINARY_STORAGE = {
#     'CLOUD_NAME': os.environ.get('IMG_CLOUD_NAME'),
#     'API_KEY': os.environ.get('IMG_API_KEY'),
#     'API_SECRET': os.environ.get('IMG_API_SECRET'),
# }

# # Cloudinary image upload format
# DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
