from django.http import HttpResponseRedirect, HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.views.decorators.cache import never_cache

from django_rpx import settings, logger

def rpx_response(request):
    """
    process the login token
    """
    logger.debug('django_rpx.views.rpx_response processing')
    token = request.POST.get('token', None)
    if not token: 
        logger.debug('no token provided, forbidden')
        return HttpResponseForbidden()
    logger.debug('authenticating')
    user=authenticate(token=token)
    logger.debug('authenticaton complete, user is %s' %(user,))
    if user and user.is_active:
        login(request, user)
        # TODO make it 302 and put in a cache buster
        return HttpResponseRedirect('/?login')
    else:
        return HttpResponseForbidden()

    
    
@login_required
def rpx_unmap(request):
    """
    unmaps an identifier from an existing user
    """
    # first get the identifier
    if request.method.lower() == 'post':
        identifier = request.POST.get('identifier', '')
        api = MappingApi()
        if api.request_unmap(request.user, identifier):
            return HttpResponseRedirect('/')
    return HttpResponseForbidden()
        
@never_cache
def rpx_logout(request):
    """
    logout
    """
    logout(request)
    return HttpResponseRedirect('/?logout')
