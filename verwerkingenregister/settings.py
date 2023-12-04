# verwerkingenregister/settings.py

from dotenv import load_dotenv

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

load_dotenv( BASE_DIR / '.env', )

SECRET_KEY = os.getenv('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITE_ID = 1

# Application definition
INSTALLED_APPS = [
  'django.contrib.admin',
  'django.contrib.auth',
  'django.contrib.contenttypes',
  'django.contrib.sessions',
  'django.contrib.messages',
  'django.contrib.staticfiles',
  'django.contrib.sites',
  'django.contrib.sitemaps',
  # apps
  'site_basis.apps.SiteBasisConfig',
  'users.apps.UsersConfig',
  'rechten.apps.RechtenConfig',
  'verwerkingen.apps.VerwerkingenConfig',
  'algoritmes.apps.AlgoritmesConfig',
  'waarmerken.apps.WaarmerkenConfig',
  'bronnen.apps.BronnenConfig',
  'geoworkflow.apps.GeoworkflowConfig',
  'budgetten.apps.BudgettenConfig',
  'reserveren.apps.ReserverenConfig',
  'contacts.apps.ContactsConfig',
  # support packages
  'django_extensions',
  'easyaudit',
  'crispy_forms',
  'crispy_bootstrap5',
  'formtools',
  'import_export',
]

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK          = 'bootstrap5'

MIDDLEWARE = [
  'django.middleware.security.SecurityMiddleware',
  'django.contrib.sessions.middleware.SessionMiddleware',
  'django.middleware.common.CommonMiddleware',
  'django.middleware.csrf.CsrfViewMiddleware',
  'django.contrib.auth.middleware.AuthenticationMiddleware',
  'django.contrib.messages.middleware.MessageMiddleware',
  'django.middleware.clickjacking.XFrameOptionsMiddleware',
  'easyaudit.middleware.easyaudit.EasyAuditMiddleware',
]

ROOT_URLCONF = 'verwerkingenregister.urls'

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

WSGI_APPLICATION = 'verwerkingenregister.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.sqlite3',
    'NAME': BASE_DIR / 'db.sqlite3',
  }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
  {
    'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
  },
  {
    'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
  },
]

# django-easy-audit settings
DJANGO_EASY_AUDIT_WATCH_MODEL_EVENTS   = True  # log model events 
DJANGO_EASY_AUDIT_WATCH_AUTH_EVENTS    = True  # log authentication events
DJANGO_EASY_AUDIT_WATCH_REQUEST_EVENTS = False # log request events
# ignored models
DJANGO_EASY_AUDIT_UNREGISTERED_CLASSES_EXTRA = [
  'geoworkflow.Notitie'
  ]

# Django system logging 
FORMATTERS = (
  {
    "verbose": {
      "format": "{levelname} {asctime:s} {threadName} {thread:d} {module} {filename} {lineno:d} {name} {funcName} {process:d} {message}",
      "style": "{",
    },
    "simple": {
      "format": "{levelname} {asctime:s} {module} {filename} {lineno:d} {funcName} {message}",
      "style": "{",
    },
  },
)
HANDLERS = {
  "console_handler": {
    "class": "logging.StreamHandler",
    "formatter": "simple",
  },
  "my_handler": {
    "class"      : "logging.handlers.RotatingFileHandler",
    "filename"   : f"{BASE_DIR}/logs/blogthedata.log",
    "mode"       : "a",
    "encoding"   : "utf-8",
    "formatter"  : "simple",
    "backupCount": 5,
    "maxBytes"   : 1024 * 1024 * 5,  # 5 MB
  },
  "my_handler_detailed": {
    "class"      : "logging.handlers.RotatingFileHandler",
    "filename"   : f"{BASE_DIR}/logs/blogthedata_detailed.log",
    "mode"       : "a",
    "formatter"  : "verbose",
    "backupCount": 5,
    "maxBytes"   : 1024 * 1024 * 5,  # 5 MB
  },
}
LOGGERS = (
    {
        "django": {
            "handlers": ["console_handler", "my_handler_detailed"],
            "level": "INFO",
            "propagate": False,
        },
        "django.request": {
            "handlers": ["my_handler"],
            "level": "WARNING",
            "propagate": False,
        },
    },
)
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": FORMATTERS[0],
    "handlers": HANDLERS,
    "loggers": LOGGERS[0],
}

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Europe/Amsterdam'
USE_I18N  = True
USE_TZ    = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATICFILES_DIRS = [
  os.path.join(BASE_DIR, 'static'),
  os.path.join(BASE_DIR, 'media')
]

STATIC_ROOT = BASE_DIR / "staticfiles" # The absolute filesystem path to the directory where collectstatic will collect static files for deployment.
STATIC_URL  = "/static/"               # URL to use when referring to static files located in STATIC_ROOT.

MEDIA_ROOT = BASE_DIR / "mediafiles"   # The absolute filesystem path to the directory that will hold user-stored files.
MEDIA_URL  = "/media/"                 # URL that handles the media served from MEDIA_ROOT, used for managing stored files.

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
