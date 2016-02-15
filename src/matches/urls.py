from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^location/(?P<slug>[\w-]+)/$', 'matches.views.location_match_view', name='location_match_view_url'),
]