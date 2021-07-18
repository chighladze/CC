import os
from pathlib import Path


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'drtngo-ineecure-kxv6)xaq-(#76fgr4!d-%hf1i4cklzim&xcf6d+**7eai_lh0h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["127.0.0.1", "198.18.18.109"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'cc',
        'USER': 'giorgi',
        'PASSWORD': '~!q1w2Giorgi~!',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
