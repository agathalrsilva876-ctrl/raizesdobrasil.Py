from django.shortcuts import render
from produtos.models import Produto
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'core/index.html')


def quem_somos(request):
    return render(request, 'core/quem_somos.html')

def sudeste(request):
    return render(request, 'core/sudeste.html')
def dashboard(request):
    return render(request, 'usuarios/dashboard.html')

@login_required(login_url='usuarios:login')
def dashboard_artesao(request):
    return render(request, 'usuarios/dashboard_artesao.html')

@login_required(login_url='usuarios:login')
def meus_produtos(request):
    produtos = Produto.objects.filter(
        artesao__usuario=request.user
    )

    return render(request, 'usuarios/meus_produtos.html', {
        'produtos': produtos
    })
