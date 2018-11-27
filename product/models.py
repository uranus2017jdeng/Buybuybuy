# coding=utf-8
from __future__ import unicode_literals
from django.contrib.auth.models import User
import traceback
from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField('类别', max_length=10)

    def __str__(self):
        return self.name.__str__()
