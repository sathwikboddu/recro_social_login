from django.db import models

from social_django.models import AbstractUserSocialAuth, DjangoStorage, USER_MODEL


class CustomUserSocialAuth(AbstractUserSocialAuth):
    user = models.ForeignKey(USER_MODEL, related_name='custom_social_auth',
                             on_delete=models.CASCADE)


class CustomDjangoStorage(DjangoStorage):
    user = CustomUserSocialAuth
# Create your models here.
# class Users(models.Model):
#     id = models.CharField(max_length=100)
#     name = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)

#     def __str__(self):
#         return '{} {}'.format(self.first_name, self.last_name)