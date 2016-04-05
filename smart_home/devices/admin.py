from django.contrib import admin

from .models import Device
from .models import DeviceState
from .models import Location


admin.site.register(Device)
admin.site.register(DeviceState)
admin.site.register(Location)
