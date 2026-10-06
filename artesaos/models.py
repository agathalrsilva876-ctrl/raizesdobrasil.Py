from django.db import models

class Artesao(models.Model):
    REGIOES = [
        ('Norte', 'Norte'),
        ('Nordeste', 'Nordeste'),
        ('Centro-Oeste', 'Centro-Oeste'),
        ('Sudeste', 'Sudeste'),
        ('Sul', 'Sul'),
    ]

    nome = models.CharField(max_length=100)
    nome_loja = models.CharField(max_length=100)
    estado = models.CharField(max_length=50)
    cidade = models.CharField(max_length=100)
    regiao = models.CharField(max_length=20, choices=REGIOES)
    descricao = models.TextField()
    telefone = models.CharField(max_length=20)
    instagram = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome_loja

