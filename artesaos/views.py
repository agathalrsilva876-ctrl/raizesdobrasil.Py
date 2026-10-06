from django.shortcuts import render, redirect
from .forms import ArtesaoForm


def regioes(request):
    return render(request, 'artesaos/regiao.html')


def cadastrar_artesao(request):
    if request.method == 'POST':
        form = ArtesaoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('artesaos:cadastro_sucesso')
    else:
        form = ArtesaoForm()

    return render(request, 'artesaos/cadastro.html', {'form': form})


def cadastro_sucesso(request):
    return render(request, 'artesaos/cadastro_sucesso.html')