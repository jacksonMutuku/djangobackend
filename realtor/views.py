# Create your views here.
from django.shortcuts import render
from .models import ForRent
from .models import ForSale
from .serializers import ForSaleSerializer
from .serializers import ForRentSerializer
from rest_framework import viewsets

class ForSaleView(viewsets.ModelViewSet):
    queryset = ForSale.objects.all() 
    #  queryset = Data.objects.all() .order_by('-purpose')
    serializer_class = ForSaleSerializer


class ForRentView(viewsets.ModelViewSet):
    queryset = ForRent.objects.all() 
    #  queryset = Data.objects.all() .order_by('-purpose')
    serializer_class = ForRentSerializer
