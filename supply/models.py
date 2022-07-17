from pyexpat import model
from statistics import mode
from django.db import models
from products.models import SanPham

# Create your models here.

class NhaCungCap(models.Model):
    tenNCC = models.CharField(null=False,blank=False,max_length=200)
    diaChi = models.TextField(null=False,blank=False,max_length=500)
    dienTHoai = models.CharField(null=False,blank=False,max_length=200)

    def __str__(self) -> str:
        return self.tenNCC

class PhieuNhapKho(models.Model):
    maNCC = models.ForeignKey(NhaCungCap,on_delete=models.CASCADE)
    ngayNhap = models.DateTimeField()
    maNV = models.CharField(null=False,blank=False,max_length=200)

    def __str__(self) -> str:
        return str(self.id)

class ChiTietPhieuNhap(models.Model):
    maPNK = models.ForeignKey(PhieuNhapKho,on_delete=models.CASCADE)
    maSP = models.ForeignKey(SanPham,on_delete=models.CASCADE)
    soLuong = models.IntegerField(null=False,blank=False)
    donGia = models.FloatField(null=False,blank=False)
    thanhTien = models.FloatField(null=False,blank=False)

    def __str__(self) -> str:
        return str(self.maPNK)+" : "+str(self.maSP)


