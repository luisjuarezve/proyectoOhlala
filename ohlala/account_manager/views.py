from django.contrib.auth.hashers import check_password, make_password
from django.db import transaction
from django.shortcuts import render, redirect
from account_manager.models import Cuenta, Cliente
from django.http import HttpResponse
from ohlala_app.models import Servicio
# Create your views here.


def form_signup(request):
    if request.method == 'POST':
        cedula = request.POST.get('cedula')
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        fecha_nacimiento = request.POST.get('fecha_nacimiento')
        correo_electronico = request.POST.get('correo_electronico')
        contrasena = request.POST.get('contrasena')
        if Cliente.objects.filter(cedula=cedula).exists() or Cuenta.objects.filter(correo_electronico=correo_electronico).exists():
            return HttpResponse('La cédula o el correo electrónico ya están registrados en el sistema. Por favor, verifica los datos e intenta nuevamente.')
        else:
            try:
                with transaction.atomic():
                    cliente = Cliente(cedula=cedula, nombre=nombre, apellido=apellido,
                                      telefono=telefono, fecha_nacimiento=fecha_nacimiento)
                    cliente.save()
                    cuenta = Cuenta(idCliente=cliente, correo_electronico=correo_electronico,
                                    contrasena=contrasena)
                    cuenta.save()
                    return redirect('login')
            except Exception as e:
                print(f"Error: {e}")
                return HttpResponse('Ocurrió un error durante el registro. Por favor, intenta nuevamente.')


def form_login(request):
    if request.method == 'POST':
        correo_electronico = request.POST.get('correo_electronico')
        contrasena = request.POST.get('contrasena')
        try:
            cuenta = Cuenta.objects.get(
                correo_electronico=correo_electronico, contrasena=contrasena)
            request.session['id_cliente'] = cuenta.idCliente_id
            request.session.save()
            return redirect('agendar')
        except Cuenta.DoesNotExist:
            return redirect('login')
    else:
        return redirect('login')


def form_logout(request):
    if request.method == 'POST':
        del request.session['id_cliente']
        return redirect('login')  # Redirect to the login page
    else:
        return redirect('login')


def signup(request):
    return render(request, 'account_manager/signup.html')


def login(request):
    return render(request, 'account_manager/login.html')
