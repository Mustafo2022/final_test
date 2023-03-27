from django.urls import path
from .views import HomeView, AboutView, ContactView, verify

urlpatterns = [
    path('', HomeView, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView, name='about'),
    path('verify/', verify, name='verify'),
]