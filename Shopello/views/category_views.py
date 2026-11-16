from django.shortcuts import render, redirect
from ..models import Categories
from django.contrib import messages
def create(request):
    return render(request,'categories/create.html')
def createCategory(request):
    return render(request,'categories/create.html')
def store(request):
    category=Categories()
    category.categoryName=request.POST.get('categoryName')
    category.save()
    messages.success(request,"Category Added Successfully")
    return render(request,'categories/create.html')
def index(request):
    categories=Categories.objects.raw('SELECT * FROM shopello_categories WHERE status IS NULL')
    return render(request,'categories/index.html',{'categories':categories})
def updateView(request,pk):
    category=Categories.objects.get(id=pk)
    return render(request,'categories/edit.html',{'category':category})
def update(request,pk):
    category=Categories.objects.get(id=pk)
    category.categoryName=request.POST.get('categoryName')
    category.save()
    messages.success(request,"Category Updated Successfully")
    return redirect('/categories')
def delete(request,pk):
    category=Categories.objects.get(id=pk)
    category.status="deleted"
    category.save()
    messages.success(request,"Category Deleted Successfully")
    return redirect('/categories')