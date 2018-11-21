# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Countries(models.Model):
    id_contry = models.AutoField(primary_key=True)
    country_name = models.CharField(max_length=250)
    def __str__(self): 
        return self.country_name

class States(models.Model):
    id_state = models.AutoField(primary_key=True)
    country = models.ForeignKey(Countries)
    state = models.CharField(max_length=255)
    def __str__(self):
        return self.state

class TypeIdentification(models.Model):
    id_type_identification = models.AutoField(primary_key=True)
    concept = models.CharField(max_length=250) 

    def __str__(self):
        return self.concept

class ContributeRegimen(models.Model):
    id_contribute_regimen = models.AutoField(primary_key=True)
    regimen = models.CharField(max_length=250)

    def __str__(self):
        return self.regimen

class Sectors(models.Model):
    id_sector = models.AutoField(primary_key=True)
    name_sector = models.CharField(max_length=250)
    description_sector = models.TextField()
    
    def __str__(self):
        return self.name_sector

class Rules(models.Model):
    id_rules = models.IntegerField(primary_key=True)
    rule = models.CharField(max_length=250)

    def __str__(self):
		return self.rule
