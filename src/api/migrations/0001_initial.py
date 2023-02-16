# Generated by Django 3.2.16 on 2023-01-25 04:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TController',
            fields=[
                ('controller_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('server_uri', models.CharField(max_length=32)),
                ('server_accesstoken', models.CharField(max_length=32)),
                ('server_access_interval', models.IntegerField()),
                ('last_server_access', models.DateTimeField()),
                ('next_server_access', models.DateTimeField()),
                ('status', models.IntegerField()),
                ('active', models.IntegerField()),
                ('last_server_sync', models.DateTimeField(blank=True, null=True)),
                ('version', models.CharField(max_length=32)),
                ('last_updated', models.DateTimeField()),
            ],
            options={
                'db_table': 't_controller',
            },
        ),
        migrations.CreateModel(
            name='TDataGet',
            fields=[
                ('device_id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('get_cd', models.SmallIntegerField()),
                ('datetime_start', models.DateTimeField()),
                ('datetime_end', models.DateTimeField()),
                ('value', models.BinaryField(max_length=16)),
                ('server_sync', models.IntegerField()),
            ],
            options={
                'db_table': 't_data_get',
                'unique_together': {('device_id', 'get_cd', 'datetime_start')},
            },
        ),
        migrations.CreateModel(
            name='TDevices',
            fields=[
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.tdataget')),
                ('device_type', models.SmallIntegerField()),
                ('device_info', models.TextField(blank=True, null=True)),
                ('address_ipv6', models.CharField(db_column='address_IPv6', max_length=16)),
                ('address_ipv4', models.CharField(db_column='address_IPv4', max_length=16)),
                ('protocol', models.CharField(max_length=2)),
                ('access_get_interval', models.IntegerField()),
                ('access_set_interval', models.IntegerField()),
                ('last_access_get', models.DateTimeField()),
                ('last_access_set', models.DateTimeField()),
                ('next_access_get', models.DateTimeField()),
                ('next_access_set', models.DateTimeField()),
                ('status', models.SmallIntegerField()),
                ('active', models.IntegerField()),
                ('server_sync', models.SmallIntegerField()),
                ('last_server_sync', models.DateTimeField(blank=True, null=True)),
                ('added', models.DateTimeField()),
                ('deleted', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 't_devices',
            },
        ),
        migrations.CreateModel(
            name='TDeviceEnl',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('sys_device_type', models.SmallIntegerField()),
                ('sys_get_or_set', models.IntegerField()),
                ('sys_get_or_set_cd', models.SmallIntegerField()),
                ('ecl_classgroup_cd', models.CharField(max_length=1)),
                ('ecl_class_cd', models.CharField(max_length=1)),
                ('ecl_epc', models.SmallIntegerField(db_column='ecl_EPC')),
            ],
            options={
                'db_table': 't_device_ENL',
                'unique_together': {('sys_device_type', 'sys_get_or_set_cd')},
            },
        ),
        migrations.CreateModel(
            name='TDeviceDido',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=128)),
                ('sys_device_type', models.SmallIntegerField()),
                ('sys_di_or_do', models.IntegerField()),
                ('sys_di_or_do_cd', models.SmallIntegerField()),
            ],
            options={
                'db_table': 't_device_DIDO',
                'unique_together': {('sys_device_type', 'sys_di_or_do_cd')},
            },
        ),
        migrations.CreateModel(
            name='TDataSet',
            fields=[
                ('device', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='api.tdevices')),
                ('set_cd', models.SmallIntegerField()),
                ('datetime', models.DateTimeField()),
                ('plan_no', models.IntegerField()),
                ('value', models.BinaryField(max_length=16)),
                ('device_sync', models.IntegerField()),
            ],
            options={
                'db_table': 't_data_set',
                'unique_together': {('device_id', 'set_cd', 'datetime', 'plan_no')},
            },
        ),
    ]
