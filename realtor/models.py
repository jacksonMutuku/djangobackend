from django.db import models


class ForRent(models.Model):
    fname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    location= models.CharField(max_length=50)
    coverPhoto=models.ImageField(upload_to ='uploads/images',blank='false', null='false')
    coverPhoto1=models.ImageField(upload_to ='uploads/images',blank='true')
    # image_two = models.ImageField()
    # image_three = models.ImageField()
    rentamount=models.IntegerField(blank=True)
    purpose=models.CharField(max_length=50)
    bathno= models.IntegerField(blank=True)
    furnishingStatus=models.CharField(max_length=50)
    housetype=models.CharField(max_length=50)
    rentFrequency=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
    roomnumber=models.IntegerField()
    # area=models.float()
    # roomnumber=models.IntegerField()
    # date=models.DateTimeField(auto_add_now=True)


class ForSale(models.Model):
    fname= models.CharField(max_length=50)
    lastname= models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    location= models.CharField(max_length=50)
    coverPhoto=models.ImageField(upload_to ='uploads/images',blank='false', null='false')
    # image_two = models.ImageField()
    photos = models.ImageField('uploads/photos',blank='false', null='false')
    price=models.IntegerField(blank=True)
    purpose=models.CharField(max_length=50)
    bathno= models.IntegerField(blank=True)
    furnishingStatus=models.CharField(max_length=50)
    housetype=models.CharField(max_length=50)
    description=models.TextField(max_length=1000)
    roomnumber=models.IntegerField()
    # area=models.float()
    # roomnumber=models.IntegerField()
    # date=models.DateTimeField(auto_add_now=True)


    # def__str__(self):
    #     return self.name
    
    
