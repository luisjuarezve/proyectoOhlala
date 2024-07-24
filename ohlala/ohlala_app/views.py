from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from ohlala_app.models import Servicio, Manicurista
# Create your views here.


def login_required_custom(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if 'id_cliente' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return _wrapped_view_func


def inicio(request):
    if 'id_cliente' not in request.session:
        return render(request, 'ohlala_app/inicio.html', {'sesion': 'inactivo'})
    servicios = Servicio.objects.all()
    return render(request, 'ohlala_app/inicio.html', {'sesion': 'activo'})


def servicios(request):
    if 'id_cliente' not in request.session:
        return render(request, 'ohlala_app/servicios.html', {'sesion': 'inactivo'})
    servicios = Servicio.objects.all()
    return render(request, 'ohlala_app/servicios.html', {'sesion': 'activo'})


def agendar(request):
    if 'id_cliente' not in request.session:
        return redirect('login')
    servicios = Servicio.objects.all()
    manicuristas = Manicurista.objects.all()
    return render(request, 'ohlala_app/agendar.html', {'servicios': servicios, 'manicuristas': manicuristas, 'sesion': 'activo'})


def nosotros(request):
    if 'id_cliente' not in request.session:
        return render(request, 'ohlala_app/nosotros.html', {'sesion': 'inactivo'})
    servicios = Servicio.objects.all()
    return render(request, 'ohlala_app/nosotros.html', {'sesion': 'activo'})


def contacto(request):
    if 'id_cliente' not in request.session:
        return render(request, 'ohlala_app/contacto.html', {'sesion': 'inactivo'})
    servicios = Servicio.objects.all()
    return render(request, 'ohlala_app/contacto.html', {'sesion': 'activo'})
