from django.db import models

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