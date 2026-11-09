from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProdutoForm
from .models import Produto, FotoProduto
from artesaos.models import Artesao



def cadastrar_produto(request, artesao_id):
    artesao = get_object_or_404(Artesao, id=artesao_id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        imagens = request.FILES.getlist('imagens')

        if form.is_valid():

            if len(imagens) == 0:
                form.add_error(
                    None,
                    'Adicione pelo menos 1 foto do produto.'
                )

            elif len(imagens) > 4:
                form.add_error(
                    None,
                    'Você pode adicionar no máximo 4 fotos.'
                )

            else:
                produto = form.save(commit=False)

                produto.artesao = artesao
                produto.cidade = artesao.cidade
                produto.estado = artesao.estado
                produto.regiao = artesao.regiao
                produto.imagem = imagens[0]

                produto.save()

                for imagem in imagens[1:]:
                    FotoProduto.objects.create(
                        produto=produto,
                        imagem=imagem
                    )

                return redirect(
                    'produtos:produto_cadastrado',
                    artesao_id=artesao.id
                )

    else:
        form = ProdutoForm()

    return render(
        request,
        'produtos/cadastro.html',
        {
            'form': form,
            'artesao': artesao
        }
    )



def produto_cadastrado(request, artesao_id):
    artesao = get_object_or_404(Artesao, id=artesao_id)

    return render(
        request,
        'produtos/cadastro_sucesso.html',
        {
            'artesao': artesao
        }
    )

def cadastrar_produto(request, artesao_id):
    artesao = get_object_or_404(Artesao, id=artesao_id)

    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        imagens = request.FILES.getlist('imagens')

        if form.is_valid():

            if len(imagens) == 0:
                form.add_error(
                    None,
                    'Adicione pelo menos 1 foto do produto.'
                )

            elif len(imagens) > 4:
                form.add_error(
                    None,
                    'Você pode adicionar no máximo 4 fotos.'
                )

            else:
                produto = form.save(commit=False)

                produto.artesao = artesao
                produto.cidade = artesao.cidade
                produto.estado = artesao.estado
                produto.regiao = artesao.regiao

                # A primeira foto será a imagem principal
                produto.imagem = imagens[0]

                produto.save()

                # Salva todas as fotos na galeria do produto
                for imagem in imagens:
                    FotoProduto.objects.create(
                        produto=produto,
                        imagem=imagem
                    )

                return redirect(
                    'produtos:produto_cadastrado',
                    artesao_id=artesao.id
                )

    else:
        form = ProdutoForm()

    return render(
        request,
        'produtos/cadastro.html',
        {
            'form': form,
            'artesao': artesao
        }
    )