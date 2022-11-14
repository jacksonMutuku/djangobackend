# realtor/serializers.py
from rest_framework import serializers
from .models import ForRent
from .models import ForSale




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
        'coverPhoto': {'required': False},
        'otherPhotos': {'required': False},
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
        'coverPhoto': {'required': False},
        'otherPhotos': {'required': False},
        }

class PropertiesSerializer(serializers.ModelSerializer):
    rent = ForRentSerializer()
    sale = ForSaleSerializer()
    class Meta : 
        model = ForRent, ForSale
        fields = "__all__"




    # def validate_reference(self, reference):
    #     """Write your validation logic here"""
    #     if reference:
    #         return reference
    #     return "Test"

    # def validate_description(self, description):
    #     """Write your validation logic here"""
    #     if description:
    #         return description
    #     return "Test"



# class CombinedSerializer(serializers.Serializer):
#     allproperties=ForSaleSerializer(many=True)
#     class Meta:
#         model = ForRent
#         fields= '__all__'


# class ContactsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Contacts
#         fields= '__all__'
#         extra_kwargs = {'std_code': {'required': False},'uni_code': {'required': False},'lastname': {'required': False},'firstname': {'required': False},'phoneNumber': {'required': False},'email': {'required': False}}