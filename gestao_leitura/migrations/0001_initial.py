# Generated by Django 4.1 on 2022-09-05 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Leituras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('livro', models.CharField(max_length=50)),
                ('categoria', models.CharField(max_length=50)),
                ('resenha', models.TextField(max_length=256)),
                ('status', models.BooleanField(default=False)),
                ('dataInicio', models.DateField()),
                ('dataTermino', models.DateField()),
            ],
        ),
    ]
