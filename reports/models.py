from django.db import models
from users.models import UserModel


class ReportModel(models.Model):
    username = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'"{self.title}" BY {self.username}'

    class Meta:
        verbose_name = 'Report'
        verbose_name_plural = 'Reports'
