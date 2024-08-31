from django.urls import path
from .views import ListFuncionario, eliminar_funcionario,CriarFuncionario, UpdateFuncionario,ListEscalaoIRS, CriarEscalaoIRS, DetailFuncionario, EndContratoFuncionario,HistoricFuncionario

urlpatterns = [
     path('', ListFuncionario.as_view(), name='funcionarios_list'),
     path('eliminar/<int:pk>/', eliminar_funcionario, name='eliminar_funcionario'),
     path('novo', CriarFuncionario.as_view(), name='novo_funcionario'),
     path('funcionarioUpdate/<int:pk>/', UpdateFuncionario.as_view(), name='update_funcionario'),
     path('escaloesIRS', ListEscalaoIRS.as_view(), name='escaloes_list'),
     path('detailFuncionario/<int:pk>/', DetailFuncionario.as_view(), name='detail_funcionario'),
     path('termoContrato/<int:pk>/', EndContratoFuncionario.as_view(), name='end_funcionario'),
     path('historicoFuncionario', HistoricFuncionario.as_view(), name='historic_funcionario'),
     

]
