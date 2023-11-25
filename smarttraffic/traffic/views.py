# traffic/views.py
from django.shortcuts import render, redirect
from .models import Device, VirtualDevice, Permissions, TrafficData
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm

def index(request):
    devices = Device.objects.all()
    virtual_devices = VirtualDevice.objects.all()
    permissions = Permissions.objects.all()
    traffic_data = TrafficData.objects.all()

    context = {
        'devices': devices,
        'virtual_devices': virtual_devices,
        'permissions': permissions,
        'traffic_data': traffic_data,
    }

    return render(request, 'traffic/index.html', context)

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'traffic/device_list.html', {'devices': devices})

def virtual_device_list(request):
    virtual_devices = VirtualDevice.objects.all()
    return render(request, 'traffic/virtual_device_list.html', {'virtual_devices': virtual_devices})

def permissions_list(request):
    permissions = Permissions.objects.all()
    return render(request, 'traffic/permissions_list.html', {'permissions': permissions})

def traffic_data_list(request):
    traffic_data_list = TrafficData.objects.all()
    print(traffic_data_list)
    return render(request, 'traffic/traffic_data_list.html', {'traffic_data_list': traffic_data_list})

def my_protected_view(request):
    # Tu lógica de vista aquí
    return render(request, 'my_protected_template.html')

def login_view(request):
    if request.method == 'POST':
        # Recuperar el nombre de usuario y la contraseña del formulario de inicio de sesión
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Autenticar al usuario
        user = authenticate(request, username=username, password=password)

        # Verificar si la autenticación fue exitosa
        if user is not None:
            # Iniciar sesión para el usuario autenticado
            login(request, user)
            # Redirigir a una página después del inicio de sesión (puedes cambiar esto)
            return redirect('index')
        else:
            # Si la autenticación falla, puedes mostrar un mensaje de error
            error_message = "Nombre de usuario o contraseña incorrectos."
            return render(request, 'login.html', {'error_message': error_message})

    # Si no es una solicitud POST, simplemente renderizar la página de inicio de sesión
    return render(request, 'login.html')

def signup_view(request):
    if request.method == 'POST':
        # Obtener los datos del formulario de registro
        form = UserCreationForm(request.POST)

        # Verificar si el formulario es válido
        if form.is_valid():
            # Crear la cuenta de usuario
            user = form.save()

            # Iniciar sesión para el nuevo usuario
            login(request, user)

            # Redirigir a una página después del registro (puedes cambiar esto)
            return redirect('index')
    else:
        # Si no es una solicitud POST, simplemente renderizar el formulario de registro
        form = UserCreationForm()

    return render(request, 'signup.html', {'form': form})