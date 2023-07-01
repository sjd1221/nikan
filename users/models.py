from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    Hospital = models.CharField(max_length=300, blank= True)
    Post = models.IntegerField(default=0)





# Create your models here.
