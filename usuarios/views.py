# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Users
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from .serializers import UsersSerializer
from django.http import *

# Create your views here.
class ListUsers(APIView):
	def get(self, request):
		usuarios = Users.objects.all()
		usuarios_json = UsersSerializer(usuarios, many=True)
		return Response(usuarios_json.data)

	def post(self, request):
		usuario_json = UsersSerializer(data = request.data)
		if usaurio_json.is_valid():
			usuario_json.save()
			return Response(usuario_json.data, status=201)
		return Response(usuario_json.data.errors, status=400) 