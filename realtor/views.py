# Create your views here.
from django.shortcuts import render
from rest_framework import permissions
from .models import ForRent
from .models import ForSale
from rest_framework.generics import CreateAPIView
from .serializers import ForSaleSerializer
from .serializers import ForRentSerializer
from rest_framework import viewsets
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,RetrieveAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.parsers import MultiPartParser,FormParser
from django.shortcuts import redirect, render
import requests
from requests.auth import HTTPBasicAuth
import datetime
import json
from .form import PhoneNumber


class ForSaleView(viewsets.ModelViewSet):
    queryset = ForSale.objects.all() 
    parser_classes=(MultiPartParser,FormParser)
    serializer_class = ForSaleSerializer


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



def getAccessToken(request):
    consumer_key = 'XjWEg9z1ihL9zoXO1JRaCOhfIJAgB8cu'
    consumer_secret = 'y48BAeDDA0AgXqI2'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'
    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token['access_token']
    return HttpResponse(validated_mpesa_access_token)

    
def showform(request):

    form = PhoneNumber()
    if request.method == 'POST':
        form = PhoneNumber(request.POST)
        if form.is_valid():

            form.save()
            number = '254' + str(form.cleaned_data.get('phone'))
            print(number)

            #print(total)
            access_token = MpesaAccessToken.validated_mpesa_access_token
            api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
            headers = {"Authorization": "Bearer %s" % access_token}
            request = {
                "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
                "Password": LipanaMpesaPpassword.decode_password,
                "Timestamp": LipanaMpesaPpassword.lipa_time,
                "TransactionType": "CustomerPayBillOnline",
                "Amount": 20,
                "PartyA":  number,  # replace with your phone number to get stk push -600989
                "PartyB": LipanaMpesaPpassword.Business_short_code,
                "PhoneNumber": number,  # replace with your phone number to get stk push
                "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
                "AccountReference": "Mania",
                "TransactionDesc": "Fear not for I am with you"
            }

            response = requests.post(api_url, json=request, headers=headers)
            print(response)
            # return HttpResponse('success')
            return redirect('thanks')

    context = {'form': form}
    return render(request, 'payments/payment.html', context)


# The last page
def thankspayment(request):

    t_time = datetime.datetime.now()
    hours = 0.5
    added_time = datetime.timedelta(hours=hours)
    time = t_time + added_time
    print(time)

    context = {'time': time}
    return render(request, 'payments/thanks.html', context)





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