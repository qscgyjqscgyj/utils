from django.db import models

from vk_api.managers import VkAuthTokenManager


class VkAuthToken(models.Model):
    user_id = models.CharField(max_length=255)
    token = models.CharField(max_length=255)

    objects = VkAuthTokenManager()

    def __str__(self):
        return self.token

    def __unicode__(self):
        return self.token
