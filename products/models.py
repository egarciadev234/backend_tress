# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from utilities.models import *
from django.db import models
import uuid
from django.contrib.auth.models import User

class UnitMeasurement(models.Model):
    id_measure = models.AutoField(primary_key=True)
    name_measure = models.CharField(max_length=40)
    def __str__(self):
        return self.name_measure

class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    name_category = models.CharField(max_length=250)
    sector_id = models.ForeignKey(Sectors)
    def __str__(self):
        return self.name_category

class Brand(models.Model):
    id_brand = models.AutoField(primary_key=True)
    name_brand = models.CharField(max_length=250)
    description_brand = models.TextField()
    logo = models.ImageField(upload_to="media/logos")
    def __str__(self):
        return self.name_brand

class Product(models.Model):
    id_product = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name_product = models.CharField(max_length=200)
    description = models.TextField()
    category_id = models.ForeignKey(Category)
    brand_id = models.ForeignKey(Brand)
    measure_id = models.ForeignKey(UnitMeasurement)
    provider_id = models.ForeignKey(User)
    sector_id = models.ForeignKey(Sectors)
    ranking = models.DecimalField(max_digits=3, decimal_places=2)
    def __str__(self):
        return self.name_product

class ImagesProduct(models.Model):
    product_id = models.ForeignKey(Product, related_name='images_products')
    image = models.ImageField(upload_to="/images_products")