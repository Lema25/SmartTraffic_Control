from django.db.models.signals import post_migrate
from django.dispatch import receiver
from django.contrib.auth.models import User, Permission, Group
from django.contrib.contenttypes.models import ContentType
from .models import Device, VirtualDevice
from .permissions import assign_permissions

@receiver(post_migrate)
def on_post_migrate(sender, **kwargs):

    pass
