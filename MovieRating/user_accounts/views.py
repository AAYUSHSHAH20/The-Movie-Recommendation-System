from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import UserCreateForm
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate
from django.db import IntegrityError
from movie.models import Movie
from django.contrib.auth.decorators import login_required
# Create your views here.

def signupaccount(request):
        if request.method == 'GET':
                return render(request,'signup.html',{'form':UserCreateForm})
        else:
                if request.POST['password1'] == request.POST['password2']:
                        try:
                                user = User.objects.create_user(
                                        request.POST['username'],
                                        password = request.POST['password1'],
                                      
                                )
                                user.save()
                                login(request,user)
                                return redirect('home')
                        except  IntegrityError:
                                return render(request,'signup.html',{'form':UserCreateForm,'error':'user is already taken'})
                else:
                        return render(request,'signup.html',{'form':UserCreateForm,'error':'password does not match'})


def logoutaccount(request):
        logout(request)
        return redirect('home')       

def loginaccount(request):
        if request.method == 'GET':
                return render(request,'login.html',{'form':AuthenticationForm})
        else:
                user = authenticate(request,
                    username = request.POST['username'],
                    password = request.POST['password']
                    )
                if user is None:
                        return render(request,'login.html',{'form':AuthenticationForm,'error':'username and password does not match'})
                else:
                        login(request,user)
                        return redirect('home')
                