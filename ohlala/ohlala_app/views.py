from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Servicio
# Create your views here.


def inicio(request):
    return render(request, 'ohlala_app/inicio.html', {})


def precios(request):
    return render(request, 'ohlala_app/precios.html', {})


def agendar(request):
    servicios = Servicio.objects.all()
    return render(request, 'ohlala_app/agendar.html', {'servicios': servicios})


def nosotros(request):
    return render(request, 'ohlala_app/nosotros.html', {})


def contacto(request):
    return render(request, 'ohlala_app/contacto.html', {})
