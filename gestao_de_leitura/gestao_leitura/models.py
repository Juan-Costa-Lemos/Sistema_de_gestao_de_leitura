from wsgiref.validate import validator
from django.db import models

class Leituras(models.Model):
    STATUS_CHOICES = (
        ("N", "Não lido"),
        ("L", "Lendo"),
        ("C", "Concluido")
    )
    GENERO_CHOICES = (
        ("F","Fantasia"), 
        ("FC","Ficção científica"),
        ("D","Distopia" ),
        ("AV","Ação e aventura"),
        ("H","Horror"),
        ("TS","Thriller e Suspense")
    )
    livro = models.CharField(max_length=50)
    genero = models.CharField(max_length=50,default=False, choices=GENERO_CHOICES, blank=False, null=False)
    resenha = models.TextField(max_length=256)
    status = models.CharField(max_length=50,default=False, choices=STATUS_CHOICES, blank=False, null=False)
    dataInicio = models.DateField()
    dataTermino = models.DateField()
    