from django.shortcuts import render
import django_filters
from rest_framework import viewsets, filters

from .models import TController,TDataGet,TDataSet,TDeviceDido,TDeviceEnl,TDevices
from .serializer import TControllerSerializer,TDataGetSerializer,TDataSetSerializer,TDeviceDidoSerializer,TDeviceEnlSerializer,TDevicesSerializer

# Create your views here.

class TControllerViewSet(viewsets.ModelViewSet):
    queryset = TController.objects.all()
    serializer_class = TControllerSerializer

class TDataGetViewSet(viewsets.ModelViewSet):
    queryset = TDataGet.objects.all()
    serializer_class = TDataGetSerializer

class TDataSetViewSet(viewsets.ModelViewSet):
    queryset = TDataSet.objects.all()
    serializer_class = TDataSetSerializer

class TDeviceDidoViewSet(viewsets.ModelViewSet):
    queryset = TDeviceDido.objects.all()
    serializer_class = TDeviceDidoSerializer

class TDeviceEnlViewSet(viewsets.ModelViewSet):
    queryset = TDeviceEnl.objects.all()
    serializer_class = TDeviceEnlSerializer

class TDevicesViewSet(viewsets.ModelViewSet):
    queryset = TDevices.objects.all()
    serializer_class = TDevicesSerializer