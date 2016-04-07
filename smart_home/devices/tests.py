from django.test import TestCase
from .models import Device, Location, DeviceState
from django.db import IntegrityError
from django.test import Client
from django.core.urlresolvers import reverse

class uniqueMethodTests(TestCase):

    # Test it will add a device to the database
    def testingAddsToDatabase(self):
        kitchen = Location(location_name='kitchen').save()
        bedroom = Location(location_name='bedroom').save()

        device1 = Device(device_name='kettle',serial_num='12345',ip_addr='172.16.254.1',
                         location=Location.objects.get(location_name='kitchen'),
                         current_state=DeviceState.objects.get(state='on'))

        device1.save()

        device2 = Device(device_name='kettle',serial_num='12345',ip_addr='172.16.254.2',
                         location=Location.objects.get(location_name='bedroom'),
                         current_state=DeviceState.objects.get(state='on'))

        device2.save()

        self.assertEqual(device1.id, 1)
        self.assertEqual(device2.id, 2)

    # Test model fields for serial number and IP address work correctly
    def testingVariableTypeDefinition(self):
        kitchen = Location(location_name='kitchen').save()

        device1 = Device(device_name='kettle',serial_num='abc',ip_addr='1721637',
                         location=Location.objects.get(location_name='kitchen'),
                         current_state=DeviceState.objects.get(state='on'))

        with self.assertRaises(ValueError):
            device1.save()

    # Test that it will not allow 2 same devices to have the same location
    def testingSameLocation(self):
        kitchen = Location(location_name='kitchen').save()

        device1 = Device(device_name='kettle',serial_num='12345',ip_addr='172.16.254.1',
                         location=Location.objects.get(location_name='kitchen'),
                         current_state=DeviceState.objects.get(state='on'))
        device2 = Device(device_name='kettle',serial_num='12345',ip_addr='172.16.254.2',
                          location=Location.objects.get(location_name='kitchen'),
                         current_state=DeviceState.objects.get(state='on'))

        device1.save()
        with self.assertRaises(IntegrityError):
            device2.save()

    # Test it will not allow 2 devices to have the same IP address
    def testingSameIPaddr(self):
        kitchen = Location(location_name='kitchen').save()
        bedroom = Location(location_name='bedroom').save()

        device1 = Device(device_name='kettle',serial_num='12345',ip_addr='172.16.254.1',
                         location=Location.objects.get(location_name='kitchen'),
                         current_state=DeviceState.objects.get(state='on'))

        device2 = Device(device_name='TV',serial_num='54321',ip_addr='172.16.254.1',
                          location=Location.objects.get(location_name='bedroom'),
                         current_state=DeviceState.objects.get(state='on'))

        device1.save()

        with self.assertRaises(IntegrityError):
            device2.save()

class viewTests(TestCase):
    def test_index_view_page(self):
        response = self.client.get(reverse('devices:home_page'))
        self.assertEqual(response.status_code, 200)

    def test_detail_view_page(self):
        kitchen = Location(location_name='kitchen').save()
        device1 = Device(device_name='kettle',serial_num='12345',ip_addr='172.16.254.1',
                         location=Location.objects.get(location_name='kitchen'),
                         current_state=DeviceState.objects.get(state='on'))

        device1.save()

        response = self.client.get(reverse('devices:detail', kwargs={'device_id': 1}))
        self.assertEqual(response.status_code, 200)

    def test_list_view_page(self):
        response = self.client.get(reverse('devices:list'))
        self.assertEqual(response.status_code, 200)

    def test_login_view_page(self):
        response = self.client.get(reverse('devices:login'))
        self.assertEqual(response.status_code, 200)