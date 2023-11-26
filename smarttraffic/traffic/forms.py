from django import forms
from .models import Device
from .models import VirtualDevice

class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['name', 'type', 'location']
        
        
class VirtualDeviceForm(forms.ModelForm):
    class Meta:
        model = VirtualDevice
        fields = ['name', 'type', 'metadata']