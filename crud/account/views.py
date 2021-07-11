from account.models import UserInformation
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = UserInformation()
            profile.user = user
            profile.age = request.POST["age"]
            profile.address = request.POST["address"]
            profile.save()

            auth.login(request, user)
            return redirect('main')
        else:
            return render (request, 'signup.html', {'form': form})
    else:
        form = UserCreationForm()
        return render (request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth.login(request, user)
            return redirect('main')
        else:
            return render (request, 'login.html', {'form': form})
    else:
        form = AuthenticationForm()
        return render (request, 'login.html', {'form': form})

def logout(request):
    auth.logout(request)
    return redirect('main')