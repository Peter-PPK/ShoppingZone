from django.shortcuts import render, redirect
from ..models import Products, Categories, Brands,SubCategories
from django.contrib import messages
def index(request):
    products=Products.objects.raw('SELECT * FROM shopello_products As P JOIN shopello_categories AS C ON P.categoryID_id=c.id JOIN shopello_brands AS B ON P.brandID_id=B.id WHERE P.status IS NULL')
    return render(request, 'products/index.html', {'products': products})
def create(request):
    categories=Categories.objects.raw('SELECT * FROM shopello_categories WHERE status IS Null')
    brands=Brands.objects.raw('SELECT * FROM shopello_brands WHERE status IS Null')
    return render(request,'products/create.html',{'categories':categories,'brands':brands})
def store(request):
    product=Products()
    product.productName=request.POST.get('productName')
    product.productImages=request.FILES['productImage']
    product.price=request.POST.get('price')
    product.description=request.POST.get('description')
    product.color=request.POST.get('color')
    product.size=request.POST.get('size')
    product.etaDate=request.POST.get('etaDate')
    product.categoryID_id=request.POST.get('categoryName')
    product.brandID_id=request.POST.get('brandName')
    product.save()
    messages.success(request, "Product Added Successfully")
    return redirect('/products')
def updateView(request,pk):
    categories=Categories.objects.raw('SELECT * FROM shopello_categories WHERE status IS NULL')
    brands=Brands.objects.raw('SELECT * FROM shopello_brands WHERE status IS NULL')
    product=Products.objects.get(id=pk)
    return render(request,'products/edit.html',{'product':product,'categories':categories,'brands':brands})
def update(request,pk):
    product=Products.objects.get(id=pk)
    product.productName=request.POST.get('productName')
    if request.FILES.get('productImage')==None:
        product.productImages=request.POST.get('image')
    else:
        product.productImages=request.FILES.get('productImage')
    product.price=request.POST.get('price')
    product.description=request.POST.get('description')
    product.color=request.POST.get('color')
    product.size=request.POST.get('size')
    product.etaDate=request.POST.get('etaDate')
    product.categoryID_id=request.POST.get('categoryName')
    product.brandID_id=request.POST.get('brandName')
    product.status=request.POST.get('status')
    product.save()
    messages.success(request,"Product Update Successfully")
    return redirect('/products')
def delete(request, pk):
    product=Products.objects.get(id=pk)
    product.status="deleted"
    product.save()
    messages.success(request,"Product Deleted Successfully")
    return redirect('/products')
def storeCategoryAtProduct(request):
    if request.method == "POST":
        categoryName = request.POST.get('categoryName')
        subCategoryId = request.POST.get('subCategoryName')
        if categoryName:
            category = Categories()
            category.categoryName = categoryName
            if subCategoryId:
                try:
                    category.subCategoryID_id = subCategoryId  # adjust if your FK field is named differently
                except:
                    pass
            category.save()
            messages.success(request, "Category created successfully!")
        else:
            messages.error(request, "Category name cannot be empty.")
        return redirect("createProduct")  # make sure this URL name exists
    return redirect("createProduct")
