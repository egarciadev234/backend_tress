# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .serializers import *
from .models import Countries
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from django.http import *
from django.contrib.auth.models import User

# Create your views here.
class ListCountries(APIView):
	def get(self, request):
		countries = Countries.objects.all()
		countries_json = CountriesSerializer(countries, many=True)
		return Response(countries_json.data)

class ListStates(APIView):
	def get(self, request):
		states = States.objects.all()
		states_json = StatesSerializer(states, many=True)
		return Response(states_json.data)

class ListRules(APIView):
	def get(self, request):
		rules = Rules.objects.all()
		rules_json = RulesSerializer(rules, many=True)
		return Response(rules_json.data)

class ListTypeId(APIView):
	def get(self, request):
		type_identification = TypeIdentification.objects.all()
		type_identification_json = TypeIdentificationSerializer(type_identification, many=True)
		return Response(type_identification_json.data)

class ListContributeRegimen(APIView):
	def get(self, request):
		contribute_regimen = ContributeRegimen.objects.all()
		contribute_regimen_json = ContributeRegimenSerializer(contribute_regimen, many=True)
		return Response(contribute_regimen_json.data)

class AuthUser(APIView):
	def get(self, request):
		# uid = request.session['my_id']
		# id_auth_user = User.objects.get(pk=uid)
		# user = request.user.id
		# id_auth_user = User.objects.get(pk=user)
		# id_auth_user_json = UserAuthSerializer(id_auth_user)
		user = User.objects.all()
		user_json = UserDetailSerializer(user, many=True)
		return Response(user_json.data)

