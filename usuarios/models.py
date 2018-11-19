# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from utilities.models import *
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Users(models.Model):
	auth_user = models.ForeignKey(User)
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	type_identification =  models.ForeignKey(TypeIdentification)
	number_identification = models.CharField(max_length=20)
	cellphone = models.CharField(max_length=15)
	country = models.ForeignKey(Countries)
	state = models.ForeignKey(States)
	city = models.CharField(max_length=50)
	postal_code = models.CharField(max_length=50)
	address_location = models.CharField(max_length=255)
	contributory_regimen = models.ForeignKey(ContributeRegimen)
	rol = models.ForeignKey(Rules)

	def __str__(self):
		return self.first_name