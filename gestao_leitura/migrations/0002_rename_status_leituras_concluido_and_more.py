# Generated by Django 4.1 on 2022-09-06 00:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_leitura', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='leituras',
            old_name='status',
            new_name='Concluido',
        ),
        migrations.RenameField(
            model_name='leituras',
            old_name='categoria',
            new_name='genero',
        ),
    ]
