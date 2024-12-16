"""
Django settings for hexa_core project.

Generated by 'django-admin startproject' using Django 5.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
from datetime import timedelta # access token 위해 필요
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-cx9junbjgw2)(&^y=72%=f1)m@s#9n9^d-z74zii*0u&sqnk1o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost', '172.29.182.105', '172.30.1.165'] # CORS 문제 해결하기 위해서 넣어줘야 함 IP 설정

AUTH_USER_MODEL = 'auths.User'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'auths.apps.AuthsConfig',
    'dashboard.apps.DashboardConfig',
    'rest_framework',               # Django REST Framework
    'rest_framework_simplejwt',     # JWT Authentication
]

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [ # 모든 뷰에 기본으로 적용할 권한을 설정
	    'rest_framework.permissions.IsAuthenticated' # 인증된 요청에 한해서 뷰 호출 허용(로그인이 되어있어야만 접근 허용)
	  ],
	  'DEFAULT_AUTHENTICATION_CLASSES': [ # 인증 방식을 정의
		  # 클라이언트가 요청을 보낼 때 JWT Access Token을 헤더에 포함해야 해당 리소스에 접근 가능
	    'rest_framework_simplejwt.authentication.JWTAuthentication'
	  ]
}

# 추가적인 JWT_AUTH 설정
SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5), # 액세스 토큰 유효 기간=5분
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1), # 리프레시 토큰 유효 기간=1일
    "ROTATE_REFRESH_TOKENS": False,
    "BLACKLIST_AFTER_ROTATION": False,
    "UPDATE_LAST_LOGIN": False,

    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": "",
    "AUDIENCE": None,
    "ISSUER": None,
    "JSON_ENCODER": None,
    "JWK_URL": None,
    "LEEWAY": 0,

    "AUTH_HEADER_TYPES": ("Bearer",), # 인증 헤더 타입을 설정/여기서는 "Bearer" 타입 사용(요청 헤더에 Authorization: Bearer <token> 형식으로 토큰을 보내야 함)
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",

    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
    "SLIDING_TOKEN_LIFETIME": timedelta(minutes=5),
    "SLIDING_TOKEN_REFRESH_LIFETIME": timedelta(days=1),

    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}


MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # CORS 문제 해결하기 위해서 넣어줘야 함
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'hexa_core.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'hexa_core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # MariaDB는 MySQL과 호환됩니다.
        'NAME': 'healthcare',                   # 데이터베이스 이름
        'USER': 'root',                         # 사용자 이름
        'PASSWORD': 'admin',                    # 비밀번호
        'HOST': '172.29.182.105',               # MariaDB 서버의 IP 주소
        'PORT': '3306',                         # MariaDB의 포트
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # MariaDB는 MySQL과 호환됩니다.
#         'NAME': os.environ.get('DB_NAME', 'healthcare'),
#         'USER': os.environ.get('DB_USER', 'root'),
#         'PASSWORD': os.environ.get('DB_PASSWORD', 'admin'),
#         'HOST': os.environ.get('DB_HOST', '172.29.182.105'),  # DB의 서비스 이름과 일치
#         'PORT': os.environ.get('DB_PORT', '3306'),
#     }
# }


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

AUTH_USER_MODEL='auths.User'

CORS_ALLOW_CREDENTIALS = True  # 인증 정보 허용 (withCredentials)
CORS_ALLOWED_ORIGINS = [
    # 'http://localhost:5173', 
    # 'http://127.0.0.1:5173', 
    # 'http://172.29.182.105:3000', 
    # 'http://172.30.1.165:3000', 
    'http://172.30.1.165:5173', 
    'http://172.29.182.105:5173'
] # CORS 문제 해결하기 위해서 넣어줘야 함 IP 설정
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:5173",  # Svelte 앱 주소
]