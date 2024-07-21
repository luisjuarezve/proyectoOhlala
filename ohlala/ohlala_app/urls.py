from django.urls import path, include
from ohlala_app import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('servicios', views.servicios, name='servicios'),
    path('agendar', views.agendar, name='agendar'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
]
