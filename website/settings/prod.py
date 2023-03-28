from .base import *


DEBUG = False

ALLOWED_HOSTS = ['85.204.27.163']


STATICFILES_DIRS = []

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')