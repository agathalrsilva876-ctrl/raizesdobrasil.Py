from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.http import require_POST


def login_usuario(request):
    if request.method == 'POST':
        email = request.POST.get('username')
        senha = request.POST.get('senha')

        usuario = authenticate(
            request,
            username=email,
            password=senha
        )

        if usuario is not None:
            login(request, usuario)
            return redirect('core:dashboard_artesao')

        messages.error(request, 'E-mail ou senha incorretos.')

    return render(request, 'usuarios/login.html')

@require_POST
def logout_usuario(request):
    logout(request)
    return redirect('usuarios:login')