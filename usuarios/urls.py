from django.contrib import admin
from django.conf.urls import url, include
from .views import *
urlpatterns = [
    url(r'^usuarios/$', ListUsers.as_view(), name='list-usuarios'),
]