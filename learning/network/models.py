from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Group(models.Model):

    users = models.ManyToManyField(User, related_name='group_memberships')

class Permission(models.Model):

    users = models.ManyToManyField(User, related_name='user_permissions')