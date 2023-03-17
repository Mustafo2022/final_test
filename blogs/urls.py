from django.urls import path
from .views import PostsDetail, delete

urlpatterns = [
    path('detail/<int:pk>', PostsDetail.as_view(), name="detail"),
    path('delete/<int:pk>', delete, name="delete"),
]