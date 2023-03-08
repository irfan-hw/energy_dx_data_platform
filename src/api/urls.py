from rest_framework import routers
from .views import TControllerViewSet,TDataGetViewSet,TDataSetViewSet,TDeviceDidoViewSet,TDeviceEnlViewSet,TDevicesViewSet

router = routers.DefaultRouter()
router.register(r'tcontroller', TControllerViewSet, basename='tcontroller')
router.register(r'tdataget', TDataGetViewSet, basename='tdataget')
router.register(r'tdataset', TDataSetViewSet, basename='tdataset')
router.register(r'tdevicedido', TDeviceDidoViewSet)
router.register(r'tdeviceenl', TDeviceEnlViewSet)
router.register(r'tdevices', TDevicesViewSet, basename='tdevices')