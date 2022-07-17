from django.db import models
import datetime
import os 
from django.contrib.auth.models import User

# Create your models here.

def get_file_path(request,filename):
    return os.path.join('static/uploads/',filename)

class HangSX(models.Model):
    tenHSX = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self) -> str:
        return self.tenHSX


class SanPham(models.Model):
    tenSP = models.CharField(max_length=200,null=False,blank=False)
    maHSX = models.ForeignKey(HangSX,on_delete=models.CASCADE)
    soLuong = models.IntegerField(null=False,blank=False)
    anhSP = models.ImageField(upload_to = get_file_path,height_field=None,width_field=None,max_length = None,null = True,blank= True)
    moTa = models.TextField(max_length=500,null=False,blank=False)
    kieuDang = models.CharField(max_length=200,null=False,blank=False)
    manHinh = models.CharField(max_length=200,null=False,blank=False)
    camera = models.CharField(max_length=200,null=False,blank=False)
    boNhoTrong = models.CharField(max_length=200,null=False,blank=False)
    heDieuHanh = models.CharField(max_length=200,null=False,blank=False)
    CPU = models.CharField(max_length=200,null=False,blank=False)
    ram = models.CharField(max_length=200,null=False,blank=False)
    pin = models.CharField(max_length=200,null=False,blank=False)

    def __str__(self) -> str:
        return self.tenSP




