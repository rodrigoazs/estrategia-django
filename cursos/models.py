from django.db import models

class Apostila(models.Model):
    titulo = models.CharField('Título', max_length=255)
    created_at = models.DateTimeField('Criação', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Atualização', auto_now=True, editable=False)

    def __str__(self):
        return self.titulo

class Curso(models.Model):
    titulo = models.CharField('Título', max_length=255)
    descricao = models.TextField('Descrição', max_length=500)
    imagem = models.ImageField(upload_to='static/images/cursos/%Y/%m', max_length=100)
    created_at = models.DateTimeField('Criação', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Atualização', auto_now=True, editable=False)

    def __str__(self):
        return self.titulo

class Aula(models.Model):
    titulo = models.CharField('Título', max_length=255)
    created_at = models.DateTimeField('Criação', auto_now_add=True, editable=False)
    updated_at = models.DateTimeField('Atualização', auto_now=True, editable=False)
    apostilas = models.ManyToManyField(Apostila, blank=True, related_name='aulas', through='Pacote')
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

    def apostila_list(self):
        return [ex.apostila for ex in Pacote.objects.filter(aula=self).order_by('ordem')]

class Pacote(models.Model):
    apostila = models.ForeignKey(Apostila, on_delete=models.CASCADE)
    aula = models.ForeignKey(Aula, on_delete=models.CASCADE)
    ordem = models.PositiveIntegerField(default=0, blank=False, null=False)

    def __str__(self):
        return self.apostila.titulo

    class Meta:
        ordering =  ['ordem']
