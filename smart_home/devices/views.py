from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext, loader

from .models import Device
from .models import DeviceState

#def index(request):
#    device_list = Device.objects.order_by('device_name')[:10]
#    response = "\n".join([device.device_name for device in device_list])
#    return HttpResponse(response)

def home_page(request):
    device_list = Device.objects.order_by('device_name')[:10]
    return render(request,"index.html", {'devices': device_list})

def list(request):
    device_list = Device.objects.order_by('device_name')[:10]
    return render(request,"device.html", {'devices': device_list})

def detail(request, device_id):
	device = get_object_or_404(Device, pk=device_id)
	return render(request, "detail.html", {'device': device})

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

        return HttpResponse(device_state.state)
