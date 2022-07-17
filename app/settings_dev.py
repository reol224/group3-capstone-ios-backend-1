import os
from app.settings import *
from corsheaders.defaults import default_headers

# Disable debugging and logging
DEBUG = True
LOGGING = {}
LOCAL_STATIC = True

# Allow cross-site in Development
# https://pypi.org/project/django-cors-headers/
# corsheader
# CORS_ALLOW_ALL_ORIGINS = True
# CORS_ALLOW_CREDENTIALS = True
# CORS_ALLOW_HEADERS = list(default_headers) + [
#     'referrer-policy',
#     'type',
# ]

# cors
INSTALLED_APPS.append('corsheaders')
MIDDLEWARE.insert(2, 'corsheaders.middleware.CorsMiddleware') # place to correct position which is no.3
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = list(default_headers) + [
    'referrer-policy',
    'type',
]

GEO_DATA_DIR = os.path.join(DATA_DIR, "geo")
