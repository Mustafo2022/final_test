from django.db import models


class UserModel(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    points = models.PositiveIntegerField()
    popularity = models.PositiveIntegerField()
    email_verified = models.BooleanField(default=False)
    friends = models.ManyToManyField('UserModel', blank=True)

    def __str__(self):
        return f'{self.first_name} | {self.last_name} | {self.age}'

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
