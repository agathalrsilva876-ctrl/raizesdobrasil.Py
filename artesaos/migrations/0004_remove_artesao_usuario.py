from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('artesaos', '0003_artesao_usuario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artesao',
            name='usuario',
        ),
    ]
