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
    if request.session.get('usuario_id'):
        return redirect('inicio')
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                usuario = Usuario.objects.get(email=email, password=password)
                request.session['usuario_id'] = usuario.id
                request.session['email'] = usuario.email
                return redirect('inicio')
            except Usuario.DoesNotExist:
                form.add_error(None, 'Credenciales erróneas')
    else:
        form = LoginForm()
    return render(request, 'autenticacio/login.html', {'form': form})

def inicio(request):
    usuario_id = request.session.get('usuario_id')
    if usuario_id:
        try:
            usuario = Usuario.objects.get(id=usuario_id)
            context = {
                'usuario': usuario,
                'esta_logueado': True
            }
            return render(request, 'autenticacio/inicio.html', context)
        except Usuario.DoesNotExist:
            del request.session['usuario_id']
            if 'email' in request.session:
                del request.session['email']
    return render(request, 'autenticacio/inicio.html', {'esta_logueado': False})

def logout(request):
    if 'usuario_id' in request.session:
        del request.session['usuario_id']
    if 'email' in request.session:
        del request.session['email']
    return redirect('login')
