# Create your views here.
from django.shortcuts import render
from rest_framework import permissions
from .models import ForRent
from .models import ForSale
# from .models import PropertyOwner
# from .models import Contacts
from .models import Listing
from .serializers import ForSaleSerializer
from .serializers import ForRentSerializer
# from .serializers import ContactsSerializer
# from .serializers import CombinedSerializer
# from .serializers import PropertiesSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
# from rest_framework import generics,status
# from rest_framework import viewsets
# from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser,FormParser

class ForSaleView(viewsets.ModelViewSet):
    queryset = ForSale.objects.all() 
    parser_classes=(MultiPartParser,FormParser)
    serializer_class = ForSaleSerializer

# class PropertiesView(viewsets.ModelViewSet):
#     queryset = Listing.objects.all() 
#     serializer_class = PropertiesSerializer

# class CreatedData(viewsets.ModelViewSet):
#     queryset = ForSale.objects.all()
#     serializer_class = CombinedSerializer


# class CombinedView(viewsets.ModelViewSet):
#     queryset = ForRent.objects.all()
#     serializer_class = CombinedSerializer


@api_view(['GET'])
def showmultiplemodels(request):
    rentproperties=ForRent.objects.all()
    saleproperties=ForSale.objects.all()
    rentSerializeobj=ForRentSerializer(rentproperties,many=True)
    saleSerializeobj=ForSaleSerializer(saleproperties,many=True)
    resultmodel= saleSerializeobj.data+rentSerializeobj.data
    return Response(resultmodel)

class ForRentView(viewsets.ModelViewSet):
    queryset = ForRent.objects.all() 
    parser_classes=(MultiPartParser,FormParser)
    # dqueryset = Data.objects.all() .order_by('-purpose')
    serializer_class = ForRentSerializer


# class DataListView(ListAPIView):
#     queryset = Contacts.objects.all() 
#     serializer_class = ContactsSerializer

# class DataDetailsView(RetrieveAPIView):
#     queryset = Contacts.objects.all() 
#     serializer_class = ContactsSerializer


# class ContactsView(generics.ListCreateAPIView):
#     queryset = Contacts.objects.all() 
#     serializer_class = ContactsSerializer

#     def post(self, request, format=None):
#         pass
        
# class ContactsUpdateView(generics.UpdateAPIView):
#     queryset = Contacts.objects.all() 
#     serializer_class = ContactsSerializer
#     def get(self, request, format=None):
#         pass

# class ContactsCreateView(CreateAPIView):
#     queryset = Contacts.objects.all() 
#     serializer_class = ContactsSerializer

#  class ContactsCreateView(generics.ListCreateAPIView):

# class ContactsUpdateView(UpdateAPIView):
#     queryset = Contacts.objects.all() 
#     serializer_class = ContactsSerializer
    
