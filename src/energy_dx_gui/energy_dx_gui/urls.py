"""energy_dx_gui URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from django.shortcuts import redirect
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('login/', views.user_login, name='user_login'),
    path('login/houjin.html', lambda r: redirect('houjin', permanent=True)),
    path('controller/', views.controller, name='controller'),
    path('controlleredit/<pk>/', views.controlleredit, name='controlleredit'),
    path('devices/', views.devices, name='devices'),
    path('devicesedit/<pk>/', views.devicesedit, name='devicesedit'),
    path('houjin/', views.houjin, name='houjin'),
    path('houjin/<int:houjin_id>/buildings/', views.shisetsu, name='shisetsu'),
    path('houjin-search/', views.houjin_search_view, name='houjin_search'),
    path('building-name/', views.store_building_name, name='store-building-name'),
    path('store-device-id/', views.store_device_id, name='store_device_id'),
    path('get-class-names/<int:school_id>/', views.get_class_names, name='get_class_names'),
    path('get-building-names/', views.get_shisetsu_names, name='store-building-name'),
    path('get-building-names-by-houjin/<int:houjin_id>/', views.get_shisetsu_names, name='get_building_names_by_houjin'),
    path('get-all-building-names/', views.get_all_shisetsu_names, name='get-all-building-names'),
    path('get-houjin-names/', views.get_houjin_names, name='store-houjin-name'),
    
]
