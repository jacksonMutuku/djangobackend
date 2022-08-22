from django.contrib import admin

from .models import ForRent
from .models import ForSale

admin.site.register(ForRent)
admin.site.register(ForSale)
