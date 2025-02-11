from django.shortcuts import render, redirect
from .forms import LoginForm

# Create your views here.

def login_sin_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('inicio')
    else:
        form = LoginForm()
    return render(request, 'autenticacio/login.html', {'form': form})

def login_con_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return redirect('inicio')
    else:
        form = LoginForm()
    return render(request, 'autenticacio/login.html', {'form': form})

def inicio(request):
    return render(request, 'autenticacio/inicio.html')
