from django.db import models

# Create your models here.

class KhachHang(models.Model):
    tenKH = models.CharField(null=False,blank=False,max_length=200)
    email = models.CharField(null=False,blank=False,max_length=200)
    password =  models.CharField(null=False,blank=False,max_length=200)
    diaChi = models.TextField(null=False,blank=False,max_length=500)
    dienThoai = models.CharField(null=False,blank=False,max_length=200)
    

    def __str__(self) -> str:
        return self.tenKH



