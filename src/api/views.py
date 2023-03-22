import json, traceback
from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from datetime import datetime,timedelta
from energy_dx_data_platform.logger import Logger

from .models import TController,TDataGet,TDataSet,TDeviceDido,TDeviceEnl,TDevices
from .serializer import TControllerSerializer,TDataGetSerializer,TDataSetSerializer,TDeviceDidoSerializer,TDeviceEnlSerializer,TDevicesSerializer

# Create your views here.
logger = Logger(__name__)

class TControllerViewSet(viewsets.ModelViewSet):
    serializer_class = TControllerSerializer
    http_method_names = ['get']

    def get_queryset(self):
        self.queryset = TController.objects.all()

        _controller_id = self.request.query_params.get('controller_id', None)

        if _controller_id is None:
            logger.info('Get Controller | Query parameter not complete 400')
            raise ValidationError(detail='Query parameter not complete', code=400)

        try:
            self.queryset = TController.objects.filter( 
                controller_id=_controller_id
            )
            logger.info('Get Controller | Controller '+_controller_id+' data returned 201')
            return self.queryset
        except:
            logger.error(traceback.format_exc())
            return Response(data='Get Controller | Error occured', status=status.HTTP_400_BAD_REQUEST)

class TDataGetViewSet(viewsets.ModelViewSet):
    serializer_class = TDataGetSerializer
    http_method_names = ['put']

    def put(self, request, *args, **kwargs):

        data = json.loads(request.body)

        if("device_id" in data and "get_cd" in data and "datetime_start" in data and "datetime_end" in data and 
            "value" in data and "server_sync" in data):

            try:
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
                    logger.info('TDataGet | '+  data["device_id"] +' data updated 201')
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
                    logger.info('TDataGet | '+  data["device_id"] +' data created 201')
                    return Response(data='Data Created', status=status.HTTP_201_CREATED)
            except:
                logger.error(traceback.format_exc())
                return Response(data='Error occured', status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.info('TDataGet | Data format invalid 400')
            return Response(data='Data format invalid', status=status.HTTP_400_BAD_REQUEST)

class TDataSetViewSet(viewsets.ModelViewSet):
    serializer_class = TDataSetSerializer
    http_method_names = ['get', 'put']

    def get_queryset(self):
        self.queryset = TDataSet.objects.all()

        _device_id = self.request.query_params.get('device_id', None)

        if _device_id is None:
            logger.info('TDataSet | Query parameter not complete 400')
            raise ValidationError(detail='Query parameter not complete', code=400)

        try:
            self.queryset = TDataSet.objects.filter( 
                device_id=_device_id, 
                datetime__gte = datetime.now(), 
                datetime__lte = datetime.now() + timedelta(hours=24)
            )
            logger.info('TDataSet | '+_device_id+' data returned 201')
            return self.queryset
        except:
            logger.error(traceback.format_exc())
            return Response(data='Error occured', status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)

        if("device_id" in data and "set_cd" in data and "datetime" in data and "plan_no" in data and 
            "value" in data and "device_sync" in data):
            try:
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
                    logger.info('TDataSet | '+  data["device_id"] +' data updated 201')
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
                    logger.info('TDataSet | '+  data["device_id"] +' data created 201')
                    return Response(data='Data Created', status=status.HTTP_201_CREATED)
            except:
                logger.error(traceback.format_exc())
                return Response(data='Error occured', status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.info('TDataSet | Data format invalid 400')
            return Response(data='Data format invalid', status=status.HTTP_400_BAD_REQUEST)

class TDeviceDidoViewSet(viewsets.ModelViewSet):
    queryset = TDeviceDido.objects.all()
    serializer_class = TDeviceDidoSerializer

class TDeviceEnlViewSet(viewsets.ModelViewSet):
    queryset = TDeviceEnl.objects.all()
    serializer_class = TDeviceEnlSerializer

class TDevicesViewSet(viewsets.ModelViewSet):
    serializer_class = TDevicesSerializer
    http_method_names = ['put']
    def put(self, request, *args, **kwargs):
        data = json.loads(request.body)

        if("id" in data and "device_type" in data and
            "protocol" in data and "access_get_interval" in data and "access_set_interval" in data and
            "status" in data and "active" in data and "server_sync" in data and "added" in data):

            try:
                query = TDevices.objects.filter(
                    device_id_temp = data["id"],
                )
                if query:
                    query.update(
                        device_id_temp = data["id"],
                        device_id = data["device_id"] if "device_id" in data else None,
                        device_type = data["device_type"],
                        device_info = data["device_info"] if "device_info" in data else None,
                        calc_info = data["calc_info"] if "calc_info" in data else None,
                        address_ipv6 = data["address_IPv6"]  if "address_IPv6" in data else None,
                        address_ipv4 = data["address_IPv4"]  if "address_IPv4" in data else None,
                        protocol = data["protocol"],
                        access_get_interval = data["access_get_interval"],
                        access_set_interval = data["access_set_interval"],
                        last_access_get = data["last_access_get"] if "last_access_get" in data else None,
                        last_access_set = data["last_access_set"] if "last_access_set" in data else None,
                        next_access_get = data["next_access_get"] if "next_access_get" in data else None,
                        next_access_set = data["next_access_set"] if "next_access_set" in data else None,
                        status = data["status"],
                        active = data["active"],
                        server_sync = data["server_sync"],
                        last_server_sync = data["last_server_sync"] if "last_server_sync" in data else None,
                        added = data["added"],
                        deleted = data["deleted"] if "deleted" in data else None
                    )
                    logger.info('Set Device | '+data["id"]+' data updated 201')
                    return Response(data='Data Updated', status=status.HTTP_201_CREATED)
                else:
                    query.create(
                        device_id_temp = data["id"],
                        device_id = data["device_id"] if "device_id" in data else None,
                        device_type = data["device_type"],
                        device_info = data["device_info"] if "device_info" in data else None,
                        calc_info = data["calc_info"] if "calc_info" in data else None,
                        address_ipv6 = data["address_IPv6"]  if "address_IPv6" in data else None,
                        address_ipv4 = data["address_IPv4"]  if "address_IPv4" in data else None,
                        protocol = data["protocol"],
                        access_get_interval = data["access_get_interval"],
                        access_set_interval = data["access_set_interval"],
                        last_access_get = data["last_access_get"] if "last_access_get" in data else None,
                        last_access_set = data["last_access_set"] if "last_access_set" in data else None,
                        next_access_get = data["next_access_get"] if "next_access_get" in data else None,
                        next_access_set = data["next_access_set"] if "next_access_set" in data else None,
                        status = data["status"],
                        active = data["active"],
                        server_sync = data["server_sync"],
                        last_server_sync = data["last_server_sync"] if "last_server_sync" in data else None,
                        added = data["added"],
                        deleted = data["deleted"] if "deleted" in data else None
                    )
                    logger.info('Set Device | '+data["id"]+' data created 201')
                    return Response(data='Data Created', status=status.HTTP_201_CREATED)
            except:
                logger.error(traceback.format_exc())
                return Response(data='Error occured', status=status.HTTP_400_BAD_REQUEST)
        else:
            logger.error('Set Device | Put Device Data format invalid 400')
            return Response(data='Data format invalid', status=status.HTTP_400_BAD_REQUEST)