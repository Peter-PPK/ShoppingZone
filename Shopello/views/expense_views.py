from django.shortcuts import render, redirect
from ..models import Expenses,Centers
from django.contrib import messages
def create(request):
    centers=Centers.objects.raw('SELECT * FROM shopello_centers WHERE status = "Open"')
    return render(request,'expenses/create.html',{'centers':centers})
def store(request):
    expense = Expenses()
    expense.expenseNo = request.POST.get('expenseNo')
    expense.centerID_id = request.POST.get('centerName')   # matches form name
    expense.paymentType = request.POST.get('paymentType')
    expense.expenseDate = request.POST.get('expenseDate')
    expense.amount = request.POST.get('amount')
    expense.approveBy = request.POST.get('approveBy')
    expense.note = request.POST.get('note')
    expense.save()
    messages.success(request, "Expense Added Successfully")
    return redirect('/expenses')   # better to redirect than re-render
def index(request):
    expenses = Expenses.objects.filter(status__isnull=True).select_related('centerID')
    return render(request, 'expenses/index.html', {'expenses': expenses})
def updateView(request,pk):
    centers=Centers.objects.all()
    expense=Expenses.objects.get(id=pk)
    return render(request,'expenses/edit.html',{'expense':expense,'centers':centers})
def update(request, pk):
    expense = Expenses.objects.get(id=pk)
    expense.expenseNo = request.POST.get('expenseNo')
    expense.centerID_id = request.POST.get('centerName')   # same fix here
    expense.paymentType = request.POST.get('paymentType')
    expense.expenseDate = request.POST.get('expenseDate')
    expense.amount = request.POST.get('amount')
    expense.approveBy = request.POST.get('approveBy')
    expense.note = request.POST.get('note')
    expense.save()
    messages.success(request, "Expense Updated Successfully")
    return redirect('/expenses')
def delete(request,pk):
    expense=Expenses.objects.get(id=pk)
    expense.status="deleted"
    expense.save()
    messages.success(request,"Expense Deleted Successfully")
    return redirect('/expenses')