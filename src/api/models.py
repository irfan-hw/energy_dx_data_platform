# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TController(models.Model):
    controller_id = models.CharField(primary_key=True, max_length=32)
    server_uri = models.CharField(max_length=32)
    server_accesstoken = models.CharField(max_length=32)
    server_access_interval = models.IntegerField()
    last_server_access = models.DateTimeField(blank=True, null=True)
    next_server_access = models.DateTimeField(blank=True, null=True)
    status = models.IntegerField()
    active = models.IntegerField()
    last_server_sync = models.DateTimeField(blank=True, null=True)
    version = models.CharField(max_length=32)
    last_updated = models.DateTimeField()

    class Meta:
        db_table = 't_controller'


class TDataGet(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=32)
    get_cd = models.SmallIntegerField()
    datetime_start = models.DateTimeField()
    datetime_end = models.DateTimeField()
    value = models.CharField(max_length=254)
    server_sync = models.IntegerField()

    class Meta:
        db_table = 't_data_get'
        unique_together = (('device_id', 'get_cd', 'datetime_start'),)


class TDataSet(models.Model):
    id = models.AutoField(primary_key=True)
    device_id = models.CharField(max_length=32)
    set_cd = models.SmallIntegerField()
    datetime = models.DateTimeField()
    plan_no = models.IntegerField()
    value = models.CharField(max_length=254)
    device_sync = models.IntegerField()

    class Meta:
        db_table = 't_data_set'
        unique_together = (('device_id', 'set_cd', 'datetime', 'plan_no'),)


class TDeviceDido(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    sys_device_type = models.SmallIntegerField()
    sys_di_or_do = models.IntegerField()
    sys_di_or_do_cd = models.SmallIntegerField()

    class Meta:
        db_table = 't_device_DIDO'
        unique_together = (('sys_device_type', 'sys_di_or_do_cd'),)


class TDeviceEnl(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=128)
    sys_device_type = models.SmallIntegerField()
    sys_get_or_set = models.IntegerField()
    sys_get_or_set_cd = models.SmallIntegerField()
    ecl_classgroup_cd = models.CharField(max_length=1)
    ecl_class_cd = models.CharField(max_length=1)
    ecl_epc = models.SmallIntegerField(db_column='ecl_EPC')  # Field name made lowercase.

    class Meta:
        db_table = 't_device_ENL'
        unique_together = (('sys_device_type', 'sys_get_or_set_cd'),)


class TDevices(models.Model):
    device_id_temp = models.CharField(max_length=32, primary_key=True)
    device_id = models.CharField(max_length=32,blank=True)
    device_type = models.SmallIntegerField()
    device_info = models.TextField(blank=True)
    calc_info = models.CharField(max_length=64,blank=True)
    address_ipv6 = models.CharField(db_column='address_IPv6', max_length=16,blank=True)  # Field name made lowercase.
    address_ipv4 = models.CharField(db_column='address_IPv4', max_length=16,blank=True)  # Field name made lowercase.
    protocol = models.CharField(max_length=2)
    access_get_interval = models.IntegerField()
    access_set_interval = models.IntegerField()
    last_access_get = models.DateTimeField(blank=True, null=True)
    last_access_set = models.DateTimeField(blank=True, null=True)
    next_access_get = models.DateTimeField(blank=True, null=True)
    next_access_set = models.DateTimeField(blank=True, null=True)
    status = models.SmallIntegerField()
    active = models.IntegerField()
    server_sync = models.SmallIntegerField()
    last_server_sync = models.DateTimeField(blank=True, null=True)
    added = models.DateTimeField(blank=True, null=True)
    deleted = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = 't_devices'
