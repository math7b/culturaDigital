from django.db import models
from django.contrib.auth.models import User


class Materia(models.Model):
    nome = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.nome

class Categoria(models.Model):
    tipo = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.tipo

class Tarefas(models.Model):
    nome = models.CharField(max_length=50)
    link = models.URLField()
    imagem = models.ImageField(blank=True, null=True, upload_to ='uploads/')
    descricao = models.CharField(max_length=200)
    materia = models.ForeignKey(Materia, on_delete=models.DO_NOTHING)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)
    publicado = models.BooleanField(default=False)
    usuario = models.ForeignKey(to=User, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name= 'Tarefa'

    def __str__(self):
        return self.nome
