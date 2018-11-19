from rest_framework import serializers
from .models import Countries, States, ContributeRegimen, Rules, TypeIdentification
from django.contrib.auth.models import User

class CountriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Countries
		fields = '__all__'

class StatesSerializer(serializers.ModelSerializer):
	class Meta:
		model = States
		fields = '__all__'

class RulesSerializer(serializers.ModelSerializer):
	class Meta:
		model = Rules
		fields = '__all__'

class TypeIdentificationSerializer(serializers.ModelSerializer):
	class Meta:
		model = TypeIdentification
		fields = '__all__'

class ContributeRegimenserializer(serializers.ModelSerializer):
	class Meta:
		model = ContributeRegimen
		fields = '__all__'

class UserDetailSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = [
		    'id',
			'username',
			'email',
			'first_name',
			'last_name',
		]

