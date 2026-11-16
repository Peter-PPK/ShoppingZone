from django.shortcuts import render,redirect
from ..models import Centers,Cities
from django.contrib import messages
def create(request):
    cities=Cities.objects.raw('SELECT * FROM shopello_cities WHERE status IS NULL')
    return render(request,'centers/create.html',{'cities':cities})
def store(request):
    center=Centers()
    center.centerName=request.POST.get('centerName')
    center.address=request.POST.get('address')
    center.cityID_id=request.POST.get('cityName')
    center.status=request.POST.get('status')
    center.save()
    messages.success(request,"Center Added Successfully")
    return redirect('/centers')
def index(request):
    centers=Centers.objects.raw('SELECT * FROM shopello_centers As C1 LEFT JOIN shopello_cities AS C2 ON C1.cityID_id = C2.id WHERE C1.status != "deleted"')
    return render(request,'centers/index.html',{'centers':centers})
def updateView(request,pk):
    cities=Cities.objects.all()
    center=Centers.objects.get(id=pk)
    return render(request,'centers/edit.html',{'center':center,'cities':cities})
def update(request,pk):
    center=Centers.objects.get(id=pk)
    center.centerName=request.POST.get('centerName')
    center.address=request.POST.get('address')
    center.cityID_id=request.POST.get('cityName')
    center.status=request.POST.get('status')
    center.save()
    messages.success(request,"Center Update Successfully")
    return redirect('/centers')
def delete(request,pk):
    center=Centers.objects.get(id=pk)
    center.status="deleted"
    center.save()
    messages.success(request,"Center Deleted Successfully")
    return redirect('/centers')