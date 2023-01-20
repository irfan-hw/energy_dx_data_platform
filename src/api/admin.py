from django.contrib import admin
from .models import TController,TDataGet,TDataSet,TDeviceDido,TDeviceEnl,TDevices

# Register your models here.

@admin.register(TController)
class TController(admin.ModelAdmin):
    pass

@admin.register(TDataGet)
class TDataGet(admin.ModelAdmin):
    pass

@admin.register(TDataSet)
class TDataSet(admin.ModelAdmin):
    pass

@admin.register(TDeviceDido)
class TDeviceDido(admin.ModelAdmin):
    pass

@admin.register(TDeviceEnl)
class TDeviceEnl(admin.ModelAdmin):
    pass

@admin.register(TDevices)
class TDevices(admin.ModelAdmin):
    pass
