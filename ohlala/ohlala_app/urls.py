from django.urls import path, include
from ohlala_app import views
urlpatterns = [
    path('', views.inicio, name='inicio'),
]
