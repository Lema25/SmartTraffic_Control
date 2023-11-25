# traffic/urls.py
from django.urls import path
from .views import index, device_list, virtual_device_list, permissions_list, traffic_data_list, login_view, signup_view  # Asegúrate de incluir 'login_view'
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('', index, name='index'),
    path('devices/', device_list, name='device_list'),
    path('virtual-devices/', virtual_device_list, name='virtual_device_list'),
    path('permissions/', permissions_list, name='permissions_list'),
    path('traffic-data/', traffic_data_list, name='traffic_data_list'),
    path('login/', LoginView.as_view(), name='login'),  # Agrega esta línea
    path('signup/', signup_view, name='signup'),
    
]
