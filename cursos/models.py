from django.db import models

class Apostila(models.Model):
    titulo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.titulo

class Curso(models.Model):
    titulo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return self.titulo

class Aula(models.Model):
    titulo = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)
    apostilas = models.ManyToManyField(Apostila, blank=True, related_name='aulas', through='Pacote')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

class Pacote(models.Model):
    class Meta:
        ordering =  ('ordem',)

    apostila = models.ForeignKey(Apostila, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.apostila.titulo
