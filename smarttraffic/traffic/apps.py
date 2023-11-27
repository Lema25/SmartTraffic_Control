from django.apps import AppConfig

class TrafficConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'traffic'

    def ready(self):
        from django.apps import apps
        from .models import create_content_and_permissions

        # Llamar a la función después de la migración
        create_content_and_permissions()
        
        ContentType = apps.get_model('contenttypes', 'ContentType')
        
        # Obtén o crea el contenido relacionado con el modelo Device y VirtualDevice
        device_content_type, _ = ContentType.objects.get_or_create(model='device', app_label='traffic')
        virtual_device_content_type, _ = ContentType.objects.get_or_create(model='virtualdevice', app_label='traffic')

        # Crea permisos para agregar dispositivos y dispositivos virtuales
        Permission = apps.get_model('auth', 'Permission')
        add_device_permission, _ = Permission.objects.get_or_create(
            codename='add_device',
            name='Can add device',
            content_type=device_content_type,
        )

        add_virtualdevice_permission, _ = Permission.objects.get_or_create(
            codename='add_virtualdevice',
            name='Can add virtual device',
            content_type=virtual_device_content_type,
        )