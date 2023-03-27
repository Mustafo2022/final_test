from django.db import models

from users.models import UserModel


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blogs(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='image_user')
    image = models.ImageField(upload_to='blogs')
    views = models.PositiveIntegerField(blank=True, null=True)
    category = models.ManyToManyField(Category, blank=True)
    likes = models.ManyToManyField(UserModel, blank=True)

    def total_likes(self):
        return self.likes.count()

    def __str__(self):
        return self.title
