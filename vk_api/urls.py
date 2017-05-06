# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url
from vk_api.views import VkAuthView


urlpatterns = patterns('',
    url(r'^auth/$', VkAuthView.as_view(), name='vk_auth'),
)
