from django.db import models
from django_add_default_value import AddDefaultValue


# class Contacts(models.Model):
#     firstName= models.CharField(max_length=50)
#     lastName= models.CharField(max_length=50)
#     email=models.EmailField(max_length=50)
#     phoneNumber=models.IntegerField(null=True)

# class Properties(models.Model):
#     class Meta:
#         abstract=True

# class PropertyOwner(models.Model):
#     contact= models.ForeignKey(Contacts,null=True,on_delete=models.CASCADE)

# class Tenant(models.Model):
#     contact= models.ForeignKey(Contacts,on_delete=models.CASCADE)

class Listing(models.Model):
    location= models.CharField(max_length=50)
    coverPhoto=models.ImageField(upload_to ='uploads/images',blank='false', null='false')
    # photos = models.JSONField('uploads/photos',blank='false', null='false')
    otherPhotos = models.ImageField('uploads/photos',blank='false', null='false')
    purpose=models.CharField(max_length=50)
    furnishingStatus=models.CharField(max_length=50)
    housetype=models.CharField(max_length=50)
    description=models.TextField(max_length=1000,blank=True)
    rooms=models.IntegerField()
    amenities=models.CharField(max_length=5000)
    bathrooms=models.IntegerField()
    class Meta:
        abstract=True


class ForSale(Listing):
    ownerId=models.CharField(max_length=500)
    # ownerId=models.ForeignKey(Contacts,null=True,on_delete=models.CASCADE)
    price=models.IntegerField()

    # listing= models.OneToOneField(Listing,null=True,on_delete=models.CASCADE)


class ForRent(Listing):
    ownerId=models.CharField(max_length=500)
    # owner= models.ForeignKey(Contacts,null=True,on_delete=models.CASCADE)
    rentamount=models.IntegerField(blank=True)
    rentFrequency=models.CharField(max_length=50)
    # listing= models.OneToOneField(Listing,null=True,on_delete=models.CASCADE)


