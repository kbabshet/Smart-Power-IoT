from django.conf.urls import url

from . import views

app_name = "devices"
urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),  # HOME PAGE
    url(r'^devices/$', views.list, name='list'),
    url(r'^devices/(?P<device_id>[0-9]+)/$', views.detail,
        name='detail'),  # DETAILS PAGE
    url(r'^devices/(?P<device_id>[0-9]+)/change-state$',
        views.change_device_state, name='change_device_state'),
    url(r'^login/', views.login, name='login'),
]
