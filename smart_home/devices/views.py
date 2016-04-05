from django.shortcuts import render
from django.http import HttpResponse

from .models import Device
from .models import DeviceState


def index(request):
    device_list = Device.objects.order_by('device_name')[:10]
    response = "\n".join([device.device_name for device in device_list])
    return HttpResponse(response)


def detail(request, device_id):
    return HttpResponse("This is the %s. It is currently %s" % (Device.objects.get(pk=device_id).device_name, DeviceState.objects.get(device__id=device_id)))
