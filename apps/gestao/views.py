from typing import Any
import datetime
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView,CreateView, DetailView
from .models import Despesas, TipoDespesa
from .forms import FormDespesas


class DespesasList(ListView):
    model = Despesas
    context_object_name = 'despesas_list'

    def get_queryset(self):
        escola = self.request.user.utilizador.escola
        ano_selecionado = self.request.GET.get('ano')
        mes_selecionado = self.request.GET.get('mes')
        mes_atual = datetime.datetime.now().month
        ano_atual = datetime.datetime.now().year

        try:
            if mes_selecionado is None:
                mes_selecionado = meses_portugueses[mes_atual-1]
                ano_selecionado = ano_atual

            elif mes_selecionado == "Setembro":
                mes_selecionado = mes_selecionado
                ano_selecionado = ano_selecionado           
            elif mes_selecionado == "Outubro":
                ano_selecionado = ano_selecionado
            elif mes_selecionado == "Novembro":
                ano_selecionado = ano_selecionado
            elif mes_selecionado == "Dezembro":
                ano_selecionado = ano_selecionado
            else:
                ano_int = int(ano_selecionado) + 1
                ano_selecionado = str(ano_int)
        except:
            pass
        # falta logica 
        if ano_selecionado and mes_selecionado:
            return Despesas.objects.filter(escola= escola)
        else :
            return Despesas.objects.filter(escola = escola)
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        ano_inicial = 2023
        anos_letivos = range(ano_inicial, ano_inicial +10)
        context['anos_letivos'] = anos_letivos
        context['meses'] = MESES
        escola = self.request.user.utilizador.escola
        #context['total_despesa_mensal'] = Despesas.total_despesa_mensal(escola)
        context['total_despesa'] = Despesas.total_despesa(escola)

        return context
    


MESES = ("Setembro", "Outubro","Novembro", "Dezembro", "Janeiro","Fevereiro","Março","Abril",
         "Maio", "Junho","Julho","Agosto")
        
meses_portugueses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def DespesaCreate(request):
    form = FormDespesas()
    if request.method == 'POST':
        form = FormDespesas(request.POST, request.FILES)

        if form.is_valid():
            despesa = form.save(commit=False)
            despesa.escola = request.user.utilizador.escola
            despesa.creator = request.user
            despesa.save()
            return redirect('despesas_list')

        else:
            form = FormDespesas()
    return render(request, 'despesas_form.html',{'form':form})


class TipoDespesaCreate(CreateView):
    model = TipoDespesa
    fields = ['nome']
    success_url = reverse_lazy('despesas_list')



    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        tipo = form.save()
        tipo.instance.creator = self.request.user
        return super().form_valid(form)
    
    def get_absolute_url(self):
        return reverse_lazy('despesas_list')


def eliminar_despesa(request, pk):
    despesa = get_object_or_404(Despesas,pk=pk)
    despesa.delete()
    return redirect('despesas_list')
