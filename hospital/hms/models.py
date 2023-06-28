from django.db import models
from django.contrib.auth.models import User, AbstractUser


class Category(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class UserProfile(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=64, null=True)
    last_name = models.CharField(max_length=64, null=True)
    email = models.EmailField(max_length=64, null=True)
    password = models.CharField(max_length=72)
    specialization = models.CharField(max_length=64, null=True)
    institute = models.CharField(max_length=128, null=True)
    gender = models.CharField(max_length=16, null=True)
    address = models.TextField(null=True)







