import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('descricao', models.TextField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cidade', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=2)),
                ('regiao', models.CharField(max_length=50)),
                ('imagem', models.ImageField(upload_to='produtos/')),
            ],
        ),
        migrations.CreateModel(
            name='FotoProduto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagem', models.ImageField(upload_to='produtos/')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fotos', to='produtos.produto')),
            ],
        ),
    ]
