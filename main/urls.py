from django.urls import path
from .views import HomeView, AboutView, ContactView, verify, Add10, Add20, Add50, Add70, Add100

urlpatterns = [
    path('', HomeView, name='home'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView, name='about'),
    path('verify/', verify, name='verify'),
    path('popularity/10', Add10, name='add-10'),
    path('popularity/20', Add20, name='add-20'),
    path('popularity/50', Add50, name='add-50'),
    path('popularity/70', Add70, name='add-70'),
    path('popularity/100', Add100, name='add-100'),
]