from rest_framework import serializers
from .models import TController,TDataGet,TDataSet,TDeviceDido,TDeviceEnl,TDevices

class TControllerSerializer(serializers.ModelSerializer):
    class Meta:
        model = TController
        fields = ('controller_id', 'server_uri','server_accesstoken','server_access_interval','last_server_access',
        'next_server_access','status','active','last_server_sync','version','last_updated')


class TDataGetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDataGet
        fields = ('device_id', 'get_cd', 'datetime_start', 'datetime_end', 'value', 'server_sync')

class TDataSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDataSet
        fields = ('device_id', 'set_cd', 'datetime', 'plan_no', 'value', 'device_sync')
        
class TDevicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDevices
        fields = ('device_id_temp','device_id', 'device_type', 'device_info','calc_info', 'address_IPv6', 'address_IPv4', 'protocol',
        'access_get_interval', 'access_set_interval', 'last_access_get', 'last_access_set','next_access_get',
        'next_access_set', 'status', 'active', 'server_sync', 'last_server_sync', 'added', 'deleted')

class TDeviceDidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDeviceDido
        fields = ('id', 'name', 'sys_device_type', 'sys_di_or_do', 'sys_di_or_do_cd')

class TDeviceEnlSerializer(serializers.ModelSerializer):
    class Meta:
        model = TDeviceEnl
        fields = ('id', 'name', 'sys_device_type', 'sys_get_or_set', 'sys_get_or_set_cd', 'ecl_classgroup_cd',
        'ecl_class_cd', 'ecl_EPC')