# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from rest_auth.registration.views import SocialLoginView, SocialConnectView
from django.shortcuts import render

# Create your views here.

class FacebookLogin(SocialLoginView):
	"""docstring for FacebookLogin"""
	adapter_class = FacebookOAuth2Adapter

class FacebookConnect(SocialConnectView):
    adapter_class = FacebookOAuth2Adapter