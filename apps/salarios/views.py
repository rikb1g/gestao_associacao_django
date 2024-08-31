from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from django.views.generic import ListView, CreateView
from .models import Salarios
from .forms import FormSalarios
from apps.funcionarios.models import Funcionario
# Create your views here.


class ListSalarios(ListView):
    model = Salarios
    context_object_name = "Salarios_list"

    def get_queryset(self) -> QuerySet[Any]:
        escola = self.request.user.utilizador.escola
        return Salarios.objects.filter() 



class CreateSalarios(CreateView):
    model = Salarios
    form_class = FormSalarios

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        salarios = form.save()
        salarios.creator = self.request.user.utilizador
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['escola'] = self.request.user.utilizador.escola
        return kwargs


def eliminar_salario(request,pk):
    salario_eliminar = get_object_or_404(Salarios, pk=pk)
    salario_eliminar.delete()

    return redirect("salarios_list")


class GetFuncionarioSalario(View):
    def get(self, request, *args, **kwargs):
        funcionario_id = request.GET.get('funcionario_id')
        if funcionario_id:
            try:
                funcionario = Funcionario.objects.get(id=funcionario_id)
                salario = funcionario.salario  # Assumindo que o campo salário existe no modelo Funcionario
                return JsonResponse({'salario': salario})
            except Funcionario.DoesNotExist:
                return JsonResponse({'salario': None})
        return JsonResponse({'salario': None})