import os
import sys
import django.core.handlers.wsgi
from django.conf import settings

# Add this file path to sys.path in order to import settings
sys.path.insert(0, os.path.join(os.path.dirname(os.path.realpath(__file__)), '..'))

os.environ['DJANGO_SETTINGS_MODULE'] = 'smartcloud.settings'

sys.stdout = sys.stderr

#STACK_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))

#sys.path.append(STACK_PATH)

DEBUG = True

application = django.core.handlers.wsgi.WSGIHandler()
