
from django.db import models
from artesaos.models import Artesao


class Produto(models.Model):

    STATUS_CHOICES = [
        ('publicado', 'Publicado'),
        ('em_analise', 'Em análise'),
    ]

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='publicado'
    )

    artesao = models.ForeignKey(
        Artesao,
        on_delete=models.CASCADE,
        related_name='produtos',
        null=True,
        blank=True
    )

    nome = models.CharField(max_length=100)
    descricao = models.TextField()
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    regiao = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='produtos/')

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
