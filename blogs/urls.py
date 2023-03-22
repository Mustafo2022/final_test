from django.urls import path
from .views import PostsDetail, delete, CreatePost

urlpatterns = [
    path('create/', CreatePost.as_view(), name="post-create"),
    path('detail/<int:pk>', PostsDetail.as_view(), name="detail"),
    path('delete/<int:pk>', delete, name="delete"),
]