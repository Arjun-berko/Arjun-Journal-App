from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from .models import Profile
from django.contrib import messages
from .forms import UserUpdateForm,ProfileUpdateForm
import os

def register(request):
    if request.method=="POST":
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            return redirect('login-view')
    else:
        form=UserRegisterForm()
    context={"form":form}
    return render(request,'users/registration.html',context)

@login_required()
def profile(request):
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.userprofile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'{request.user.username} profile picture, email and username have been updated!')
            return redirect("profile-view")

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.userprofile)
    context={"u_form":u_form,"p_form":p_form}
    return render(request,'users/profile.html',context)


