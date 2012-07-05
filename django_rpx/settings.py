from django.conf import settings

__doc__ = """
Settings relevant to django_rpx
"""


import sys
from django.conf import settings

API_KEY=getattr(settings, 'RPX_API_KEY', None)
REST_DOMAIN=getattr(settings, 'RPX_REST_DOMAIN', None
TRUSTED_PROVIDERS(settings, 'RPX_TRUSTED_PROVIDERS', (
    'Google', 'Facebook', 'Yahoo!', 'AOL', 'Twitter',))
