from django.contrib.auth.decorators import login_required
from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
  url(r'^$', Home.as_view(), name='home'),
  url(r'^user/', include('registration.backends.simple.urls')),
  url(r'^user/', include('django.contrib.auth.urls')),
  url(r'^salon/create/$', login_required(SalonCreateView.as_view()), name='salon_create'),
  url(r'salon/$', login_required(SalonListView.as_view()), name='salon_list'),
  url(r'^salon/(?P<pk>\d+)/$', login_required(SalonDetailView.as_view()), name='salon_detail'),
  url(r'^salon/update/(?P<pk>\d+)/$', login_required(SalonUpdateView.as_view()), name='salon_update'),
  url(r'^salon/delete/(?P<pk>\d+)/$', login_required(SalonDeleteView.as_view()), name='salon_delete'),
  url(r'^salon/(?P<pk>\d+)/review/create/$', login_required(ReviewCreateView.as_view()), name='review_create'),
  url(r'^salon/(?P<salon_pk>\d+)/review/update/(?P<review_pk>\d+)/$', login_required(ReviewUpdateView.as_view()), name='review_update'),
  url(r'^salon/(?P<salon_pk>\d+)/review/delete/(?P<review_pk>\d+)/$', login_required(ReviewDeleteView.as_view()), name='review_delete'),
  url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
  url(r'^user/update/(?P<slug>\w+)/$', login_required(UserUpdateView.as_view()), name='user_update'),
  url(r'^user/delete/(?P<slug>\w+)/$', login_required(UserDeleteView.as_view()), name='user_delete'),
  url(r'^search/$', login_required(SearchSalonListView.as_view()), name='search'),
)
