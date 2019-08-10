from django.db import models
from sort_order_field import SortOrderField

class Apostila(models.Model):
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Curso(models.Model):
    titulo = models.CharField(max_length=255)

    def __str__(self):
        return self.titulo

class Aula(models.Model):
    titulo = models.CharField(max_length=255)
    apostilas = models.ManyToManyField(Apostila, blank=True, related_name='aulas', through='Pacote')
    curso = models.ForeignKey(Curso, blank=True, null=True, on_delete=None)

    def __str__(self):
        return self.titulo

class Pacote(models.Model):
    class Meta:
        ordering =  ('ordem',)

    apostila = models.ForeignKey(Apostila, on_delete=None)
    aula = models.ForeignKey(Aula, on_delete=None)
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.apostila.titulo
