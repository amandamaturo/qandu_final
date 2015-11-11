from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^salon/create/$', SalonCreateView.as_view(), name='salon_create'),
  url(r'salon/$', SalonListView.as_view(), name='salon_list'),
  url(r'^salon/(?P<pk>\d+)/$', SalonDetailView.as_view(), name='salon_detail'),
)
