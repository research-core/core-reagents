"""
WSGI config for reagents_db project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/howto/deployment/wsgi/
"""

import os, sys; sys.path.append('/var/www/reagents_db')
os.environ["DJANGO_SETTINGS_MODULE"]="reagents_db.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()