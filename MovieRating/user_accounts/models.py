from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models

class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    age = models.IntegerField(null=True, blank=True)
    groups = models.ManyToManyField(Group, blank=True, related_name='custom_users')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='custom_users')

    def __str__(self):
        return self.username
