from django.urls import path
from .views import (EditEscola, CriarEscola, CreateMensalidade,AtividadesList,AtividadeNew,remover_atividade,
                    AtividadeEdit,MensalidadeList,MensaliadeEdit,remover_mensalidade, atualizar_mensalidade_aluno)

urlpatterns = [
    path("criarEscola",CriarEscola.as_view(), name= "create_escola"),
    path("editar/<int:pk>/", EditEscola.as_view(),name="update_escola"),
    path("novaMensalidade", CreateMensalidade.as_view(),name="criar_mensalide"),
    path('atividades',AtividadesList.as_view(),name='atividades_list'),
    path('novaAtividade/',AtividadeNew.as_view(),name='atividade_new'),
    path('removerAtividade/<int:pk>/',remover_atividade,name='atividade_delete'),
    path('editarAtividade/<int:pk>/',AtividadeEdit.as_view(),name='atividade_update'),
    path('mensalidade/',MensalidadeList.as_view(),name='mensalidade_list'),
    path('editarMensalidade/<int:pk>/',MensaliadeEdit.as_view(),name='mensalidade_base_update'),
    path('removerMensalidade/<int:pk>/',remover_mensalidade,name='mensalidade_remove'),
    path('atualizarMensalidadeAluno/<int:mensalidade_id>/',atualizar_mensalidade_aluno,name='atualizar_mensalidade_aluno'),

]