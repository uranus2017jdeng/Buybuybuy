# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
import traceback
from django.db import models



# Create your models here.
class Customer(models.Model):
    name = models.CharField('姓名',max_length=10)
    phone = models.CharField('电话',max_length=20)
    address = models.CharField('地址',max_length=100,default='深圳')
    vip = models.IntegerField('VIP',default=0)


    def __str__(self):
        return self.name.__str__()