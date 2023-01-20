from rest_framework import routers
from .views import TControllerViewSet,TDataGetViewSet,TDataSetViewSet,TDeviceDidoViewSet,TDeviceEnlViewSet,TDevicesViewSet

router = routers.DefaultRouter()
router.register(r'tcontroller', TControllerViewSet)
router.register(r'tdataget', TDataGetViewSet)
router.register(r'tdataset', TDataSetViewSet)
router.register(r'tdevicedido', TDeviceDidoViewSet)
router.register(r'tdeviceenl', TDeviceEnlViewSet)
router.register(r'tdevices', TDevicesViewSet)