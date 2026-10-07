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
    ESTADOS = [
        ('AC', 'Acre'),
        ('AL', 'Alagoas'),
        ('AP', 'Amapá'),
        ('AM', 'Amazonas'),
        ('BA', 'Bahia'),
        ('CE', 'Ceará'),
        ('DF', 'Distrito Federal'),
        ('ES', 'Espírito Santo'),
        ('GO', 'Goiás'),
        ('MA', 'Maranhão'),
        ('MT', 'Mato Grosso'),
        ('MS', 'Mato Grosso do Sul'),
        ('MG', 'Minas Gerais'),
        ('PA', 'Pará'),
        ('PB', 'Paraíba'),
        ('PR', 'Paraná'),
        ('PE', 'Pernambuco'),
        ('PI', 'Piauí'),
        ('RJ', 'Rio de Janeiro'),
        ('RN', 'Rio Grande do Norte'),
        ('RS', 'Rio Grande do Sul'),
        ('RO', 'Rondônia'),
        ('RR', 'Roraima'),
        ('SC', 'Santa Catarina'),
        ('SP', 'São Paulo'),
        ('SE', 'Sergipe'),
        ('TO', 'Tocantins'),
    ]

    estado = models.CharField(
        max_length=2,
        choices=ESTADOS
    )
    cidade = models.CharField(max_length=100)
    regiao = models.CharField(max_length=20, choices=REGIOES)
    descricao = models.TextField()
    telefone = models.CharField(max_length=20)
    instagram = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nome_loja

