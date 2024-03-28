from django.urls import path
from .views import (AlunoList,AlunoCreate,AlunoEdit, remover_aluno)

urlpatterns = [
    path('', AlunoList.as_view(), name='alunos_list'),
    path('novo', AlunoCreate.as_view(), name='aluno_new'),
    path('eliminar/<int:pk>/', remover_aluno,name='aluno_delete'),
    path('editar/<int:pk>/', AlunoEdit.as_view(),name='aluno_edit'),


]
