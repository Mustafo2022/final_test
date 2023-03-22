from django.urls import path
from .views import HomeView, AboutView, ContactView, VerifyEmail

urlpatterns = [
    path('', HomeView, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView, name='about'),
    path('verify-email/', VerifyEmail, name='verify-email'),
]