from django.conf.urls import patterns, include, url
from .views import *

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^bar/create/$', BarCreateView.as_view(), name='bar_create'),
    url(r'bar/$', BarListView.as_view(), name='bar_list'),
    url(r'^bar/(?P<pk>\d+)/$', BarDetailView.as_view(), name='bar_detail'),
    url(r'^bar/update/(?P<pk>\d+)/$', BarUpdateView.as_view(), name='bar_update'),
    url(r'^bar/delete/(?P<pk>\d+)/$', BarDeleteView.as_view(), name='bar_delete'),
)
