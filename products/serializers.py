 from rest_framework import serializers
from .models import *

class UnitMeasuresSerializers(serializers.ModelSerializer):
	class Meta:
		model = UnitMeasurement
		fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Category
		fields = '__all__'


class BrandsSerializer(serializers.ModelSerializer):
	logo = serializers.FileField('logo.url')
	class Meta:
		model = Brand
		fields = '__all__'

class ProductsSerializer(serializers.ModelSerializer): 
	class Meta: 
		model = Product
		fields = '__all__'

class ImagesProductsSerializer(serializers.ModelSerializer):
	image = serializers.FileField('image.url')
	class Meta:
		model = ImagesProduct
		fields = '__all__'