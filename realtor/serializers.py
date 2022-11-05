# realtor/serializers.py
from rest_framework import serializers
from .models import ForRent
from .models import ForSale
from .models import Contacts
# from .models import Listing


class ForSaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForSale
        fields= '__all__'
        extra_kwargs = {'std_code': {'required': False},'uni_code': {'required': False},
        'price': {'required': False },
        'location': {'required': False},
        'description': {'required': False},
        'housetype': {'required': False},
        'bathrooms': {'required': False},
        'rooms': {'required': False},
        'rentFrequency': {'required': False},
        'furnishingStatus': {'required': False},
        'purpose': {'required': False},
        }


class ForRentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ForRent
        fields= '__all__'
        extra_kwargs = {'std_code': {'required': False},'uni_code': {'required': False},
        'rentamount': {'required': False },
        'rentFrequency': {'required': False },
        'location': {'required': False},
        'description': {'required': False},
        'housetype': {'required': False},
        'bathrooms': {'required': False},
        'rooms': {'required': False },
        'rentFrequency': {'required': False},
        'furnishingStatus': {'required': False},
        'purpose': {'required': False},
        }

class PropertiesSerializer(serializers.ModelSerializer):
    rent = ForRentSerializer()
    sale = ForSaleSerializer()
    class Meta : 
        model = ForRent, ForSale
        fields = "__all__"

# class CombinedSerializer(serializers.Serializer):
#     allproperties=ForSaleSerializer(many=True)
#     class Meta:
#         model = ForRent
#         fields= '__all__'


class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contacts
        fields= '__all__'
        extra_kwargs = {'std_code': {'required': False},'uni_code': {'required': False},'lastname': {'required': False},'firstname': {'required': False},'phoneNumber': {'required': False},'email': {'required': False}}