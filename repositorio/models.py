from django.db import models
from django.contrib.postgres.fields import ArrayField

class Autor(models.Model):
    primeironome= models.CharField(max_length=200)
    ultimonome = models.CharField(max_length=200)
    foto = models.ImageField(upload_to="fotos/")

    def __str__(self):
        return self.primeironome


class Orientador(models.Model):
    primeironome = models.CharField(max_length=200)
    ultimonome = models.CharField(max_length=200)
    linkcurriculolattes= models.URLField()

    def __str__(self):
        return self.primeironome


class Curso(models.Model):

    MODALIDADE = (
        ('B', 'BACHARELADO'),
        ('L', 'LICENCIATURA'),
        ('T', 'TECNOLOGICO'),
    )

    nome = models.CharField(max_length=200)
    modalidade = models.CharField(choices=MODALIDADE, max_length=150)

    def __str__(self):
        return self.nome


class Tcc(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.ForeignKey(Autor, on_delete=models.PROTECT)
    orientador = models.ForeignKey(Orientador, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    anododocumento = models.IntegerField()
    resumo = models.TextField()
    arquivododocumento = models.FileField(upload_to="documentos/")
    palavras_chave = ArrayField(models.CharField(max_length=200), blank=True)

    def __str__(self):
        return self.titulo

