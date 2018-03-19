from django.db import models
from django.contrib.auth.models import User
import os
from django.conf import settings
# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length = 150,blank=True)
    last_name = models .CharField(max_length = 150,blank=True)
    username = models.OneToOneField(User,on_delete = models.CASCADE)
    email = models.EmailField(max_length = 200,blank=True)
    profile_picture = models.ImageField(default = 'default.png',blank = True)
    business = models.CharField(max_length = 200)

    def __str__(self):
        user = str(self.username)
        return user

    def users(self):
        return str(self.username)
    def rem_file(self):
        os.remove(os.path.join(settings.MEDIA_ROOT,self.profile_picture.name))

class verified(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    is_verified = models.BooleanField(default=False,blank=True)
    v_key = models.IntegerField()


    def __str__(self):
        if self.is_verified:
            message = ' Verified'
        else:
            message = ' Unverified'
        return str(self.user)+ message
