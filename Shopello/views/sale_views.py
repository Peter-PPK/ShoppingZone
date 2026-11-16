from django.shortcuts import render, redirect
from ..models import Sales,SaleDetails,Centers,Products,Customers
from django.contrib import messages
def create(request):
    centers=Centers.objects.raw('SELECT * FROM shopello_centers WHERE status != "deleted')
    customers=Customers.objects.raw('SELECT * FROM shopello_customers WHERE status IS NULL')
    products=Products.objects.raw('SELECT * FROM shopello_products WHERE status IS NULL')
    return render(request,'sales/create.html',{'centers':centers,'customers':customers,'products':products})
def store(request):
    sale=Sales()
    saleDetail=SaleDetails()
    data=request.POST
    sale.saleNo=data.get('saleNo')
    sale.tAmount=data.get('amount')
    sale.centerID_id=data.get('centerName')
    sale.customerID_id=data.get('customerName')
    sale.discount=data.get('discount')
    sale.tax=data.get('tax')
    sale.balance=data.get('balance')
    sale.paid=data.get('paid')
    sale.credit=data.get('credit')
    sale.saleDate=data.get('saleDate')
    sale.note=data.get('note')
    sale.save()
    i=1
    x=True
    while x:
        try:
            productName="{}{}{}".format('rows[',i,'][productName]')
            saleTypeName="{}{}{}".format('rows[',i,'][saleTypeName]')
            qty="{}{}{}".format('rows[',i,'][qty]')
            price="{}{}{}".format('rows[',i,'][price]')
            amount="{}{}{}".format('rows[',i,'][amount]')
            if data.get(qty)!=None:
                saleDetail.quantity=data.get(qty)
                saleDetail.total=data.get(amount)
                saleDetail.saleType=data.get(saleTypeName)
                saleDetail.saleID_id=sale.pk
                saleDetail.productID_id=data.get(productName)
                saleDetail.save()
                i+=1
            else:
                x=False
                print("fail")
        except:
            import traceback
            print(traceback.format_exc())
            x=False
    messages.success(request,"Sale Added Successfully")
    return redirect('/sales')
def index(request):
    sales=Sales.objects.raw('SELECT * FROM shopello_sales As S JOIN shopello_customers AS C1 ON S.customerID_id=C1.id JOIN shopello_centers AS C2 ON S.centerID_id=C2.id WHERE S.status IS NULL')
    return render(request,'sales/index.html',{'sales':sales})
def updateView(request,pk):
    centers=Centers.objects.raw('SELECT * FROM shopello_centers WHERE status != "deleted"')
    customers=Customers.objects.raw('SELECT * FROM shopello_customers WHERE status IS NULL')
    saleQuery="{}{}{}".format('SELECT * FROM shopello_saleDetails AS S JOIN shopello_products AS P ON S.productID_id=P.id WHERE S.saleID_id=',pk,' AND S.status IS NULL')
    saleDetails=saleDetails.objects.raw(saleQuery)
    sale=Sales.objects.get(id=pk)
    return render(request,'sales/edit.html',{'sale':sale,'centers':centers,'customers':customers,'saleDetails':saleDetails})
def update(request,pk):
    sale=Sales.objects.get(id=pk)
    sale.saleNo=request.POST.get('saleNo')
    sale.centerID_id=request.POST.get('centerName')
    sale.customerID_id=request.POST.get('customerName')
    sale.saleDate=request.POST.get('saleDate')
    sale.note=request.POST.get('note')
    sale.save()
    messages.success(request,"Sale Update Successfully")
    return redirect('/sales')
def delete(request,pk):
    sale=Sales.objects.get(id=pk)
    sale.status="deleted"
    sale.save()
    messages.success(request,"Sale Deleted Successfully")
    return redirect('/sales')