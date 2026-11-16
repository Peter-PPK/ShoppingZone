from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth import logout
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from ..forms import SignUpForm
def create(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect("userList")
    else:
        form = SignUpForm()
    return render(request, 'users/create.html', {'form': form})
def index(request):
    User=get_user_model()
    users=User.objects.raw('SELECT * FROM shopello_user WHERE status = ""')
    return render(request,'users/index.html',{'users':users})
def home(request):
    return render(request,"inc/home.html")
def updateView(request,pk):
    User=get_user_model()
    user=User.objects.get(id=pk)
    return render(request,"users/edit.html",{"user":user})
def update(request,pk):
    User=get_user_model()
    user=User.objects.get(id=pk)
    user.username=request.POST.get("username")
    user.userImage=request.FILES.get("userImage",False)
    user.email=request.POST.get("email")
    user.userType=request.POST.get("userType")
    user.save()
    messages.success(request,"User Update Successfully")
    return redirect("/users")
def delete(request,pk):
    User=get_user_model()
    user=User.objects.get(id=pk)
    user.status="deleted"
    user.save()
    messages.success(request,"User Deleted Successfully")
    return redirect("/users")