from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt

from .models import Device
from .models import DeviceState


def index(request):
    device_list = Device.objects.order_by('device_name')[:10]
    response = "\n".join([device.device_name for device in device_list])
    return HttpResponse(response)


def detail(request, device_id):
    return HttpResponse("This is the %s. It is currently %s" % (Device.objects.get(pk=device_id).device_name, DeviceState.objects.get(device__id=device_id)))


@csrf_exempt
def change_device_state(request, device_id):
    device = get_object_or_404(Device, pk=device_id)

    print(device_id)
    try:
        device_state = DeviceState.objects.get(pk=request.POST['state'])
    except(KeyError, DeviceState.DoesNotExist):
        return HttpResponse("You selected an invalid state!")
    else:
        device.current_state = device_state
        device.save()

        return HttpResponseRedirect(reverse("devices:index"))
