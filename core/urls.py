from django.conf.urls import patterns, include, url
from .views import *
from django.contrib.auth.decorators import login_required

urlpatterns = patterns('',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^user/', include('registration.backends.simple.urls')),
    url(r'^user/', include('django.contrib.auth.urls')),
    url(r'^bar/create/$', login_required(BarCreateView.as_view()), name='bar_create'),
    url(r'bar/$', login_required(BarListView.as_view()), name='bar_list'),
    url(r'^bar/(?P<pk>\d+)/$', login_required(BarDetailView.as_view()), name='bar_detail'),
    url(r'^bar/update/(?P<pk>\d+)/$', login_required(BarUpdateView.as_view()), name='bar_update'),
    url(r'^bar/delete/(?P<pk>\d+)/$', login_required(BarDeleteView.as_view()), name='bar_delete'),
    url(r'^bar/(?P<pk>\d+)/response/create/$', login_required(ResponseCreateView.as_view()), name='response_create'),
    url(r'^bar/(?P<bar_pk>\d+)/response/delete/(?P<response_pk>\d+)/$', login_required(ResponseDeleteView.as_view()), name='response_delete'), 
    url(r'^vote/$', login_required(VoteFormView.as_view()), name='vote'),   
    url(r'^user/(?P<slug>\w+)/$', login_required(UserDetailView.as_view()), name='user_detail'),
    url(r'^user/update/(?P<slug>\w+)/$', login_required(UserUpdateView.as_view()), name='user_update'),
    url(r'^user/delete/(?P<slug>\w+)/$', login_required(UserDeleteView.as_view()), name='user_delete'),       
    url(r'^bar/(?P<bar_pk>\d+)/response/update/(?P<response_pk>\d+)/$', login_required(ResponseUpdateView.as_view()), name='response_update'),
)    