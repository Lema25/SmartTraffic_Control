from django.shortcuts import render, redirect
from .models import Device, VirtualDevice, Permissions, TrafficData, Device
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from .forms import DeviceForm, VirtualDeviceForm
from django.contrib.auth.models import User 
from django.db.models import Q

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

    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('device_list')
    else:
        form = DeviceForm()

    return render(request, 'traffic/device_list.html', {'devices': devices, 'form': form})

def virtual_device_list(request):
    virtual_devices = VirtualDevice.objects.all()

    if request.method == 'POST':
        form = VirtualDeviceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('virtual_device_list')
    else:
        form = VirtualDeviceForm()

    return render(request, 'traffic/virtual_device_list.html', {'virtual_devices': virtual_devices, 'form': form})

def permissions_list(request):
    users = User.objects.all()  # Obtén todos los usuarios
    return render(request, 'traffic/permissions_list.html', {'users': users})

def traffic_data_list(request):
    # Manejar la lógica de búsqueda
    search_device = request.GET.get('search_device')
    device_type = request.GET.get('device_type')
    lista=[]

    if search_device and device_type:
        # Utilizar Q para manejar la búsqueda en la tabla correspondiente
        if device_type == 'normal':
            query="SELECT * FROM traffic_device WHERE name LIKE '%"+search_device+"%'"
            for dispositivos in Device.objects.raw(query):
                lista.append(dispositivos)
        elif device_type == 'virtual':
            query="SELECT * FROM traffic_virtualdevice WHERE name LIKE '%"+search_device+"%'"
            for dispositivos in VirtualDevice.objects.raw(query):
                lista.append(dispositivos)
    #print("SQL Query:", str(traffic_data_list.query))
    
    # Renderizar la página con los resultados filtrados
    #print("traffic_data_list:", traffic_data_list)
    return render(request, 'traffic/traffic_data_list.html', {'traffic_data_list': lista})

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