from django.urls import path

from .views import PostsDetail, delete, BlogCreate, PostLike, BlogListView, GalleryLike, GalleryDelete

urlpatterns = [
    path('like/<int:pk>/', PostLike, name='like'),
    path('li/<int:pk>/', GalleryDelete, name='gallery-delete'),
    path('ike/<int:pk>/', GalleryLike, name='gallery-like'),
    path('create/', BlogCreate, name="post-create"),
    path('gallery/', BlogListView.as_view(), name="gallery"),
    path('detail/<int:pk>', PostsDetail.as_view(), name="detail"),
    path('delete/<int:pk>', delete, name="delete"),
]
