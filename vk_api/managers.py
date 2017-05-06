from django.db import models


class VkAuthTokenManager(models.Manager):
    def token(self, user_id):
        return self.filter(user_id=user_id).order_by('-pk')[0]
