# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.contrib import admin

# Register your models here.

admin.site.register(UnitMeasurement)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(ImagesProduct)
