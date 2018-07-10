import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','WebPro.settings')

import django
django.setup()

from WebApp.models import Girl,Score
