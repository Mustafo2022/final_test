from django.contrib import admin
from .models import UserModel, ResetPassword

admin.site.register(UserModel)
admin.site.register(ResetPassword)
