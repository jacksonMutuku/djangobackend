# realtor/serializers.py
from rest_framework import serializers
from .models import ForRent
from .models import ForSale


class ForSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForSale
        fields= '__all__'


class ForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForRent
        fields= '__all__'