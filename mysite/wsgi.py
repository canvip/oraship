"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/howto/deployment/wsgi/
"""

import os
import site
import sys
site.addsitedir('C:/wsgi_app/env/Lib/site-packages/')

from django.core.wsgi import get_wsgi_application
path = 'C:/wsgi_app/mysite'
if path not in sys.path:
    sys.path.append(path)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
application = get_wsgi_application()
#Wrong!
#sys.path.append("/home/user/mysite/mysite")

#Correct
sys.path.append("C:/wsgi_app/mysite")
