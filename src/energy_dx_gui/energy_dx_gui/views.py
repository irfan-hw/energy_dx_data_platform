from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.db import connection
from .models import Houjin, Shisetsu
from .database import get_t_controller_data, get_t_controller_object, get_t_devices_data, get_t_devices_object

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('houjin.html') # replace with the name of your houjin.html template
        else:
            return render(request, 'index.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'index.html')
    
def controller(request):
    building_name = request.GET.get('building')
    controller = get_t_controller_data()
    context = {'controller': controller, 'building_name': building_name}
    return render(request, 'controller.html', context)  

def controlleredit(request, pk):
    if request.method == 'POST':
        server_accesstoken = request.POST['server_accesstoken']
        server_access_interval = request.POST['server_access_interval']
        status = request.POST['status']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE t_controller SET server_accesstoken=%s, server_access_interval=%s, status=%s WHERE controller_id=%s", [server_accesstoken, server_access_interval, status, pk])
            connection.commit()
        return redirect('controller')
    else:
        controlleredit = get_t_controller_object(pk=pk)
        context = {'controlleredit': controlleredit}
        return render(request, 'controlleredit.html', context)

def devices(request):
    devices = get_t_devices_data()
    context = {'devices': devices}
    return render(request, 'devices.html', context)  

def devicesedit(request, pk):
    if request.method == 'POST':
        device_id = request.POST['device_id']
        with connection.cursor() as cursor:
            cursor.execute("UPDATE t_devices SET device_id=%s WHERE device_id_temp=%s", [device_id, pk])
            connection.commit()
        return redirect('devices')
    else:
        controlleredit = get_t_devices_object(pk=pk)
        context = {'devicesedit': devicesedit}
        return render(request, 'devicesedit.html', context)

def houjin(request):        
    houjins = Houjin.objects.all()
    context = {'houjins': houjins}
    print(houjins)
    return render(request, 'houjin.html', context)  

def shisetsu(request, houjin_id):
    shisetsu_list = Shisetsu.objects.filter(houjin_id=houjin_id)
    buildings = [s.shisetsu_name for s in shisetsu_list]
    data = {'buildings': buildings}
    return JsonResponse(data)

def get_class_names(request, school_id):
    class_names = ClassName.objects.filter(school_id=school_id)
    class_name_data = [{'name': class_name.name} for class_name in class_names]
    return JsonResponse(class_name_data, safe=False)