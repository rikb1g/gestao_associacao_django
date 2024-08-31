from django.urls import path
from .views import ListSalarios, CreateSalarios, eliminar_salario, GetFuncionarioSalario

urlpatterns = [
  path("", CreateSalarios.as_view(), name="salarios_create"),
  path("salariosList", ListSalarios.as_view(), name="salarios_list"),
  path("eliminar/<int:pk>/", eliminar_salario, name="salarios_delete"),
  path('getFuncionarioSalario', GetFuncionarioSalario.as_view(), name='get_funcionario_salario'),

]