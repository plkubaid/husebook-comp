from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class support(models.Model):
    email = models.EmailField()
    complain_id = models.CharField(max_length=50)
    com_type = models.CharField(max_length=20)
    body = models.TextField()
    seen = models.BooleanField(default=False,blank=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.complain_id + str(self.user) + self.com_type


class Open_Support(models.Model):
    email = models.EmailField()
    complain_id = models.CharField(max_length=50)
    com_type = models.CharField(max_length=20)
    body = models.TextField()
    seen = models.BooleanField(default=False,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.complain_id + self.email

class suggestionM(models.Model):
    email = models.EmailField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    body = models.TextField()
    seen = models.BooleanField(default=False,blank=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email + str(self.body)

class support_employee(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user)
