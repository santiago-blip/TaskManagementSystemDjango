from .base import *

#sqlite
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': os.getenv("ENGINE_DB"),
        'NAME': os.getenv("NAME_DB"),                      
        'USER': os.getenv("USER_DATABASE"),
        'PASSWORD': os.getenv("PASSWORD_DATABASE"),
        'HOST': os.getenv("HOST_DB"),
        'PORT': os.getenv("PORT_DB"),
    }
}

ALLOWED_HOSTS = []