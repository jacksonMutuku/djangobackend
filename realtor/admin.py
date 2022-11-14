from django.contrib import admin
from .models import ForRent
from .models import ForSale
from .models import PhoneNumber
# from .models import PropertyOwner
# from .models import Contacts
# from .models import Tenant

# admin.site.register(Listing)
# admin.site.register(Contacts)
# admin.site.register(Tenant)
admin.site.register(PhoneNumber)
admin.site.register(ForRent)
admin.site.register(ForSale)
