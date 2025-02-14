from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import Usuario

# Create your views here.

def login_sin_sesion(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(email=email, password=password)
                return redirect('inicio')
            except Usuario.DoesNotExist:
                form.add_error(None, 'Credenciales erróneas')
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
