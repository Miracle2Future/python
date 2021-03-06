from django.db import models

# Create your models here.
class UserType(models.Model):
    name = models.CharField(max_length=32)

class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    user_type = models.ForeignKey(UserType,on_delete=models.DO_NOTHING) #Django 2.0+ on_delete为必选参数，需修改值为DO_NOTHING