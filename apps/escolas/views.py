import calendar
import datetime
import json

from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView

from .models import Escola, Mensalidade, Atividades
from apps.estudantes.models import MensalidadePagamento, Aluno


class CriarEscola(CreateView):
    model = Escola
    fields = ['nome']

    def form_valid(self, form):
        objeto = form.save()
        usuario = self.request.user.utilizador
        usuario.escola = objeto
        usuario.save()
        return redirect("home")



class EditEscola(UpdateView):
    model = Escola
    fields = ['nome']
    template_name = 'mensalidade_form.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        escola = self.get_object()
        context['mensalidades'] = Mensalidade.objects.filter(escola=escola)
        return context




class CreateMensalidade(CreateView):
    model = Mensalidade
    fields = ['nome', 'valor']
    success_url = 'mensalidade_list'

    def form_valid(self, form):
        mensalidade = form.save(commit= False)
        mensalidade.escola = self.request.user.utilizador.escola
        mensalidade.save()
        return redirect('home')

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))
    
    def get_absolute_url(self):
        redirect('mensalidade_list')


class CreateAtividade(CreateView):
    model = Atividades
    fields = ['nome', 'valor']
    success_url = 'atividades_list'

    def form_valid(self, form):
        atividade = form.save(commit=False)
        atividade.escola = self.request.user.utilizador.escola
        atividade.save()
        return super(CreateAtividade,self).form_valid(form)
    
    def get_absolute_url(self):
        redirect('alunos_list')

class AtividadesList(ListView):
    model = Atividades
    template_name = 'atividade'
    context_object_name = 'atividades'

    def get_queryset(self):
        escola = self.request.user.utilizador.escola
        query = self.request.GET.get('query_atividades')

        if query:
            return Atividades.objects.filter(nome__icontains=query,escola=escola)

        else:
            return Atividades.objects.filter(escola=escola)






class AtividadeNew(CreateView):
    model = Atividades
    fields = ['nome','valor']
    success_url = 'atividades_list'

    def form_valid(self, form):
        atividade = form.save(commit=False)
        atividade.escola = self.request.user.utilizador.escola
        form.instance.creator = self.request.user
        atividade.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))

    def get_absolute_url(self):
        redirect('alunos_list')


def remover_atividade(request, pk):
    aluno_eliminar = get_object_or_404(Atividades, pk=pk)
    aluno_eliminar.delete()
    return redirect('atividades_list')

class AtividadeEdit(UpdateView):
    model = Atividades
    fields = ['nome', 'escola','valor']
    success_url = reverse_lazy('atividades_list')



class MensalidadeList(ListView):
    model = MensalidadePagamento
    template_name = "mensalidadePagamento/mensalidadePagamento_list.html"
    context_object_name = "mensalidades"

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

        if ano_selecionado and mes_selecionado:
            return MensalidadePagamento.objects.filter(escola= escola,mes= mes_selecionado, ano= ano_selecionado)
        else:
            return MensalidadePagamento.objects.filter(escola= escola,mes= mes_atual, ano = ano_atual)



    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ano_inicial = 2023
        anos_letivos = range(ano_inicial, ano_inicial + 10)
        context['anos_letivos'] = anos_letivos
        context['meses'] = MESES

        alunos = Aluno.objects.all()
        context['alunos'] = alunos

        return context




class MensaliadeEdit(UpdateView):
    model = Mensalidade
    fields = ['nome', 'valor']
    success_url = reverse_lazy('mensalidade_list')


def remover_mensalidade(request, pk):
    mensalidade_eliminar = get_object_or_404(Mensalidade, pk=pk)
    mensalidade_eliminar.delete()
    return redirect('mensalidade_list')



MESES = ("Setembro", "Outubro","Novembro", "Dezembro", "Janeiro","Fevereiro","Março","Abril",
         "Maio", "Junho","Julho","Agosto")

meses_portugueses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]


def atualizar_mensalidade_aluno(request, mensalidade_id):
    if request.method == 'POST':
        data = json.loads(request.body)
        paga = data.get('paga')
        if paga is not None:
            mensalidade = MensalidadePagamento.objects.get(pk=mensalidade_id)
            mensalidade.escola = request.user.utilizador.escola
            mensalidade.paga = paga
            mensalidade.save()
            return JsonResponse({'mensagem': 'Mensalidade atualizada com sucesso'})
    return JsonResponse({'erro': 'Erro ao atualizar a mensalidade'}, status = 400)




