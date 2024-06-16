from django.urls import path
from .views import ListSalarios, CreateSalarios, eliminar_salario

urlpatterns = [
  path("", CreateSalarios.as_view(), name="salarios_create"),
  path("salariosList", ListSalarios.as_view(), name="salarios_list"),
  path("eliminar/<int:pk>/", eliminar_salario, name="salarios_delete"),

]