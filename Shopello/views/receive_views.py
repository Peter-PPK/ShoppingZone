from django.shortcuts import render, redirect
from ..models import Receives, ReceiveDetails, Centers, Products
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def create(request):
    centers=Centers.objects.raw('SELECT * FROM shopello_centers WHERE status != "deleted"')
    products=Products.objects.raw('SELECT * FROM shopello_products WHERE status IS NULL')
    return render(request,'receives/create.html',{'centers':centers,'products':products})
def store(request):
    receive=Receives()
    receiveDetail=ReceiveDetails()
    data=request.POST
    receive.receiveNo=data.get('receiveNo')
    receive.centerID_id=data.get('centerName')
    receive.receiveDate=data.get('receiveDate')
    receive.note=data.get('note')
    receive.save()
    i=1
    x=True
    while x:
        try:
            productName="{}{}{}".format('rows[',i,'][productName]')
            qty="{}{}{}".format('rows[',i,'][qty]')
            if data.get(qty)!=None:
                receiveDetail.quantity=data.get(qty)
                receiveDetail.receiveID_id=receive.pk
                receiveDetail.productID_id=data.get(productName)
                receiveDetail.save()
                i+=1
            else:
                x=False
                print("fail")
        except:
            import traceback
            print(traceback.format_exc())
            x=False
    messages.success(request,'Receive added successfully')
    return redirect('/receives')
def index(request):
    receives=Receives.objects.raw('SELECT * FROM shopello_receives As S JOIN shopello_centers AS C2 ON S.centerID_id=C2.id WHERE S.status IS NULL')
    return render(request,'receives/index.html',{'receives':receives})
def updateView(request,pk):
    centers=Centers.objects.raw('SELECT * FROM shopello_centers WHERE status != "deleted"')
    receiveQuery="{}{}{}".format('SELECT * FROM shopello_receiveDetails AS S JOIN shopello_products AS P ON S.productID_id=P.id WHERE S.receiveID_id=',pk,' AND S.status IS NULL')
    receiveDetails=ReceiveDetails.objects.raw(receiveQuery)
    receive=Receives.objects.get(id=pk)
    return render(request,'receives/edit.html',{'receive':receive,'centers':centers,'receiveDetails':receiveDetails})
def update(request,pk):
    receive=Receives.objects.get(id=pk)
    receive.receiveNo=request.POST.get('receiveNo')
    receive.centerID_id=request.POST.get('centerName')
    receive.receiveDate=request.POST.get('receiveDate')
    receive.note=request.POST.get('note')
    receive.save()
    messages.success(request,'Receive Update Successfully')
    return redirect('/receives')
def delete(request,pk):
    receive=Receives.objects.get(id=pk)
    receive.status="deleted"
    receive.save()
    messages.success(request,'Receive Deleted Successfully')
    return redirect('/receives')