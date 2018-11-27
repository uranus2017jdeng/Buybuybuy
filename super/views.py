# coding=utf-8
from django.shortcuts import render
from django.http import  HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from PIL import Image, ImageDraw, ImageFont
import os
import random
import string
try:
    from cStringIO import StringIO
except ImportError:
    from io import StringIO
import datetime
import traceback
import json
import time

from Buybuybuy.settings import BASE_DIR
from super.models import *
# Create your views here.

def index(request):

    return render(request,'super/index.html',locals())
