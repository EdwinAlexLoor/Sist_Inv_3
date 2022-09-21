from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.shortcuts import render, redirect

from .forms import UserCreationForm, RolForm, RolUsuarioForm

# Create your views here.

def crear_usuario(request):

    if request.method=="POST":
        form = UserCreationForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form=UserCreationForm()
    return render(request, "registration/signup.html", {'form_p':form})