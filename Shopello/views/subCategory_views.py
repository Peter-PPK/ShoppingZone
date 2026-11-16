from django.shortcuts import render, redirect
from ..models import Cities, Centers, SubCategories
from django.contrib import messages
def create(requests):
    cities=Cities.objects.raw('SELECT * FROM cybershop_cities WHERE status IS Null')
    subCategories=subCategories.objects.raw('SELECT * FROM cybershop_subcategories WHERE status IS Null')
    return render(requests,'subCategories/create.html',{'subcategories':subCategories,'cities':cities})
def store(requests):
    subCategory=SubCategories()
    subCategory.subCategoryName=requests.POST.get('subCategoryName')
    subCategory.address=requests.POST.get('subCategory.address')
    subCategory.status=requests.POST.get('subCategory.status')
    subCategory.save()
    messages.success(requests,"subCategory Added Successfully")
    return redirect('/subCategories')
def index(request):
    subCategories=SubCategories.objects.raw('SELECT * FROM cybershop_subcategories WHERE status IS NULL')
    return render(request,'subCategories/index.html',{'subCategories':subCategories})
def updateView(request,pk):
    subCategories=SubCategories.objects.raw('SELECT * FROM cybershop_subcategories WHERE status IS NULL')
    subCategory=subCategories.objects.get(id=pk)
    return render(request,'subCategories/edit.html',{'subCategory':subCategory})
def update(request,pk):
    subCategories=SubCategories.objects.raw('SELECT * FROM cybershop_subcategories WHERE status IS NULL')
    subCategory=subCategories.objects.get(id=pk)
    subCategory.subCategoryName=request.POST.get('subCategoryName')
    subCategory.save()
    messages.success(request,"subCategory Updated Successfully")
    return redirect('/subCategories')
def delete(request,pk):
    subCategories=SubCategories.objects.raw('SELECT * FROM cybershop_subcategories WHERE status IS NULL')
    subCategory=subCategories.objects.get(id=pk)
    subCategory.status="deleted"
    subCategory.save()
    messages.success(request,"subCategory Deleted Successfully")
    return redirect('/subCategories')