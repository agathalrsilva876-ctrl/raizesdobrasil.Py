from django.db import models
from artesaos.models import Artesao


class Produto(models.Model):
    artesao = models.ForeignKey(
        Artesao,
        on_delete=models.CASCADE,
        related_name='produtos'
    )

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.nome


class FotoProduto(models.Model):
    produto = models.ForeignKey(
        Produto,
        on_delete=models.CASCADE,
        related_name='fotos'
    )

    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return f"Foto de {self.produto.nome}"

