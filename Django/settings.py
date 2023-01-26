# Do apps with link in left_panel
# Add forms for instances
# Good luck! :)


from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-22=8%3d0hjwqm)jh-t7@9!+ss92dx)43*2i4+g@v-s58=vn(lw'

DEPLOY = False

DEBUG = not DEPLOY

WSGI_APPLICATION = 'Django.wsgi.application'

ROOT_URLCONF = 'Django.urls'

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

ALLOWED_HOSTS = ['localhost']

SAVE_VISITS = DEPLOY

MAX_ROWS = 30

STATIC_URL = '/static/'

STATIC_ROOT = 'static/'

CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CSRF_TRUSTED_ORIGINS = [
    'http://localhost:3000',
]
CORS_ALLOWED_ORIGIN_REGEXES = [
    'http://localhost:3000',
]
CORS_ORIGIN_WHITELIST = (
'http://localhost:3000',
)

INSTALLED_APPS = [
    'corsheaders',
    'colorfield',
    'admin_interface',
    'Main.apps.MainConfig',
    'Pages.apps.PagesConfig',
    'Panel.apps.PanelConfig',
    'django.contrib.auth',
    'Account.apps.AccountConfig',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'Account.middleware.VisitMiddleware',
    'Panel.middleware.IsSuperUserMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]
