# Generated by Django 3.2.4 on 2021-06-25 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_funcionario_imagem'),
    ]

    operations = [
        migrations.CreateModel(
            name='Recurso',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criacao', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualizado')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('nome', models.CharField(max_length=100, verbose_name='Nome')),
                ('descricao', models.TextField(max_length=200, verbose_name='Descrição')),
                ('icone', models.CharField(choices=[('lni-leaf"', 'Pluma'), ('lni-laptop-phone', 'Multi-Plataforma'), ('lni-support', 'Suporte'), ('lni-lock', 'Segurança'), ('lni-bolt', 'Velocidade'), ('lni-coffee-cup', 'Cafe Em Paz')], max_length=50, verbose_name='Icone')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]