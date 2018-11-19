# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
# Create your views here.

class ListBrands(APIView):
	def get(self, request):
		brands = Brand.objects.all()
		brands_json = BrandsSerializer(brands, many=True)
		return Response(brands_json.data)

class ListCategories(APIView):
	def get(self, request):
		categories = Category.objects.all()
		categories_json = CategoriesSerializer(categories, many=True)
		return Response(categories_json.data)

class ListProducts(APIView):
	def get(self, request):
		products = Product.objects.all()
		products_json = ProductsSerializer(products, many=True)
		return Response(products_json.data)

class DetailProduct(APIView):
	def get(self, request, uuid):
		product = Product.objects.filter(id_product = uuid)
		product_json = ProductsSerializer(product, many=True)
		return Response(product_json.data)

	def put(self, request, uuid):
		product = Product.objects.filter(id_product = uuid).first()
		product_json = ProductsSerializer(product, data=request.data)
		if product_json.is_valid(): 
			product_json.save()
			return Response(product_json.data)
		return Response(product_json.data.errors, status=400)

	def delete(self, request, uuid):
		product = Product.objects.filter(id_product = uuid)
		images = ImagesProduct.objects.filter(product_id_id = uuid)
		images.delete()
		product.delete()
		return Response(status=204)

class ImagesProducts(APIView):
	def get(self, request):
		images = ImagesProduct.objects.all()
		images_json = ImagesProductsSerializer(images, many=True)
		return Response(images_json.data)


class DetailsImagesProduct(APIView):
	def get(self, request, product):
		images = ImagesProduct.objects.filter(product_id_id = product)
		images_json = ImagesProductsSerializer(images, many=True)
		return Response(images_json.data)

