from rest_framework import serializers
from .models import Users
class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('first_name', 'last_name', 'number_identification', 'cellphone',
			'country', 'state', 'city', 'postal_code', 'address_location', 'contributory_regimen')