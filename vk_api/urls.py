# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from vk_api.views import VkAuthView, VkAPIStatusUpdateView

urlpatterns = patterns('',
    url(r'^auth/$', VkAuthView.as_view(), name='vk_auth'),
    url(r'^status/update$', VkAPIStatusUpdateView.as_view(), name='vk_status_update'),
)
