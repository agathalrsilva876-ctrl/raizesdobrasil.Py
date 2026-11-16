
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.db import transaction
from .forms import ArtesaoForm
from .models import Artesao
from django.contrib.auth.decorators import login_required
from .forms import EditarArtesaoForm
from django.contrib.auth import login


def regioes(request):
    return render(request, 'artesaos/regiao.html')


def cadastrar_artesao(request):
    if request.method == 'POST':
        form = ArtesaoForm(request.POST)

        if form.is_valid():

            with transaction.atomic():

                email = form.cleaned_data['email']
                senha = form.cleaned_data['senha']

                usuario = User.objects.create_user(
                    username=email,
                    email=email,
                    password=senha
                )

                artesao = form.save(commit=False)
                artesao.usuario = usuario
                artesao.save()
                form.save_m2m()

            login(request, usuario)
            return redirect(
                'artesaos:cadastro_sucesso',
                artesao_id=artesao.id
            )

    else:
        form = ArtesaoForm()

    return render(
        request,
        'artesaos/cadastro.html',
        {'form': form}
    )


@login_required(login_url='usuarios:login')
def cadastro_sucesso(request, artesao_id):
    artesao = get_object_or_404(
        Artesao,
        id=artesao_id,
        usuario=request.user
    )

    return render(
        request,
        'artesaos/cadastro_sucesso.html',
        {'artesao': artesao}
    )

@login_required(login_url='usuarios:login')
def cadastro_sem_produtos(request, artesao_id):
    artesao = get_object_or_404(
        Artesao,
        id=artesao_id,
        usuario=request.user
    )

    return render(
        request,
        'artesaos/cadastro_sem_produtos.html',
        {'artesao': artesao}
    )
@login_required(login_url='usuarios:login')
def editar_perfil(request):
    artesao = get_object_or_404(
        Artesao,
        usuario=request.user
    )

    if request.method == 'POST':
        form = EditarArtesaoForm(
            request.POST,
            instance=artesao
        )

        if form.is_valid():
            form.save()
            return redirect('core:dashboard_artesao')

    else:
        form = EditarArtesaoForm(instance=artesao)

    return render(
        request,
        'artesaos/editar_perfil.html',
        {
            'form': form,
            'artesao': artesao
        }
    )
