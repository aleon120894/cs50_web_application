from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):

    username = models.CharField(max_length=32)
    password = models.PasswordField()

class Auction(models.Model):

    date = models.DateField(max_length=32)
    status = models.BooleanField()
    lot = models.CharField(max_length=64)
