from django.shortcuts import render
from produtos.models import Produto


def home(request):
    return render(request, 'core/index.html')


def quem_somos(request):
    return render(request, 'core/quem_somos.html')

def sudeste(request):
    return render(request, 'core/sudeste.html')
def dashboard(request):
    return render(request, 'usuarios/dashboard.html')
def dashboard_artesao(request):
    return render(request, 'usuarios/dashboard_artesao.html')
def meus_produtos(request):
    produtos = Produto.objects.all()

    return render(request, 'usuarios/meus_produtos.html', {
        'produtos': produtos
    })