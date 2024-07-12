from django.urls import path, include
from ohlala_app import views
from django.conf.urls import handler404

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('precios', views.precios, name='precios'),
    path('agendar', views.agendar, name='agendar'),
    path('nosotros', views.nosotros, name='nosotros'),
    path('contacto', views.contacto, name='contacto'),
]

handler404 = 'ohlala_app.views.not_found'
