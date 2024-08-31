from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib import messages
from django.db.models import ProtectedError
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView,CreateView,UpdateView, DeleteView, DetailView
from .models import Funcionario,EscalaoIRS
from .forms import FuncionarioForm, FormTermoContrato

# Create your views here.



class CriarFuncionario(CreateView):
    model = Funcionario
    form_class = FuncionarioForm

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
            return Funcionario.objects.filter(nome__icontains=query, escola= escola,ativo=True)
        else:    
            return Funcionario.objects.filter(escola=escola, ativo=True)

class HistoricFuncionario(ListView):
    model = Funcionario
    context_object_name = "historic_funcionario_list"

    def get_queryset(self) -> QuerySet[Any]:
        escola = self.request.user.utilizador.escola
        query = self.request.GET.get('queryfuncionario')
        if query:
            return Funcionario.objects.filter(nome__icontains=query, escola= escola,ativo=False)
        
        else:
            return Funcionario.objects.filter(escola= escola, ativo=False)
        
        

def eliminar_funcionario(request, pk):
    funcionario_eliminar = get_object_or_404(Funcionario, pk=pk)
    try:
        funcionario_eliminar.delete()
        return redirect('funcionarios_list')
    except ProtectedError:
        messages.error(request, 'Não é possível excluir este funcionário porque existem salários processados. Deves terminar o contrato do mesmo!')
        return redirect('funcionarios_list')


class UpdateFuncionario(UpdateView):
    model = Funcionario
    form_class = FuncionarioForm
    success_url = reverse_lazy('funcionarios_list')

    
class EndContratoFuncionario(UpdateView):
    model = Funcionario
    form_class = FormTermoContrato
    success_url = reverse_lazy('funcionarios_list')
    
    def form_valid(self, form: FormTermoContrato) -> HttpResponse:
        funcionario = form.save(commit=False)
        funcionario.ativo = False
        funcionario.save()
        return super().form_valid(form)



class DetailFuncionario(DetailView):
    model = Funcionario
    context_object_name = 'detailFuncionario'
    


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


