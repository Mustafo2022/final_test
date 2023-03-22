from django.contrib.auth.models import AbstractUser
from django.db import models


class ResetPassword(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=7)

    def __str__(self):
        return f'{self.email} | {self.password}'


class UserModel(AbstractUser):
    img = models.ImageField(upload_to='users/', blank=False)
    bio = models.TextField()
    age = models.PositiveIntegerField(blank=True, null=True)
    points = models.PositiveIntegerField(default=100)
    popularity = models.PositiveIntegerField(default=10)
    email_verified = models.BooleanField(default=False)
    friends = models.ManyToManyField('UserModel', blank=True)
