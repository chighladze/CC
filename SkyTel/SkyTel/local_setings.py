import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-kxv6)xaq-(#76mkr4!d-%hf1i4cs3zim&xcf6d+**7eai_lh0h'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    # 'default': {},

    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'users_db.sqlite3',
    },

    'asterisk_db': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'asterisk',
        'USER': 'temouser',
        'PASSWORD': 'f5S4XFKALBwQ',
        'HOST': '188.227.192.34',
    },
}

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]