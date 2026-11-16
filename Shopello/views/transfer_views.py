from django.shortcuts import render, redirect
from ..models import Transfers, TransferDetails, Centers, Products
from django.contrib import messages
from django.contrib.auth.decorators import login_required
def create(request):
    centers=Centers.objects.raw('SELECT * FROM shopello_centers WHERE status != "deleted"')
    products=Products.objects.raw('SELECT * FROM shopello_products WHERE status IS NULL')
    return render(request,'transfers/create.html',{'centers':centers,'products':products})
def store(request):
    transfer=Transfers()
    transferDetail=TransferDetails()
    data=request.POST
    transfer.transferNo=data.get('transferNo')
    transfer.fromcenterID_id=data.get('fromCenter')
    transfer.tocenterID_id=data.get('toCenter')
    transfer.transferDate=data.get('transferDate')
    transfer.note=data.get('note')
    transfer.save()
    i=1
    x=True
    while x:
        try:
            productName="{}{}{}".format('rows[',i,'][productName]')
            qty="{}{}{}".format('rows[',i,'][qty]')
            if data.get(qty)!=None:
                transferDetail.quantity=data.get(qty)
                transferDetail.transferID_id=transfer.pk
                transferDetail.productID_id=data.get(productName)
                transferDetail.save()
                i+=1
            else:
                x=False
                print("fail")
        except:
            import traceback
            print(traceback.format_exc())
            x=False
    messages.success(request,'Transfer added successfully')
    return redirect('/transfers')
def index(request):
    transfers=Transfers.objects.raw('SELECT * FROM shopello_transfers As S JOIN shopello_centers AS C2 ON S.fromcenterID_id=C2.id AND S.tocenterID_id=C2.id WHERE S.status IS NULL')
    return render(request,'transfers/index.html',{'transfers':transfers})
def updateView(request,pk):
    centers=Centers.objects.raw('SELECT * FROM shopello_centers WHERE status != "deleted"')
    transferQuery="{}{}{}".format('SELECT * FROM shopello_transferDetails AS S JOIN shopello_products AS P ON S.productID_id=P.id WHERE S.transferID_id=',pk,' AND S.status IS NULL')
    transferDetails=TransferDetails.objects.raw(transferQuery)
    transfer=Transfers.objects.get(id=pk)
    return render(request,'transfers/edit.html',{'transfer':transfer,'centers':centers,'transferDetails':transferDetails})
def update(request,pk):
    transfer=Transfers.objects.get(id=pk)
    transfer.transferNo=request.POST.get('transferNo')
    transfer.fromcenterID_id=request.POST.get('fromCenter')
    transfer.tocenterID_id=request.POST.get('toCenter')
    transfer.transferDate=request.POST.get('transferDate')
    transfer.note=request.POST.get('note')
    transfer.save()
    messages.success(request,'Transfer Update Successfully')
    return redirect('/transfers')
def delete(request,pk):
    transfer=Transfers.objects.get(id=pk)
    transfer.status="deleted"
    transfer.save()
    messages.success(request,'Transfer Deleted Successfully')
    return redirect('/transfers')