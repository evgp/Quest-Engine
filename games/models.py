from django.db import models
from django.contrib.auth.models import Group, User

# Create your models here.

class Game(models.Model):
    name = models.CharField(max_length=255)
    author = models.ManyToManyField(User)