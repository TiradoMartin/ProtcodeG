"""
WSGI config for protcode project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
#import heroku
from whitenoise.django import DjangoWhiteNoise
#from dj_static import Cling

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "protcode.settings")

application = get_wsgi_application()
#linea heroku
#application = Cling(get_wsgi_application())

application = DjangoWhiteNoise(application)