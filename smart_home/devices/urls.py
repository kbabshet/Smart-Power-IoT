from django.conf.urls import url

from . import views

app_name = "devices"
urlpatterns = [
	url(r'^$', views.home_page, name='home_page'), # HOME PAGE
	url(r'^list/', views.list, name='list'),
	url(r'^(?P<device_id>[0-9]+)/$', views.detail, name='detail'), # DETAILS PAGE
	url(r'^login/', views.login, name='login'),
    #url(r'^(?P<device_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<device_id>[0-9]+)/change-state$', views.change_device_state, name='change_device_state'),
    #url(r'^devices/$', views.detail, name="device_list"),
]
