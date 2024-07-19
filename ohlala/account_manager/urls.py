from django.urls import path, include
from account_manager import views

urlpatterns = [
    path('register/', views.form_signup, name='form_signup'),
    path('auth/', views.form_login, name='form_login'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
]
