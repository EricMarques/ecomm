from .settings import *
import dj_database_url

DEBUG = False

DATABASES = {
    'default': dj_database_url.config()
}

STATIC_URL = '/static/'
if DEBUG:
   STATICFILES_DIRS = [
   os.path.join(BASE_DIR, 'static'),
   ]
else:
   STATIC_ROOT = os.path.join(BASE_DIR,'static')

MIDDLEWARE.append('whitenoise.middleware.WhiteNoiseMiddleware')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
