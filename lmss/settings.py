import os
from datetime import timedelta
from pathlib import Path

from dotenv import dotenv_values

config = dotenv_values(".env")

BASE_DIR = Path(__file__).resolve().parent.parent


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


JWT_AUTH = {
    "JWT_AUTH_HEADER_PREFIX": "JWT",
}


INSTALLED_APPS = [
    # 'slik',
    
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
    "Create_Test",
    "ExamResponse",
    'django_admin_listfilter_dropdown',
    'gamification',
    'rest_framework_simplejwt.token_blacklist',
    "silk",
]


MIDDLEWARE = [
    'silk.middleware.SilkyMiddleware',
    "apitally.django_rest_framework.ApitallyMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware", 
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

APITALLY_MIDDLEWARE = {
    "client_id": "ce0b80e9-3c41-43a3-b032-012b989acb2f",
    "env": "prod",  # or "dev"
}

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

WSGI_APPLICATION = "lmss.wsgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": config["DB_NAME"],
        "USER": config["DB_USER"],
        "PASSWORD": config["DB_PASSWORD"],
        "HOST":config["DB_HOST"],
        "PORT":config["DB_PORT"],
        'CONN_MAX_AGE':None,
        'CONN_HEALTH_CHECKS':True
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

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATIC_URL = "staticfiles/"
STATIC_ROOT = "/var/www/static/"
MEDIA_ROOT = "/var/www/media/"
MEDIA_URL = "media/"


# Email setting
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = "noreply.studystreak@gmail.com"
EMAIL_HOST_PASSWORD = "sypowsabvnbqjhrv"
EMAIL_USE_TLS = True


JAZZMIN_SETTINGS = {
    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"model": "auth.User"},
        {"model": "students.Student"},
        {"model": "Courses.Course"},
        {"model": "coursedetail.Lesson"},
        {"app": "books"},
    ],
}

INTERNAL_IPS = [
    "127.0.0.1",
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
    "DEFAULT_FILTER_BACKENDS": ["django_filters.rest_framework.DjangoFilterBackend"]
}

SPECTACULAR_SETTINGS = {
    "TITLE": "Study Streak API",
    # 'DESCRIPTION': 'Your project description',
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
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

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=1),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=2),
}

ACCOUNT_LOGIN_REDIRECT_URL = "home"
ACCOUNT_LOGOUT_REDIRECT_URL = "account_login"


KEY_ID = "rzp_test_QyWQWfJeARzOZG"
KEY_SECRET = "CbjpLbEoily2YroYWMuvNfxG"

CSRF_TRUSTED_ORIGINS = [
    "https://studystreak.in",
    "http://studystreak.in",
]

RAZORPAY_KEY_ID = config['RAZORPAY_KEY_ID']
RAZORPAY_KEY_SECRET = config['RAZORPAY_KEY_SECRET']

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


ALLOWED_STUDENTS_SESSIONS = 2
CKEDITOR_UPLOAD_PATH = "uploads/"

