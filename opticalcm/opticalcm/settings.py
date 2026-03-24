from pathlib import Path
import os

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent


# =========================
# 🔐 SEGURIDAD
# =========================

SECRET_KEY = os.environ.get('SECRET_KEY', 'unsafe-secret-key-change-this')

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
    'serviciosopticoslcm-web.onrender.com',
    'www.serviciosopticoslcm.cl',
    'serviciosopticoslcm.cl',
    'sistema.serviciosopticoslcm.cl',
]


# =========================
# 📦 APLICACIONES
# =========================

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]


# =========================
# ⚙️ MIDDLEWARE
# =========================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# =========================
# 🌐 URLS Y WSGI
# =========================

ROOT_URLCONF = 'opticalcm.urls'

WSGI_APPLICATION = 'opticalcm.wsgi.application'


# =========================
# 🎨 TEMPLATES
# =========================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'opticalcm' / 'templates',
        ],
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


# =========================
# 🗄 BASE DE DATOS
# =========================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# =========================
# 🔑 VALIDACIÓN PASSWORDS
# =========================

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


# =========================
# 🌍 INTERNACIONALIZACIÓN
# =========================

LANGUAGE_CODE = 'es-cl'

TIME_ZONE = 'America/Santiago'

USE_I18N = True

USE_TZ = True


# =========================
# 📁 ARCHIVOS ESTÁTICOS
# =========================

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'opticalcm/static'),
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedStaticFilesStorage'


# =========================
# 🔧 CONFIGURACIÓN ADICIONAL PRODUCCIÓN
# =========================

SECURE_BROWSER_XSS_FILTER = True
SECURE_CONTENT_TYPE_NOSNIFF = True
X_FRAME_OPTIONS = 'DENY'


# =========================
# 🆔 DEFAULT ID
# =========================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
