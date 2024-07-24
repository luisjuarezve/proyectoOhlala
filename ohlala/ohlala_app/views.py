from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from ohlala_app.models import Servicio, Manicurista, Cita
from account_manager.models import Cliente
from datetime import time
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


def registro_cita(request):
    if request.method == 'POST':
        fechaCita = request.POST.get('fecha')
        horaCita = time(int(request.POST.get('hora')))
        idCliente = int(request.session.get('id_cliente'))
        idManicurista = int(request.POST.get('manicurista'))
        idManicura = int(request.POST.get('manicura'))
        idPedicura = int(request.POST.get('pedicura'))
        try:
            if idManicura != 0 and idPedicura != 0:
                cliente = Cliente.objects.get(pk=idCliente)
                manicurista = Manicurista.objects.get(pk=idManicurista)
                servicioManicura = Servicio.objects.get(pk=idManicura)
                servicioPedicura = Servicio.objects.get(pk=idPedicura)
                cita_manicura = Cita(fechaCita=fechaCita, horaCita=horaCita,
                                     idCliente=cliente, idManicurista=manicurista, idServicio=servicioManicura)
                cita_manicura.save()
                cita_pedicura = Cita(fechaCita=fechaCita, horaCita=horaCita,
                                     idCliente=cliente, idManicurista=manicurista, idServicio=servicioPedicura)
                cita_pedicura.save()
                return redirect('agendar')
            elif idManicura != 0:
                cliente = Cliente.objects.get(pk=idCliente)
                manicurista = Manicurista.objects.get(pk=idManicurista)
                servicioManicura = Servicio.objects.get(pk=idManicura)
                cita_manicura = Cita(fechaCita=fechaCita, horaCita=horaCita,
                                     idCliente=cliente, idManicurista=manicurista, idServicio=servicioManicura)
                cita_manicura.save()
                return redirect('agendar')
            elif idPedicura != 0:
                cliente = Cliente.objects.get(pk=idCliente)
                manicurista = Manicurista.objects.get(pk=idManicurista)
                servicioPedicura = Servicio.objects.get(pk=idPedicura)
                cita_pedicura = Cita(fechaCita=fechaCita, horaCita=horaCita,
                                     idCliente=cliente, idManicurista=manicurista, idServicio=servicioPedicura)
                cita_pedicura.save()
                return redirect('agendar')
            else:
                return HttpResponse("Debes seleccionar por lo menos un servicio", status=400)
        except Exception as e:
            print(f"Error al registrar la cita: {str(e)}")
            return redirect('agendar')
    else:
        return redirect('login')
