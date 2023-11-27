from django.contrib.auth.models import Group, Permission, User
from django.contrib.contenttypes.models import ContentType
from .models import Device, VirtualDevice, TrafficData

def assign_permissions():
    # Obtener los contenidos relacionados con los modelos
    
    user, created = User.objects.get_or_create(
        username='aespinos@unal.edu.co',
        email='aespinos@unal.edu.co',
    )
    
    if created:
        # Configurar la contraseña solo si el usuario es creado
        user.set_password('diseño123')
        user.save()

    device_content_type = ContentType.objects.get_for_model(Device)
    virtual_device_content_type = ContentType.objects.get_for_model(VirtualDevice)
    traffic_data_content_type = ContentType.objects.get_for_model(TrafficData)

    # Crear grupos si no existen
    user_group, created = Group.objects.get_or_create(name='Usuarios')
    admin_group, created = Group.objects.get_or_create(name='Administradores')

    # Asignar permisos para usuarios regulares
    user_group.permissions.add(
        Permission.objects.get(
            content_type=device_content_type,
            codename='view_device'
        ),
        Permission.objects.get(
            content_type=virtual_device_content_type,
            codename='view_virtualdevice'
        ),
        Permission.objects.get(
            content_type=traffic_data_content_type,
            codename='view_trafficdata'
        ),
    )

    # Asignar permisos para administradores
    admin_group.permissions.add(
        Permission.objects.get(
            content_type=device_content_type,
            codename='add_device'
        ),
        Permission.objects.get(
            content_type=virtual_device_content_type,
            codename='add_virtualdevice'
        ),
        Permission.objects.get(
            content_type=traffic_data_content_type,
            codename='add_trafficdata'
        ),
    )