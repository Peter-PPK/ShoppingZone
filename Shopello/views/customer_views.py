from django.shortcuts import render, redirect
from ..models import Customers
from django.contrib import messages
def create(request):
    return render(request,'customers/create.html')
def createCustomer(request):
    return render(request,'customers/create.html')
def store(request):
    customer=Customers()
    customer.customerName=request.POST.get('customerName')
    customer.phoneNo=request.POST.get('phoneNo')
    customer.address=request.POST.get('address')
    customer.memberNo=request.POST.get('memberNo')
    customer.remark=request.POST.get('remark')
    customer.save()
    messages.success(request,"Customer Added Successfully")
    return render(request,'customers/create.html')
def index(request):
    customers=Customers.objects.raw('SELECT * FROM shopello_customers WHERE status IS NULL')
    return render(request,'customers/index.html',{'customers':customers})
def updateView(request,pk):
    customer=Customers.objects.get(id=pk)
    return render(request,'customers/edit.html',{'customer':customer})
def update(request,pk):
    customer=Customers.objects.get(id=pk)
    customer.customerName=request.POST.get('customerName')
    customer.save()
    messages.success(request,"Customer Updated Successfully")
    return redirect('/customers')
def delete(request,pk):
    customer=Customers.objects.get(id=pk)
    customer.status="deleted"
    customer.save()
    messages.success(request,"Customer Deleted Successfully")
    return redirect('/customers')