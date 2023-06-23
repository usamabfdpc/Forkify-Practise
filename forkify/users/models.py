from django.db import models
from django.contrib.auth.models import AbstractUser
from enumchoicefield import ChoiceEnum, EnumChoiceField
from phone_field import PhoneField


# Enums
class Role(ChoiceEnum):
    customer = "customer"
    seller = "seller"

class OrderType(ChoiceEnum):
    parcel = "parcel"
    on_table = "table"

# Mixins
class ImageMixin(models.Model):
    alt_text = models.CharField(max_length=50)
    title = models.CharField(max_length=30)

    class Meta:
        abstract = True    


# Create your models here.

class Address(models.Model):
    country = models.CharField(max_length=50)
    province = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    street = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=5)
    more_details = models.CharField(max_length=200,blank=True)




class Users(ImageMixin,AbstractUser):
    Role_CHOICES = [
    ('s', 'seller'),
    ('c', 'customer'),
    
]
    phone = PhoneField(help_text='Contact phone number')
    image = models.ImageField(upload_to='images',blank=True)
    role = models.CharField(max_length=1,choices=Role_CHOICES,default=Role_CHOICES[1])
    address = models.ForeignKey(Address,on_delete = models.CASCADE,related_name='address',null = True)

    