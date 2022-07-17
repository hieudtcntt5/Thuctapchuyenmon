from math import prod
from django.shortcuts import redirect, render
from django.views import View
from matplotlib.style import context
from numpy import product
from .models import *
from django.contrib import messages
from order.models import ChiTietDonDH,DonDatHang
from supply.models import ChiTietPhieuNhap,PhieuNhapKho

# Create your views here.

def home(request):
    category = HangSX.objects.all()
    product_apple = SanPham.objects.filter(maHSX = 1).order_by('-ram')[:3]
    for item in product_apple:
        item.Nhap = ChiTietPhieuNhap.objects.filter(maSP = item.id).first
        item.Ban = ChiTietDonDH.objects.filter(maSP = item.id).first
    
    product_sony = SanPham.objects.filter(maHSX = 5).order_by('-ram')[:3]
    for item in product_sony:
        item.Nhap = ChiTietPhieuNhap.objects.filter(maSP = item.id).first
        item.Ban = ChiTietDonDH.objects.filter(maSP = item.id).first

    product_samsung = SanPham.objects.filter(maHSX = 6).order_by('-ram')[:3]
    for item in product_sony:
        item.Nhap = ChiTietPhieuNhap.objects.filter(maSP = item.id).first
        item.Ban = ChiTietDonDH.objects.filter(maSP = item.id).first
    context = {'category' : category,'product_apple':product_apple,'product_sony':product_sony,'product_samsung':product_samsung}
    return render(request,'homepage/top_product.html',context=context)

def homecollections(request,id):
    category = HangSX.objects.all()
    if HangSX.objects.get(id = id):
        products = SanPham.objects.filter(maHSX = id)
        maHSX = id
        for item in products:
           item.Nhap = ChiTietPhieuNhap.objects.filter(maSP = item.id).first
           item.Ban = ChiTietDonDH.objects.filter(maSP = item.id).first
        context = {'products' : products,'maHSX' : maHSX,'category' : category}
        return render(request,'homepage/home_collections.html',context=context)

def details_product(request,id_hangsx,id_sanpham):
    category = HangSX.objects.all()
    if HangSX.objects.get(id = id_hangsx):
        if SanPham.objects.filter(id = id_sanpham ):
            products = SanPham.objects.filter(id = id_sanpham ).first
            giaNhap = ChiTietPhieuNhap.objects.filter(maSP = id_sanpham).first
            giaBan =  ChiTietDonDH.objects.filter(maSP = id_sanpham).first
            context = {'products' : products,'giaNhap' : giaNhap,'giaBan':giaBan,'category' : category}
            return render(request,'homepage/single.html',context=context)
        else:
            messages.error("No such category found")
            return redirect('home')

    else:
       messages.error("No such category found")
       return redirect('home')

def searchproduct(request):
    category = HangSX.objects.all()
    if request.method == "POST":
       key = request.POST.get('searchproduct')
       products = SanPham.objects.filter(tenSP__contains=key)
       for item in products:
           item.Nhap = ChiTietPhieuNhap.objects.filter(maSP = item.id).first
           item.Ban = ChiTietDonDH.objects.filter(maSP = item.id).first
           ma = item.maHSX
       hang = HangSX.objects.filter(tenHSX = ma).first
       context = {'products' : products,'hang' : hang,'category' : category}
       return render(request,'homepage/search.html',context=context)
    
def single(request):
    return render(request,'homepage/single.html')

def checkout(request):
    return render(request,'homepage/checkout.html')
