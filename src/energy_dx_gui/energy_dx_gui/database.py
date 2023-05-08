from django.db import connection

def get_t_controller_data(shisetsu_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM t_controller WHERE shisetsu_id = %s", [shisetsu_id])
        rows = cursor.fetchall()
    return rows

def get_t_devices_data(device_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM t_devices WHERE controller_id=%s", [device_id])
        rows = cursor.fetchall()
    return rows

def get_t_controller_object(pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT server_accesstoken, server_access_interval, status FROM t_controller WHERE controller_id=%s", [pk])
        rows = cursor.fetchone()
    return rows

def get_t_devices_object(pk):
    with connection.cursor() as cursor:
        cursor.execute("SELECT device_id FROM t_devices WHERE device_id_temp=%s", [pk])
        rows = cursor.fetchone()
    return rows