from django.db import models
from products.models import SanPham
from user.models import KhachHang

# Create your models here.

class DonDatHang(models.Model):
    maKH = models.ForeignKey(KhachHang,on_delete=models.CASCADE)
    ngayDat = models.DateTimeField()
    ngayGiao = models.DateTimeField()

    def __str__(self) -> str:
        return str(self.id)

class ChiTietDonDH(models.Model):
    maDDH = models.ForeignKey(DonDatHang,on_delete=models.CASCADE)
    maSP = models.ForeignKey(SanPham,on_delete=models.CASCADE)
    soLuong = models.IntegerField(null=False,blank=False)
    donGia = models.FloatField(null=False,blank=False)
    thanhTien = models.FloatField(null=False,blank=False)

    def __str__(self) -> str:
        return str(self.maSP)
