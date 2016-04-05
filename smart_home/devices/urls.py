from django.conf.urls import url

from . import views

app_name = "devices"
urlpatterns = [
    url(r'^(?P<device_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<device_id>[0-9]+)/change-state$',
        views.change_device_state, name='change_device_state'),
    url(r'^$', views.index, name="index"),
]
