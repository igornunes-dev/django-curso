# Generated by Django 5.1.4 on 2025-01-21 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_features'),
    ]

    operations = [
        migrations.AlterField(
            model_name='features',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni lni-bell-1', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=14, verbose_name='Icone'),
        ),
        migrations.AlterField(
            model_name='service',
            name='icone',
            field=models.CharField(choices=[('lni-cog', 'Engrenagem'), ('lni lni-bell-1', 'Gráfico'), ('lni-users', 'Usuários'), ('lni-layers', 'Design'), ('lni-mobile', 'Mobile'), ('lni-rocket', 'Foguete')], max_length=14, verbose_name='Icone'),
        ),
    ]
