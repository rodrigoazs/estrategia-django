from django.test import TestCase
from django.urls import reverse
from .models import Curso, Aula, Apostila, Pacote

class CursoIndexViewTests(TestCase):
    def test_no_cursos(self):
        """
        Se não existir nenhum curso a mensagem
        "Sem cursos gratuitos disponíveis." é mostrada.
        """
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sem cursos gratuitos disponíveis.")
        self.assertQuerysetEqual(response.context['cursos_list'], [])

class CursoDetailViewTests(TestCase):
    def test_curso_detail_view(self):
        """
        Página detalhada de um curso.
        """
        curso_view = Curso.objects.create(titulo='Future test.',
                                          imagem='/static/images/cursos/2019/08/1.jpg')
        url = reverse('cursos:detail', args=(curso_view.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_no_curso_detail_view(self):
        """
        Página detalhada de um curso inexistente.
        """
        url = reverse('cursos:detail', args=(99999,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_curso_detail_view_no_aulas(self):
        """
        Página detalhada de um curso sem aulas.
        """
        curso_view = Curso.objects.create(titulo='Future test.',
                                          imagem='/static/images/cursos/2019/08/1.jpg')
        url = reverse('cursos:detail', args=(curso_view.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sem aulas adicionadas.")

    def test_curso_detail_view_no_apostilas(self):
        """
        Página detalhada de um curso com pelo menos uma aula
        sem apostilas.
        """
        curso_view = Curso.objects.create(titulo='Future test.',
                                          imagem='/static/images/cursos/2019/08/1.jpg')
        aula = Aula.objects.create(titulo='Aula test.', curso=curso_view)
        url = reverse('cursos:detail', args=(curso_view.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Sem apostilas adicionadas.")
