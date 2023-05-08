from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse
from django.db import connection
from django.contrib.auth.decorators import login_required
from django.core import serializers
from .models import Houjin, Shisetsu
from .database import get_t_controller_data, get_t_controller_object, get_t_devices_data, get_t_devices_object

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            user_id = user.id
            request.session['user_id'] = user_id
            return redirect('houjin.html') # replace with the name of your houjin.html template
        else:
            return render(request, 'index.html', {'error_message': 'Invalid credentials'})
    else:
        return render(request, 'index.html')

@login_required
def controller(request):
    building_name = request.session.get('building_name')
    shisetsu = Shisetsu.objects.get(shisetsu_name=building_name)
    shisetsu_id = shisetsu.id
    controller = get_t_controller_data(shisetsu_id)
    context = {'controller': controller, 'building_name': building_name}
    return render(request, 'controller.html', context)  

@login_required
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

@login_required
def devices(request):
    deviceId = request.session.get('device_id')
    devices = get_t_devices_data(deviceId)
    context = {'devices': devices}
    return render(request, 'devices.html', context)  

@login_required
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

@login_required
def houjin(request):        
    user_id = request.user.id
    houjins = Houjin.objects.filter(user_id=user_id)
    context = {'houjins': houjins}
    print('houjin')
    return render(request, 'houjin.html', context)  



@login_required
def store_building_name(request):
    if request.method == 'POST':
        building_name = request.POST.get('building_name')
        houjin_id = request.POST.get('houjin_id')
        request.session['building_name'] = building_name
        request.session['houjin_id'] = houjin_id
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=400)

@login_required
def store_device_id(request):
    device_id = request.POST.get('device_id')
    request.session['device_id'] = device_id
    return JsonResponse({'success': True})

@login_required
def shisetsu(request, houjin_id):
    shisetsu_list = Shisetsu.objects.filter(houjin_id=houjin_id)
    buildings = [s.shisetsu_name for s in shisetsu_list]
    data = {'buildings': buildings}
    return JsonResponse(data)

@login_required
def get_shisetsu_names(request, houjin_id=None):
    if houjin_id is None:
        houjin_id = request.session.get('houjin_id')
    shisetsu_list = Shisetsu.objects.filter(houjin_id=houjin_id)
    # shisetsu_list = serializers.serialize('python', shisetsu_list)
    buildings = [s.shisetsu_name for s in shisetsu_list]
    data = {'buildings': buildings}
    return JsonResponse(data)

@login_required
def get_all_shisetsu_names(request):
    shisetsu_list = Shisetsu.objects.all()
    # shisetsu_list = serializers.serialize('python', shisetsu_list)
    buildings = [s.shisetsu_name for s in shisetsu_list]
    data = {'buildings': buildings}
    return JsonResponse(data)

@login_required
def get_houjin_names(request):
    user_id = request.session.get('user_id')
    houjin_list = Houjin.objects.filter(user_id=user_id)
    # shisetsu_list = serializers.serialize('python', shisetsu_list)
    houjins = [{'id': s.id, 'name': s.houjin_name} for s in houjin_list]
    data = {'houjins': houjins}
    return JsonResponse(data)

@login_required
def houjin_search_view(request):
    query = request.GET.get('query')
    if query:
        buildings = Shisetsu.objects.filter(shisetsu_name__icontains=query)
    else:
        buildings = Shisetsu.objects.none()
    buildings_list = serializers.serialize('python', buildings)
    data = {'buildings': buildings_list}
    return JsonResponse(data)

def get_class_names(request, school_id):
    class_names = ClassName.objects.filter(school_id=school_id)
    class_name_data = [{'name': class_name.name} for class_name in class_names]
    return JsonResponse(class_name_data, safe=False)