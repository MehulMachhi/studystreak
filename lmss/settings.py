import os
from datetime import timedelta
from pathlib import Path

from dotenv import dotenv_values

config = dotenv_values(".env")

BASE_DIR = Path(__file__).resolve().parent.parent


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-o#zup200eb=2f@80#j$+6wu!2x9ts-6xczkgcd%aerj2*8kh!="

DEBUG = True


ALLOWED_HOSTS = [
    "65.20.73.247",
    "localhost",
    "127.0.0.1",
    "studystreak.io",
    "studystreak.in",
    "65.20.89.184",
]
# ALLOWED_HOSTS = ["*"]
# settings.py

ZOOM_API_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzA1NDg5NTE5LCJpYXQiOjE3MDU0ODkyMTksImp0aSI6IjQ3MjY3NDE3MWViMjRkZGNiMTM2OGRjMTU5M2RhZTdkIiwidXNlcl9pZCI6Mn0.Gq4SNpGYNqI-nrU6G8iP902vX9SOnFIGjF_z66pzRe4"

JWT_AUTH = {
    # Authorization:Token xxx
    "JWT_AUTH_HEADER_PREFIX": "JWT",
}


INSTALLED_APPS = [
    # "debug_toolbar",
    "jazzmin",
    "master",
    "Courses",
    "package",
    "students",
    "assessment",
    "coursedetail",
    "import_export",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "rest_framework.authtoken",
    "ckeditor",
    "website",
    "nested_admin",
    "QuestionBank",
    "Listening_Exam",
    "Reading_Exam",
    "Writing_Exam",
    "Speaking_Exam",
    "corsheaders",
    "exam",
    "ckeditor_uploader",
    "drf_spectacular",
    "django_filters",
    "payment",
    "LiveClass",
    "allauth",
    "allauth.account",
    "allauth.socialaccount",
    "allauth.socialaccount.providers.google",
    "Create_Test",
    "ExamResponse",
    'django_admin_listfilter_dropdown',
    'gamification',
    # "dj_rest_auth",
    #  'rest_framework.authtoken',
    # "dj_rest_auth.registration",
]
CKEDITOR_UPLOAD_PATH = "uploads/"
MIDDLEWARE = [
    # "debug_toolbar.middleware.DebugToolbarMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",
]

ROOT_URLCONF = "lmss.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                # "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "APP": {
            "client_id": "1041538556743-t4ql9a9p8r6eb9407j96lup5m3tckb01.apps.googleusercontent.com",
            "secret": "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",
            "key": "",  # leave empty
        },
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "VERIFIED_EMAIL": True,
    },
}


WSGI_APPLICATION = "lmss.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config["DB_NAME"], # "lmss",
        "USER": config["DB_USER"],
        "PASSWORD": config["DB_PASSWORD"],  # os.environ.get("DB_PASSWORD"),
        "HOST":config["DB_HOST"],
        "PORT":config["DB_PORT"],
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


LANGUAGE_CODE = "en-us"

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


STATIC_URL = "staticfiles/"


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_ROOT = "/var/www/static/"
MEDIA_ROOT = "/var/www/media/"
MEDIA_URL = "media/"
PASSWORD_RESET_TIMEOUT = 3600


# Email setting
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply.studystreak@gmail.com"
EMAIL_HOST_PASSWORD = "sypowsabvnbqjhrv"
EMAIL_USE_TLS = True
# REQUIRE_AUTHENTICATION = True

# gmail password: oecindia@123
REST_FRAMEWORK = {
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"]
}


JAZZMIN_SETTINGS = {
    "topmenu_links": [
        # Url that gets reversed (Permissions can be added)
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        # external url that opens in a new window (Permissions can be added)
        # {
        #     "name": "Support",
        #     "url": "https://github.com/farridav/django-jazzmin/issues",
        #     "new_window": True,
        # },
        # model admin to link to (Permissions checked against model)
        {"model": "auth.User"},
        {"model": "students.Student"},
        {"model": "Courses.Course"},
        {"model": "coursedetail.Lesson"},
        # App with dropdown menu to all its models pages (Permissions checked against models)
        {"app": "books"},
    ],
}

INTERNAL_IPS = [
    # ...
    "127.0.0.1",
    # ...
]




APPEND_SLASH = True


CKEDITOR_CONFIGS = {
    "default": {
        "toolbar": "full",
        "extraPlugins": ",".join(
            [
                "devtools",
                "menubutton",
                "table",
                "tableresize",
                "tabletools",
            ]
        ),
    },
}

SESSION_COOKIE_SAMESITE = "Strict"
SESSION_COOKIE_HTTPONLY = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ORIGIN_ALLOW_ALL = True
CSRF_USE_SESSIONS = True
CSRF_COOKIE_SAMESITE = None
CORS_ALLOW_ALL_ORIGINS = True

DATA_UPLOAD_MAX_MEMORY_SIZE = 5242880

REST_FRAMEWORK = {
    "TEST_REQUEST_DEFAULT_FORMAT": "json",
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Study Streak API",
    # 'DESCRIPTION': 'Your project description',
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
    # OTHER SETTINGS
}

PASSWORD_RESET_TIMEOUT = 60 * 30

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework_simplejwt.authentication.JWTAuthentication",
    ],
    'DEFAULT_PERMISSION_CLASSES':[
      "rest_framework.permissions.IsAuthenticated",  
    ]
}
AUTHENTICATION_BACKENDS = [
    "allauth.account.auth_backends.AuthenticationBackend",
]

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(days=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
}

ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"
# {"web":
#     {"client_id":"246152471027-8ql9ui19kphk2t0hp2pd57lb7bd1op3v.apps.googleusercontent.com",
#      "project_id":"fresh-ocean-412305",
#      "auth_uri":"https://accounts.google.com/o/oauth2/auth",
#      "token_uri":"https://oauth2.googleapis.com/token",
#      "auth_provider_x509_cert_url":"https://www.googleapis.com/oauth2/v1/certs",
#      "client_secret":"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",
#      "redirect_uris":["http://127.0.0.1:8000/accounts/google/login/callback/",
#                       "http://localhost:8000/accounts/google/login/callback/"],
#      "javascript_origins":["http://127.0.0.1:8000","http://localhost:8000"]}
#     }
SOCIALACCOUNT_PROVIDERS = {
    "google": {
        "SCOPE": [
            "profile",
            "email",
        ],
        "AUTH_PARAMS": {
            "access_type": "online",
        },
        "OAUTH_PKCE_ENABLED": True,
    }
}

KEY_ID = "rzp_test_QyWQWfJeARzOZG"
KEY_SECRET = "CbjpLbEoily2YroYWMuvNfxG"

CSRF_TRUSTED_ORIGINS = [
    "https://studystreak.in",
    "http://studystreak.in",
]


RAZORPAY_KEY_ID = config['RAZORPAY_KEY_ID']
RAZORPAY_KEY_SECRET = config['RAZORPAY_KEY_SECRET']


# TOKEN_URL = "https://zoom.us/oauth/token"
# BASE_URL = 'https://zoom.us'
# ACCOUNT_ID = "hy5Qo6Z-T8-HWmI2vHf4og"
# CLIENT_ID = "qjhZVzGQpq3dMgNyPLdZw"
# CLIENT_SECRET = "y4kvGXl0fp64zuSJCQ5dd9ZBNjGlaj8H"

BASE_URL = 'https://zoom.us'
TOKEN_URL = "https://zoom.us/oauth/token"
ACCOUNT_ID = "4h9jZgnETeC1jeCttAqewA"
CLIENT_ID = "uWxvDYmLRBGf6uW2HUWgA"
CLIENT_SECRET = "B8Xg5H6UJbjppdTptwa2IOjn6mQaFsBs"
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": config['REDIS_URL'],
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
    }
}

GOOGLE_CLIENT_ID = config['GOOGLE_CLIENT_ID']
GOOGLE_CLIENT_SECRET = config['GOOGLE_CLIENT_SECRET']