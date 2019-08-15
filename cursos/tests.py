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
        The detail view of a curso
        """
        curso_view = Curso.objects.create(titulo='Future test.')
        url = reverse('cursos:detail', args=(curso_view.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
