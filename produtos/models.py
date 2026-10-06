from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    artesao = models.CharField(max_length=100)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    regiao = models.CharField(max_length=50)
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome