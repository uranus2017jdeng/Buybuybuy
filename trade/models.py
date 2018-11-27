# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
import traceback
from django.db import models
from customer.models import *
from product.models import *
from django.utils import timezone


# Create your models here.
class Trade(models.Model):

    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)

    #交易状态
    # 0 未完成
    # 1 待采购
    # 2 已完成
    status = models.IntegerField('交易状态',default=0)
    product = models.ForeignKey(Product,null=True,on_delete=models.SET_NULL)
    tradename = models.DateField('交易时间')
    deposit  = models.DecimalField('订金',default=0,max_digits=10,decimal_places=2)

    def __str__(self):
        return self.name.__str__()
