from django.db import models
from django_add_default_value import AddDefaultValue

class Listing(models.Model):
    location= models.CharField(max_length=50)
    coverPhoto=models.ImageField(upload_to ='uploads/images',blank='false', null='false')
    # photos = models.JSONField('uploads/photos',blank='false', null='false')
    otherPhotos = models.ImageField('uploads/photos',blank='false', null='false')
    purpose=models.CharField(max_length=50)
    furnishingStatus=models.CharField(max_length=50)
    housetype=models.CharField(max_length=50)
    description=models.TextField(max_length=1000,blank=True)
    rooms=models.CharField(max_length=50)
    amenities=models.CharField(max_length=5000)
    bathrooms=models.CharField(max_length=50)
    class Meta:
        abstract=True


class ForSale(Listing):
    ownerId=models.CharField(max_length=500)
    price=models.IntegerField()

    
class ForRent(Listing):
    ownerId=models.CharField(max_length=500)
    rentamount=models.IntegerField(blank=True)
    rentFrequency=models.CharField(max_length=50)


class PhoneNumber(models.Model):
    phone= models.IntegerField()

    def __str__(self):
        return {self.phone}

# STATUS = ((1, "Pending"), (0, "Complete"))

# class Transaction(models.Model):
#     """This model records all the mpesa payment transactions"""
#     transaction_no = models.CharField(default=uuid.uuid4, max_length=50, unique=True)
#     phone_number=models.CharField(max_length=15)
#     checkout_request_id = models.CharField(max_length=200)
#     reference = models.CharField(max_length=40, blank=True)
#     description = models.TextField(null=True, blank=True)
#     amount = models.CharField(max_length=10)
#     status = models.CharField(max_length=15, choices=STATUS, default=1)
#     receipt_no = models.CharField(max_length=200, blank=True, null=True)
#     created = models.DateTimeField(auto_now_add=True)
#     ip = models.CharField(max_length=200, blank=True, null=True)

#     def __unicode__(self):
#         return f"{self.transaction_no}"

# class PhoneNumbers(models.Model):
#     phone = models.IntegerField()

#     def __str__(self):
#         return {self.phone}
