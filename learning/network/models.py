from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):

    # Define your custom fields here

    class Meta:
        # Define metadata, if any
        pass

    # Add unique related_name arguments for groups and user_permissions
    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        related_name='network_users_groups',  # Unique related_name for groups
        related_query_name='user',
    )

    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('user permissions'),
        blank=True,
        related_name='network_users_permissions',  # Unique related_name for user_permissions
        related_query_name='user',
    )


class Post(models.Model):

    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
