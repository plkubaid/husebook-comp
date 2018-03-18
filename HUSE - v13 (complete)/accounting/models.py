from django.db import models
from django.contrib.auth.models import User
from billing.models import Invoice


class AccountsInvoice(models.Model):
    t_id = models.CharField(max_length=200)
    price = models.FloatField()
    cost = models.FloatField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.item + str(self.price)

class Accounting(models.Model):
    status = models.BooleanField()
    date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profit = models.FloatField()

    def __str__(self):
        if self.status == True:
            b= "Profit"
        else:
            b= 'Loss'
        return str(self.user)+str(self.date)+b

class TranRecord(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    cost = models.FloatField()
    category = models.CharField(max_length=50,default='Sales',blank=True)
    buyer = models.CharField(max_length=50)
    date = models.DateField(auto_now_add=True)
    profit = models.FloatField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.name + str(self.date)
