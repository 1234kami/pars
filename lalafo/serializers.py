from rest_framework import serializers
from .models import Ad

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = '__all__'
from .models import ApartmentRent

class ApartmentRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentRent
        fields = '__all__'

from .models import ApartmentSale

class ApartmentSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApartmentSale
        fields = '__all__'