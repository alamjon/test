from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout, authenticate
from .models import Info
from .forms import Enterdata
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    if request.method == 'GET':
        return render(request,'html/home.html',{'homee':Enterdata})
    else:
        blog_create = Enterdata(request.POST['full_name'],request.POST['tel'],request.POST['products'],request.POST['summ'],request.POST['date'],request.POST['lifetime'])
        blog_create.save()
        return redirect('data')
@login_required    
def data(request):
    data = Info.objects.all()
    return render(request,'html/data_list.html',{'data':data})
def search(request):
    if request.method == 'GET':
        search = request.GET.get('search')
        sear = Info.objects.filter(first=search)
        return render(request,'html/search.html',{'sear':sear})
@login_required
def signup(request):
    if request.method == 'GET':
        user = UserCreationForm()
        return render(request,'html/signup.html',{'user':user})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('data')
            except IntegrityError:
                return render(request,'html/signup.html',{'user':UserCreationForm(),'error':'Username sizdan oldin band qilingan'})
        else:
            return render(request,'html/signup.html',{'user':UserCreationForm(),'error':'Sizning parolingiz bir xil emas'})
def signin(request):
    if request.method == 'GET':
        user = AuthenticationForm()
        return render(request,'html/signin.html',{'user':user})
    else:
        user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'html/signin.html',{'user':AuthenticationForm(),'error':"username yoki parol xato iltimos qytadan urunib ko'ring"})   
        else:
            login(request,user)
            return redirect('home')
@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

