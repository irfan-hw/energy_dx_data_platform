import json
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from datetime import datetime,timedelta

from .models import TController,TDataGet,TDataSet,TDeviceDido,TDeviceEnl,TDevices
from .serializer import TControllerSerializer,TDataGetSerializer,TDataSetSerializer,TDeviceDidoSerializer,TDeviceEnlSerializer,TDevicesSerializer

# Create your views here.

class TControllerViewSet(viewsets.ModelViewSet):
    queryset = TController.objects.all()
    serializer_class = TControllerSerializer

class TDataGetViewSet(viewsets.ModelViewSet):
    serializer_class = TDataGetSerializer
    http_method_names = ['put']

    def put(self, request, *args, **kwargs):

        data = json.loads(request.body)

        if("device_id" in data and "get_cd" in data and "datetime_start" in data and "datetime_end" in data and 
            "value" in data and "server_sync" in data):

            query = TDataGet.objects.filter(
                device_id = data["device_id"],
                get_cd = data["get_cd"],
                datetime_start = data["datetime_start"],
            )
            if query:
                query.update(
                    device_id = data["device_id"],
                    get_cd = data["get_cd"],
                    datetime_start = data["datetime_start"],
                    datetime_end = data["datetime_end"],
                    value = data["value"],
                    server_sync = data["server_sync"]
                )
                return Response(data='Data Updated', status=status.HTTP_201_CREATED)
            else:
                query.create(
                    device_id = data["device_id"],
                    get_cd = data["get_cd"],
                    datetime_start = data["datetime_start"],
                    datetime_end = data["datetime_end"],
                    value = data["value"],
                    server_sync = data["server_sync"]
                )
                return Response(data='Data Created', status=status.HTTP_201_CREATED)
        else:
            return Response(data='Data format invalid', status=status.HTTP_400_BAD_REQUEST)

class TDataSetViewSet(viewsets.ModelViewSet):
    serializer_class = TDataSetSerializer
    http_method_names = ['get', 'put']

    def get_queryset(self):
        self.queryset = TDataSet.objects.all()

        _device_id = self.request.query_params.get('device_id', None)
        # _set_cd = self.request.query_params.get('set_cd', None)
        # _datetime = self.request.query_params.get('datetime', None)
        # _plan_no = self.request.query_params.get('plan_no', None)

        if _device_id is None:
            raise ValidationError(detail='Query parameter not complete', code=400)

        self.queryset = TDataSet.objects.filter( 
            device_id=_device_id, 
            datetime__gte = datetime.now(), 
            datetime__lte = datetime.now() + timedelta(hours=24)
        )
        return self.queryset
    
    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)

        if("device_id" in data and "set_cd" in data and "datetime" in data and "plan_no" in data and 
            "value" in data and "device_sync" in data):

            query = TDataSet.objects.filter(
                device_id = data["device_id"],
                set_cd = data["set_cd"],
                datetime = data["datetime"],
                plan_no = data["plan_no"],
            )
            if query:
                query.update(
                    device_id = data["device_id"],
                    set_cd = data["set_cd"],
                    datetime = data["datetime"],
                    plan_no = data["plan_no"],
                    value = data["value"],
                    device_sync = data["device_sync"]
                )
                return Response(data='Data Updated', status=status.HTTP_201_CREATED)
            else:
                query.create(
                    device_id = data["device_id"],
                    set_cd = data["set_cd"],
                    datetime = data["datetime"],
                    plan_no = data["plan_no"],
                    value = data["value"],
                    device_sync = data["device_sync"]
                )
                return Response(data='Data Created', status=status.HTTP_201_CREATED)
        else:
            return Response(data='Data format invalid', status=status.HTTP_400_BAD_REQUEST)

class TDeviceDidoViewSet(viewsets.ModelViewSet):
    queryset = TDeviceDido.objects.all()
    serializer_class = TDeviceDidoSerializer

class TDeviceEnlViewSet(viewsets.ModelViewSet):
    queryset = TDeviceEnl.objects.all()
    serializer_class = TDeviceEnlSerializer

class TDevicesViewSet(viewsets.ModelViewSet):
    queryset = TDevices.objects.all()
    serializer_class = TDevicesSerializer