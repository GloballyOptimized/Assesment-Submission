from django.db import models
from uuid import uuid4
#....................................................

class Merchant_Porfile(models.Model):
    merchant_id  = models.CharField(default=uuid4,primary_key=True,editable=False)
    firm_name = models.CharField(default='N/A',editable=True,max_length=100)
    mobile_number = models.CharField(default='N/A',editable=True,max_length=13)
    pan = models.CharField(default='N/A',editable=False,max_length=10)
    aadhar_number = models.CharField(default='N/A',editable=False,max_length=12)
    upi = models.CharField(default='N/A',editable=True,max_length=30)
    address_block_1 = models.CharField(editable=True,max_length=100,blank=False)
    address_block_2 = models.CharField(default='N/A',editable=True,max_length=100)
    city = models.CharField(editable=True,max_length=50)
    pincode = models.IntegerField(editable=True,blank=False)
