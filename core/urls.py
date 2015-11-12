from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^salon/create/$', SalonCreateView.as_view(), name='salon_create'),
  url(r'salon/$', SalonListView.as_view(), name='salon_list'),
  url(r'^salon/(?P<pk>\d+)/$', SalonDetailView.as_view(), name='salon_detail'),
  url(r'^salon/update/(?P<pk>\d+)/$', SalonUpdateView.as_view(), name='salon_update'),
  url(r'^salon/delete/(?P<pk>\d+)/$', SalonDeleteView.as_view(), name='salon_delete'),
  url(r'^salon/(?P<pk>\d+)/review/create/$', ReviewCreateView.as_view(), name='review_create'),
  url(r'^salon/(?P<salon_pk>\d+)/review/update/(?P<review_pk>\d+)/$', ReviewUpdateView.as_view(), name='review_update'),
  url(r'^salon/(?P<salon_pk>\d+)/review/delete/(?P<review_pk>\d+)/$', ReviewDeleteView.as_view(), name='review_delete'),
)
