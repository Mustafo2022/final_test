from django.urls import path
from .views import Report

urlpatterns = [
    path('report/', Report, name='report'),
]