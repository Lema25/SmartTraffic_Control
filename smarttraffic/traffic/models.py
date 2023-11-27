from django.db import models
from django.apps import apps
from django.db.models.signals import post_migrate
from django.dispatch import receiver

class Device(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    virtual_device = models.OneToOneField('VirtualDevice', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class VirtualDevice(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    metadata = models.TextField()

class Permissions(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=100)
    relationship = models.ManyToManyField('self', blank=True)

class TrafficData(models.Model):
    device = models.ForeignKey(Device, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    vehicle_count = models.IntegerField()
    average_speed = models.FloatField()

    def __str__(self):
        return f"{self.device.name} - {self.timestamp}"

# Método para obtener o crear el contenido relacionado con el modelo Device y VirtualDevice
def create_content_and_permissions(**kwargs):
    ContentType = apps.get_model('contenttypes', 'ContentType')
    device_content_type, _ = ContentType.objects.get_or_create(model='device', app_label='traffic')
    virtual_device_content_type, _ = ContentType.objects.get_or_create(model='virtualdevice', app_label='traffic')

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

# Señal post_migrate para llamar al método después de que las migraciones se hayan aplicado
@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):
    create_content_and_permissions()
