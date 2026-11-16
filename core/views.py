from django.shortcuts import render
from produtos.models import Produto
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required


def home(request):
    return render(request, 'core/index.html')


def quem_somos(request):
    return render(request, 'core/quem_somos.html')

def sudeste(request):
    return render(request, 'core/sudeste.html')
@staff_member_required(login_url='usuarios:login')
def dashboard(request):
    return render(request, 'usuarios/dashboard.html')




@login_required(login_url='usuarios:login')
def dashboard_artesao(request):
    produtos = Produto.objects.filter(
        artesao__usuario=request.user
    )

    total_produtos = produtos.count()
    produtos_recentes = produtos.order_by('-id')[:5]

    return render(
        request,
        'usuarios/dashboard_artesao.html',
        {
            'total_produtos': total_produtos,
            'produtos_recentes': produtos_recentes,
        }
    )




@login_required(login_url='usuarios:login')
def meus_produtos(request):
    produtos = Produto.objects.filter(
        artesao__usuario=request.user
    )

    return render(request, 'usuarios/meus_produtos.html', {
        'produtos': produtos
    })
