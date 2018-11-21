"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from rest_framework_jwt.views import refresh_jwt_token
from login.views import FacebookLogin, FacebookConnect
from django.conf.urls.static import static
from  django.conf import settings

from rest_auth.registration.views import (
    SocialAccountListView, SocialAccountDisconnectView
)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^refresh-token/', refresh_jwt_token),
    url(r'^rest-auth/', include('rest_auth.urls')),
    url(r'^rest-auth/registration/', include('rest_auth.registration.urls')),
    url(r'^rest-auth/facebook/$', FacebookLogin.as_view(), name='fb_login'),
    url(r'^rest-auth/facebook/connect/$', FacebookConnect.as_view(), name='fb_connect'),
    url(r'^socialaccounts/$', SocialAccountListView.as_view(), name='social_account_list'),
    url(r'^socialaccounts/(?P<pk>\d+)/disconnect/$', SocialAccountDisconnectView.as_view(), name='social_account_disconnect'),
    url(r'^', include('usuarios.urls')),
    url(r'^', include('utilities.urls')),
] +static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
