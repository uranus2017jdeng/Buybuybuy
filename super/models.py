# coding=utf-8
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class Title(models.Model):
    role_name = models.CharField(max_length=30, unique=True)
    role_desc = models.CharField(max_length=30, )

    def __str__(self):
        return self.role_name

class UserProfile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    nick = models.CharField('真实姓名', max_length=10, blank=True, null=True)
    title = models.ForeignKey(Title, null=True, on_delete=models.SET_NULL)
    birthday = models.DateField('生日', default='0000-00-00')