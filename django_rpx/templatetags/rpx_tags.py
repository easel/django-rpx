from django import template
from django.template import Context, loader
from django.template.loader import render_to_string
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site

from django_rpx import logger, settings
"""
rpx_tags" is a slightly redundant name, but if i clall this module simple
rpx" it only allows me to use the first tag found (although all tags appear
in the libary)

TODO:
  * provide for language choice
  * document
  * provide for customisation for the "overlay" attribute, whatever it is.

"""

register = template.Library()

@register.inclusion_tag('django_rpx/rpx_link.html', takes_context=True)
def rpx_link(context, text):
    current_site=Site.objects.get_current()
    return {
      'text': text,
      'realm': settings.REALM,
      # TODO: make this cleaner, ideally use whatever the user was requesting
        # the site as 
      'token_url': "http://%s%s" % (settings.REST_DOMAIN,
        reverse('django_rpx.views.rpx_response'))
    }

@register.inclusion_tag('django_rpx/rpx_script.html')
def rpx_script():
    current_site=Site.objects.get_current()

    return {
      'realm': settings.REALM,
      'token_url': "http://%s%s" % (settings.REST_DOMAIN,
        reverse('django_rpx.views.rpx_response'))
    }

@register.inclusion_tag('django_rpx/rpx_static_link.html', takes_context=True)
def rpx_maplink(context, text):
    current_site=Site.objects.get_current()

    return {
      'text': text,
      'realm': settings.REALM,
      'token_url': "http://%s%s" % (settings.REST_DOMAIN,
        reverse('django_rpx.views.rpx_map'))
    }

@register.inclusion_tag('django_rpx/rpx_logout_link.html')
def rpx_logout_link(text):
    return {
        'text': text,
        'logout_url': "http://%s%s" % (settings.REST_DOMAIN,
            reverse('django_rpx.views.rpx_logout'))
    }

