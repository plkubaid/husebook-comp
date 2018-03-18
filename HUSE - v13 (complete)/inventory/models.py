from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=50)
    unit_price = models.FloatField(max_length=7,blank=True)
    price = models.FloatField(max_length=7)
    quantity = models.IntegerField()
    danger_level =models.IntegerField(blank=True,default = 100)
    code = models.CharField(max_length=9)
    user = models.ForeignKey(User,on_delete=models.CASCADE)


    def __str__(self):
        return 'item: '+self.name +'  by user: '+str(self.user)
