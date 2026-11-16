from django.shortcuts import render, redirect
from ..models import Brands
from django.contrib import messages
def create(request):
    return render(request,'brands/create.html')
def createBrand(request):
    return render(request,'brands/create.html')
def store(request):
    brand=Brands()
    brand.brandName=request.POST.get('brandName')
    brand.save()
    messages.success(request,"Brand Added Successfully")
    return render(request,'brands/create.html')
def index(request):
    brands=Brands.objects.raw('SELECT * FROM shopello_brands WHERE status IS NULL')
    return render(request,'brands/index.html',{'brands':brands})
def updateView(request,pk):
    brand=Brands.objects.get(id=pk)
    return render(request,'brands/edit.html',{'brand':brand})
def update(request,pk):
    brand=Brands.objects.get(id=pk)
    brand.brandName=request.POST.get('brandName')
    brand.save()
    messages.success(request,"Brand Updated Successfully")
    return redirect('/brands')
def delete(request,pk):
    brand=Brands.objects.get(id=pk)
    brand.status="deleted"
    brand.save()
    messages.success(request,"Brand Deleted Successfully")
    return redirect('/brands')
def storeAtProduct(request):
    if request.method == "POST":
        brandName = request.POST.get("brandName")
        if brandName:
            brand = Brands()
            brand.brandName = brandName
            brand.save()
            messages.success(request, "Brand created successfully!")
        else:
            messages.error(request, "Brand name cannot be empty.")
        return redirect("productCreate")
    return redirect("productCreate")
