from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView
from .models import Funcionario,EscalaoIRS

# Create your views here.



class CriarFuncionario(CreateView):
    model = Funcionario
    fields = ['nome', 'salario', 'salario', 'horas_contrato','funcao','irs','iban','duodecimos']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        funcionario = form.save(commit=False)
        funcionario.escola = self.request.user.utilizador.escola
        funcionario.save()
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
    

class ListFuncionario(ListView):
    model = Funcionario
    context_object_name = 'funcionario_list'
    

    def get_queryset(self) -> QuerySet[Any]:
        escola = self.request.user.utilizador.escola
        query = self.request.GET.get('queryfuncionario')
        if query:
            return Funcionario.objects.filter(nome__icontains=query, escola= escola)
        else:    
            return Funcionario.objects.filter(escola=escola)
        

def eliminar_funcionario(request, pk):
    funcionario_eliminar = get_object_or_404(Funcionario, pk=pk)
    funcionario_eliminar.delete()
    return redirect('funcionarios_list')

class UpdateFuncionario(UpdateView):
    model = Funcionario
    fields = ['nome', 'salario', 'salario', 'horas_contrato','funcao','irs']
    success_url = reverse_lazy('funcionarios_list')



class ListEscalaoIRS(ListView):
    model = EscalaoIRS
    context_object_name = "escaloes_irs"

    def get_queryset(self) -> QuerySet[Any]:
        return super().get_queryset()
    
class CriarEscalaoIRS(CreateView):
    model = EscalaoIRS
    fields = ['nome']

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        escalao = form.save()
        escalao.creator = self.request.user.utilizador
        escalao.save()
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
