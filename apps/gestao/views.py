from typing import Any
import datetime
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView,CreateView, DetailView
from .models import Despesas, TipoDespesa, Entradas, TipoEntrada
from .forms import FormDespesas, FormEntradas


class DespesasList(ListView):
    model = Despesas
    context_object_name = 'despesas_list'

    def get_queryset(self):
        escola = self.request.user.utilizador.escola
        ano_selecionado = self.request.GET.get('ano')
        mes_selecionado = self.request.GET.get('mes')
        mes_atual = datetime.datetime.now().month
        ano_atual = datetime.datetime.now().year
        pesquisa = self.request.GET.get('search')

        if pesquisa:
            return Despesas.objects.filter(descricao__icontains= pesquisa, escola= escola)
            
        else :
            try:
                if mes_selecionado is None:
                    mes_selecionado = mes_atual
                    ano_selecionado = ano_atual

                elif mes_selecionado == "Setembro":
                    mes_selecionado = 9
                    ano_selecionado = ano_selecionado           
                elif mes_selecionado == "Outubro":
                    mes_selecionado = 10
                    ano_selecionado = ano_selecionado
                elif mes_selecionado == "Novembro":
                    mes_selecionado = 11
                    ano_selecionado = ano_selecionado
                elif mes_selecionado == "Dezembro":
                    mes_selecionado = 12
                    ano_selecionado = ano_selecionado
                else:
                    mes_selecionado = meses_portugueses.index(mes_selecionado) + 1
                    ano_int = int(ano_selecionado) + 1
                    ano_selecionado = str(ano_int)
            except:
                pass
            
            return Despesas.objects.filter(escola= escola, data__month=mes_selecionado, data__year=ano_selecionado)
            
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        ano_inicial = 2023
        anos_letivos = range(ano_inicial, ano_inicial +10)
        context['anos_letivos'] = anos_letivos
        context['meses'] = MESES
        mes_get = self.request.GET.get('mes')
        ano_get = self.request.GET.get('ano')

        mes_ = mes_selcionado(mes_get)
        ano_ =ano_selecionado(mes_get,ano_get)

        escola = self.request.user.utilizador.escola
        context['total_despesa_mensal'] = Despesas.total_despesa_mensal(escola,mes_,ano_)
        context['total_despesa'] = Despesas.total_despesa(escola)

        return context
    


class EntradasList(ListView):
    model = Entradas
    context_object_name = 'entradas_list'

    def get_queryset(self):
        escola = self.request.user.utilizador.escola
        ano_selecionado = self.request.GET.get('ano')
        mes_selecionado = self.request.GET.get('mes')
        mes_atual = datetime.datetime.now().month
        ano_atual = datetime.datetime.now().year
        pesquisa = self.request.GET.get('search')


        if pesquisa:
            return Entradas.objects.filter(nome__icontains=pesquisa, escola = escola)
        else:
            try:
                if mes_selecionado is None:
                    mes_selecionado = mes_atual
                    ano_selecionado = ano_atual

                elif mes_selecionado == "Setembro":
                    mes_selecionado = 9
                    ano_selecionado = ano_selecionado           
                elif mes_selecionado == "Outubro":
                    mes_selecionado = 10
                    ano_selecionado = ano_selecionado
                elif mes_selecionado == "Novembro":
                    mes_selecionado = 11
                    ano_selecionado = ano_selecionado
                elif mes_selecionado == "Dezembro":
                    mes_selecionado = 12
                    ano_selecionado = ano_selecionado
                else:
                    mes_selecionado = meses_portugueses.index(mes_selecionado) + 1
                    ano_int = int(ano_selecionado) + 1
                    ano_selecionado = str(ano_int)
            except: 
                pass
            return Entradas.objects.filter(escola= escola, data__month= mes_selecionado, data__year= ano_selecionado)
        
        
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context= super().get_context_data(**kwargs)
        ano_inicial = 2023
        anos_letivos = range(ano_inicial, ano_inicial + 10)
        context['anos_letivos'] = anos_letivos
        context['meses'] = MESES
        mes_get = self.request.GET.get('mes')
        ano_get = self.request.GET.get('ano')
        
        mes_ = mes_selcionado(mes_get)
        ano_ = ano_selecionado(mes_get, ano_get)
        escola = self.request.user.utilizador.escola

        context['total_entrada_mensal'] = Entradas.total_receita_mensal(escola,mes_,ano_)

        context['total_entradas'] = Entradas.total_receita(escola)
 
        return context



meses_ano_letivo_ano_atual = ["Setembro", "Outubro","Novembro", "Dezembro"]

MESES = ("Setembro", "Outubro","Novembro", "Dezembro", "Janeiro","Fevereiro","Março","Abril",
         "Maio", "Junho","Julho","Agosto")
        
meses_portugueses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

class DespesaCreate(CreateView):
    model = Despesas
    form_class = FormDespesas
    template_name = 'despesas_form.html'

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        despesa = form.save(commit=False)
        despesa.escola = self.request.user.utilizador.escola
        despesa.creator = self.request.user.utilizador
        despesa.save()
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
    def get_absolute_url(self):
        return reverse_lazy('despesas_list')
    

class DespesaEdit(UpdateView):
    model = Despesas
    form_class = FormDespesas
    template_name = 'despesas_form.html'
    success_url = reverse_lazy('despesas_list')

    

    
class EntradaCreate(CreateView):
    model = Entradas
    form_class = FormEntradas
    template_name = 'entradas_form.html'
    success_url = reverse_lazy('entradas_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        entrada = form.save(commit=False)
        entrada.escola = self.request.user.utilizador.escola
        entrada.creator = self.request.user.utilizador
        entrada.save()
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
    def get_absolute_url(self):
        return reverse_lazy('entradas_list')
    
class EntradaEdit(UpdateView):
    model = Entradas
    form_class = FormEntradas
    template_name = 'entradas_form.html'
    success_url = reverse_lazy('entradas_list')

def eliminar_entrada(request, pk):
    entrada = get_object_or_404(Entradas, pk=pk)
    entrada.delete()
    return redirect('entradas_list')

class TipoDespesaCreate(CreateView):
    model = TipoDespesa
    fields = ['nome']
    success_url = reverse_lazy('despesas_list')



    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        tipo = form.save(commit=False)
        tipo.escola = self.request.user.utilizador.escola
        tipo.creator = self.request.user
        tipo.save()
        return super().form_valid(form)
    
    def get_absolute_url(self):
        return reverse_lazy('despesas_list')


def eliminar_despesa(request, pk):
    despesa = get_object_or_404(Despesas,pk=pk)
    despesa.delete()
    return redirect('despesas_list')


class TiposDespesaList(ListView):
    model = TipoDespesa
    context_object_name = 'tipo_despesas'

    def get_queryset(self):
        escola = self.request.user.utilizador.escola
        return TipoDespesa.objects.filter(escola= escola)


def eliminar_tipos_Despesa(request, pk):
    tipo = get_object_or_404(TipoDespesa, pk=pk)
    tipo.delete()
    return redirect('tipo_despesas_list')


class TiposDespesaEdit(UpdateView):
    model = TipoDespesa
    fields = ['nome']
    success_url = reverse_lazy('tipo_despesas_list')


class TipoEntradaCreate(CreateView):
    model = TipoEntrada
    fields = ['nome']
    success_url = reverse_lazy('entradas_list')

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        tipo = form.save(commit=False)
        tipo.escola = self.request.user.utilizador.escola
        tipo.save()
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)

    def get_success_url(self) -> str:
        return reverse_lazy('entradas_list')

class TipoEntradaList(ListView):
    model = TipoEntrada
    context_object_name = 'tipo_entrada_list'

    def get_queryset(self) -> QuerySet[Any]:
        escola = self.request.user.utilizador.escola
        return TipoEntrada.objects.filter(escola=escola)
    

class TipoEntradaEdit(UpdateView):
    model = TipoEntrada
    fields = ['nome']
    success_url = reverse_lazy('tipo_entradas_list')


def tipo_entradas_delete(request, pk):
    tipo = get_object_or_404(TipoEntrada, pk =pk)
    tipo.delete()
    return redirect('tipo_entradas_list')







def mes_selcionado(mes):
    mes_atual = datetime.datetime.now().month
    mes_selcionado = mes_atual
    try:
        if mes is None:
            mes_selcionado = mes_atual
        else:
            mes_selcionado = meses_portugueses.index(mes) +1
        
    except: 
        pass
    
    return mes_selcionado

def ano_selecionado(mes,ano):
   
    ano_atual = datetime.datetime.now().year
    mes_atual = datetime.datetime.now().month
    
    ano_selecionado = ano_atual
    try:
        if mes or ano is None:
            if mes_atual in ["Setembro", "Outubro","Novembro", "Dezembro"]:
                ano_selecionado= str(ano_atual)
            else:
                ano_selecionado = str(ano_atual)
        elif mes in ["Setembro", "Outubro","Novembro", "Dezembro"]:
            ano_selecionado = ano 
        else:
            ano_selecionado = ano +1
    except:
        pass

    return ano_selecionado


