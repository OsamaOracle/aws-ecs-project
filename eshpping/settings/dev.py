from .base import *

# non existing DB name
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'product',
        'USER': 'postgres',
        'PASSWORD': 'test123',
        'HOST': '127.0.0.1'
    }
}
