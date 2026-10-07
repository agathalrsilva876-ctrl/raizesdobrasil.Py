from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArtesaoForm
from .models import Artesao


def regioes(request):
    return render(request, 'artesaos/regiao.html')


def cadastrar_artesao(request):
    if request.method == 'POST':
        form = ArtesaoForm(request.POST)

        if form.is_valid():
            artesao = form.save()

            return redirect(
                'artesaos:cadastro_sucesso',
                artesao_id=artesao.id
            )

        def cadastro_sem_produtos(request, artesao_id):
            artesao = get_object_or_404(
                Artesao,
                id=artesao_id
            )

            return render(
                request,
                'artesaos/cadastro_sem_produtos.html',
                {'artesao': artesao}
            )

    else:
        form = ArtesaoForm()

    return render(
        request,
        'artesaos/cadastro.html',
        {'form': form}
    )


def cadastro_sucesso(request, artesao_id):
    artesao = get_object_or_404(
        Artesao,
        id=artesao_id
    )

    return render(
        request,
        'artesaos/cadastro_sucesso.html',
        {'artesao': artesao}
    )
def cadastro_sem_produtos(request, artesao_id):
    artesao = get_object_or_404(
        Artesao,
        id=artesao_id
    )

    return render(
        request,
        'artesaos/cadastro_sem_produtos.html',
        {'artesao': artesao}
    )