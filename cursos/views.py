from django.views import generic
from django.contrib.postgres.search import TrigramSimilarity

from .models import Curso, Pacote

class IndexView(generic.ListView):
    #cursos_list = get_list_or_404(Curso)
    #return render(request, 'cursos/index.html', {'cursos_list': cursos_list})
    template_name = 'cursos/index.html'
    context_object_name = 'cursos_list'

    def get_queryset(self):
        return Curso.objects.all()
        '''return Curso.objects.annotate(
                similarity=TrigramSimilarity('titulo', 'tempora modi'),
            ).filter(similarity__gt=0.1).order_by('-similarity')'''

class DetailView(generic.DetailView):
    model = Curso
    template_name = 'cursos/detail.html'

#def detail(request, curso_id):
#    curso = get_object_or_404(Curso, pk=curso_id)
#    return render(request, 'cursos/detail.html', {'curso': curso})
