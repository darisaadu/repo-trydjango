from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm
from django.contrib.auth import login, logout, authenticate



# Create your views here.

def login_view(request, *args, **kwargs):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')

        user = authenticate(username=username, password=password)
        if user == None:
            return redirect('/login')

        login(request, user)
        return redirect('/')


    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('/login')

def register_view(request, *args, **kwargs):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        form_obj = form.save()
        form_obj.is_actived = False
        form_obj.save()
        password = form.cleaned_data.get('password')
        form_obj.set_password(password)
        form_obj.save()
        return redirect('/login')
    return render(request, 'account/register.html', {'form': form})