
from math import prod
from django.shortcuts import redirect, render
from django.views import View
from numpy import product
from django.contrib import messages
from order.models import ChiTietDonDH,DonDatHang
from products.forms import CustomerUserForm
from supply.models import ChiTietPhieuNhap,PhieuNhapKho
from django.contrib.auth import authenticate,login,logout


def register(request):
    form = CustomerUserForm()
    if request.method == 'POST':
        form = CustomerUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Dang ki thanh cong | Chuyen sang dang nhap')
            return redirect('/loginpage')
    context = {'form':form}
    return render(request,'homepage/register.html',context=context)

def loginpage(request):
    # if request.user.is_authenticated:
    #     messages.warning(request,"Ban da dang nhap")
    #     return redirect('/home')
    # else:
    if request.method =='POST':    
        Username = request.POST.get('username')
        Password = request.POST.get('password')

        user = authenticate(request,username = Username , password = Password)
        if user is not None:
            login(request,user)
  #          messages.success("Dang nhap thanh cong")
            return redirect('/home')
        else:
            messages.error("Kiem tra lai username & password")
            return redirect('/loginpage')
    return render(request,'homepage/login.html')

def logoutpage(request):
    if request.user.is_authenticated:
        logout(request)

    return redirect('/home')