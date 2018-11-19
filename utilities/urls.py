from django.contrib import admin
from django.conf.urls import url, include
from .views import *
urlpatterns = [
    url(r'^countries/$', ListCountries.as_view(), name='list-countries'),
    url(r'^states/$', ListStates.as_view(), name='list-states'),
    url(r'^rules/$', ListRules.as_view(), name='list-rules'),
    url(r'^typeidentification/$', ListTypeId.as_view(), name='list-typeid'),
    url(r'^contributereg/$', ListContributeRegimen.as_view(), name='list-contribute-regimen'),
    url(r'^authid/$', AuthUser.as_view(), name='view-auth-id'),
]