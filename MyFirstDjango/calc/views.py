from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import CreateUserForm
from .models import *
from .forms import *

def home(request):
  return render(request,'home.html',{'name':'Rohan'})

def add(request):
  a=int(request.POST["num1"])
  b=int(request.POST["num2"])
  out=a+b
  return render(request, "result.html",{'result':out})

def dashboard(request):
  customers=Customer.objects.all()
  orders=Order.objects.all()
  return render(request, 'dashboard.html', {'customers':customers, 'orders':orders})

def products(request):
  products=Product.objects.all()
  return render(request, 'product.html', {'products':products})

def customer(request, pk_test):
  customer=Customer.objects.get(id=pk_test)
  customers=Customer.objects.all()
  orders=customer.order_set.all()
  order_count=orders.count()
  context={'customers':customers, 'cust':customer,'orders':orders,'ordcount':order_count}
  return render(request,'customer.html',context)

def createOrder(request):
  form=OrderForm()
  if request.method=="POST":
    form=OrderForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('/')
  context={'form':form}
  return render(request,'order_form.html',context)

def updateOrder(request, pk):
  order=Order.objects.get(id=pk)
  form=OrderForm(instance=order)
  if request.method=="POST":
    form=OrderForm(request.POST, instance=order)
    if form.is_valid():
      form.save()
      return redirect('/')
  context={'form':form}
  return render(request,'order_form.html',context)

def deleteOrder(request, pk):
  order=Order.objects.get(id=pk)
  if request.method=="POST":
    order.delete()
    return redirect('/')
  
  context={'item':order}
  return render(request, 'delete.html',context)

def registerPage(request):
  form=CreateUserForm()
  if request.method=="POST":
    form=CreateUserForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('login')
    else:
      messages.success(request, "Password does not follow the rules")

  context={'form':form}
  return render(request, 'register.html', context)
