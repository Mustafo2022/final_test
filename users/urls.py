from django.urls import path
from .views import loginView, logoutView, forgotpassword, registration_view

urlpatterns = [
    path('login/forgot-password/', forgotpassword, name='forgot-password'),
    path('login/', loginView, name='login'),
    path('signup/', registration_view, name='signup'),
    path('logout/', logoutView, name='logout'),
]
