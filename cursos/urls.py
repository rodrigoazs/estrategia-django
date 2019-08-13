from django.urls import path
from . import views

app_name = 'cursos'

urlpatterns = [
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
]
