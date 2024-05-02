from django.urls import path
from .views import ListSalarios, CreateSalarios

urlpatterns = [
  path("", CreateSalarios.as_view(), name="salarios_create"),
  path("salariosList", ListSalarios.as_view(), name="salarios_list"),


]