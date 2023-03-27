from django.contrib.auth.models import AbstractUser
from django.db import models


class ResetPassword(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.email} | {self.password}'


class UserModel(AbstractUser):
    bio = models.TextField()
    age = models.PositiveIntegerField(blank=True, null=True)
    friends = models.ManyToManyField('UserModel', blank=True)
