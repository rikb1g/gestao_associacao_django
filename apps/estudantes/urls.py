from django.urls import path
from .views import (AlunoList,AlunoCreate,AlunoEdit, remover_aluno,AlunoDetail,AlunoHistoric,arquivar_aluno,renovar_maticula)

urlpatterns = [
    path('', AlunoList.as_view(), name='alunos_list'),
    path('novo', AlunoCreate.as_view(), name='aluno_new'),
    path('eliminar/<int:pk>/', remover_aluno,name='aluno_delete'),
    path('editar/<int:pk>/', AlunoEdit.as_view(),name='aluno_edit'),
    path('detalhe/<int:pk>/', AlunoDetail.as_view(),name='aluno_detail'),
    path('alunoHistoric', AlunoHistoric.as_view(),name='aluno_historic'),
    path('removerMatricula/<int:pk>/', arquivar_aluno,name='aluno_remove_registration'),
    path('renovarMatricula/<int:pk>/', renovar_maticula,name='aluno_renovar_matricula'),



]
