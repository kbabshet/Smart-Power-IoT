from django.db import models


class DeviceState(models.Model):
    state = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return self.state

class Device(models.Model):
    device_name = models.CharField(max_length=200)
    serial_num = models.IntegerField()
    ip_addr = models.GenericIPAddressField(unique=True)
    location = models.ForeignKey('Location', on_delete=models.CASCADE)
    current_state = models.ForeignKey('DeviceState', on_delete=models.CASCADE)

    def __str__(self):
        return self.device_name

    class Meta:
        unique_together = (('device_name', 'location'))

class Location(models.Model):
    location_name = models.CharField(max_length=200)

    def __str__(self):
        return self.location_name
