from django.db import models as m
from django.contrib.auth.models import User
import datetime


class Invoice(m.Model):
    transaction_id = m.CharField(max_length=200, default = '')
    name = m.CharField(max_length=50)
    quantity = m.IntegerField()
    user = m.ForeignKey(User,on_delete=m.CASCADE)
    price = m.FloatField()
    unit_price = m.FloatField(default=0.0)
    date = m.DateTimeField(auto_now_add=True)
    buyer = m.CharField(max_length=50,default='NILL',blank=True)


    def __str__(self):
        return self.transaction_id

class TempTran(m.Model):
    item = m.CharField(max_length=50)
    quantity = m.IntegerField(default=0)
    price = m.FloatField(default=0.0)
    user = m.ForeignKey(User,on_delete=m.CASCADE)
    buyer = m.CharField(max_length=50,default='NILL',blank=True)

    def __str__(self):
        return self.item


class InvoiceRecord(m.Model):
    transaction_id = m.CharField(max_length=200)
    buyer = m.CharField(max_length=100)
    date = m.DateTimeField(auto_now_add=True,blank=True)
    price = m.FloatField(default=0)
    user = m.ForeignKey(User,on_delete=m.CASCADE)


    def __str__(self):
        return 'sold to  '+self.buyer
