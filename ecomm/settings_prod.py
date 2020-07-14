from .settings import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_ROOT = "app-root/repo/wsgi/static"

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('assets', 'app-root/repo/wsgi/openshift/static'),

    )

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
