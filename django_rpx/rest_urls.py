from django.conf.urls.defaults import *
from django_rpx import views

urlpatterns = patterns('',
                           url(r'^rpx_response/',  views.rpx_response,
                               name='rpx-response'), 
                           url(r'^rpx_logout/',  views.rpx_logout,
                               name='rpx-logout'), 
                           url(r'^rpx_unmap/',  views.rpx_unmap,
                               name='rpx-unmap'), 
                      )

