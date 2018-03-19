from django.db import models
from django.contrib.auth.models import User
import datetime


class Invoice(models.Model):
    transaction_id = models.CharField(max_length=200, default = '')
    name = models.CharField(max_length=50)
    quantity = models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.FloatField()
    unit_price = models.FloatField(default=0.0)
    date = models.DateTimeField(auto_now_add=True)
    buyer = models.CharField(max_length=50,default='NILL',blank=True)


    def __str__(self):
        return self.transaction_id

class TempTran(models.Model):
    item = models.CharField(max_length=50)
    quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    buyer = models.CharField(max_length=50,default='NILL',blank=True)

    def __str__(self):
        return self.item


class InvoiceRecord(models.Model):
    transaction_id = models.CharField(max_length=200)
    buyer = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    price = models.FloatField(default=0)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return 'sold to  '+self.buyer
