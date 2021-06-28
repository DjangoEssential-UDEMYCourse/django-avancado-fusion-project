# Generated by Django 3.2.4 on 2021-06-28 14:08

import core.models
from django.db import migrations
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_comentario_comentario'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='imagem',
            field=stdimage.models.StdImageField(default='', upload_to=core.models.get_file_path, verbose_name='Imagem'),
        ),
    ]