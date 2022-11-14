from django.urls import path
from . import views

urlpatterns = [
    path('', views.showform, name='pay'),
    path('paymentcomplete', views.thankspayment, name='paymentcomplete'),
]


