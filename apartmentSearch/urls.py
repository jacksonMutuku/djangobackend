"""apartmentSearch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from realtor.views import ForRentView
from realtor.views import ForSaleView
# from realtor.views import showmultiplemodels
# from realtor.views import ContactsView,ContactsUpdateView
from realtor.views import ContactsCreateView,ContactsUpdateView,DataDetailsView,DataListView,showmultiplemodels

# from rest_framework import routers
from rest_framework.routers import DefaultRouter

# route=routers.DefaultRouter()
# route.register("",ForSaleView,basename='forsaleview')
# route.register("",ForRentView,basename='forrentview')
router = DefaultRouter()
router.register(r'forsale',ForSaleView,basename="forsale")
router.register(r'forrent',ForRentView,basename="forrent")
# router.register(r'properties',CombinedView,basename="properties")
# router.register(r'Contacts',ContactsCreateView,basename="Contacts")

urlpatterns = [
    path('properties/',showmultiplemodels),
    # path('properties/',CombinedView.as_view()),
    path('admin/', admin.site.urls),
    path('owner/<int:pk>/',DataDetailsView.as_view()),
    path('owner/',DataListView.as_view()),
    path('Create/',ContactsCreateView.as_view()),
    # path('Contacts/',ContactsCreateView.as_view(),name="Contacts"),
    path('<pk>/update/',ContactsUpdateView.as_view()),
    path('', include(router.urls)),
    # path('api/forrent/', include(route.urls)), 
    # path('api/forsale/', include(route.urls)),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
