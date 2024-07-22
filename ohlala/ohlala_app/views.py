from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Servicio
# Create your views here.


def login_required_custom(view_func):
    def _wrapped_view_func(request, *args, **kwargs):
        if 'perfil_id' in request.session:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('login')
    return _wrapped_view_func


def inicio(request):
    return render(request, 'ohlala_app/inicio.html', {})


def servicios(request):
    return render(request, 'ohlala_app/servicios.html', {})


@login_required_custom
def agendar(request):
    if 'cuenta_id' not in request.session:
        servicios = Servicio.objects.all()
        return render(request, 'ohlala_app/agendar.html', {'servicios': servicios})
    return redirect('login')


def nosotros(request):
    return render(request, 'ohlala_app/nosotros.html', {})


def contacto(request):
    return render(request, 'ohlala_app/contacto.html', {})
