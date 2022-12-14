# Generated by Django 4.1 on 2022-09-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestao_leitura', '0003_remove_leituras_concluido_leituras_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leituras',
            name='genero',
            field=models.CharField(choices=[('Fantasia', 'Fantasia'), ('Ficção científica', 'Ficção científica'), ('Distopia', 'Distopia'), ('Ação e aventura', 'Ação e aventura'), ('Horror', 'Horror'), ('Thriller e Suspense', 'Thriller e Suspense')], default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='leituras',
            name='status',
            field=models.CharField(choices=[('Não lido', 'Não lido'), ('Concluido', 'Concluido')], default=False, max_length=50),
        ),
    ]
