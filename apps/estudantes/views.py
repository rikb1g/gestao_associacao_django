import datetime

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import datetime

from .models import Aluno, Atividades, Mensalidade, MensalidadePagamento
from .forms import AlunoForm
from django.views.generic import ListView, UpdateView,CreateView, DetailView

# Create your views here.

class AlunoList(ListView):
    model = Aluno
    template_name = 'aluno_list.html'
    context_object_name = 'alunos_list'

    def get_queryset(self):
        query = self.request.GET.get('query_alunos')
        escola = self.request.user.utilizador.escola

        if query:
            # Filtra os alunos cujo nome contém a query
            return Aluno.objects.filter(nome__icontains=query, escola= escola, ativo= True)
        else:
            # Retorna todos os alunos se não houver uma query
            return Aluno.objects.filter(escola=escola,ativo =True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Passa a query atual para o contexto para exibi-la no template
        context['query_alunos'] = self.request.GET.get('query_alunos', '')
        context['tipo_lista'] = "ativos"

        # adicionar mensalidades ao contexto
        alunos = context['alunos_list']
        mensalidades = {}

        for aluno in alunos:
            mensalidades[aluno.id] = MensalidadePagamento.objects.filter(aluno=alunos, atraso= False)

        return context

from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages
from datetime import datetime

from .models import Aluno, Atividades, Mensalidade, MensalidadePagamento
from .forms import AlunoForm
from django.views.generic import ListView, UpdateView,CreateView, DetailView

# Create your views here.

class AlunoList(ListView):
    model = Aluno
    template_name = 'aluno_list.html'
    context_object_name = 'alunos_list'

    def get_queryset(self):
        query = self.request.GET.get('query_alunos')
        escola = self.request.user.utilizador.escola

        if query:
            # Filtra os alunos cujo nome contém a query
            return Aluno.objects.filter(nome__icontains=query, escola= escola, ativo= True)
        else:
            # Retorna todos os alunos se não houver uma query
            return Aluno.objects.filter(escola=escola,ativo =True)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Passa a query atual para o contexto para exibi-la no template
        context['query_alunos'] = self.request.GET.get('query_alunos', '')
        context['tipo_lista'] = "ativos"

        # adicionar mensalidades ao contexto



        return context









class AlunoCreate(CreateView):
    model = Aluno
    form_class = AlunoForm

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['escola'] = self.request.user.utilizador.escola
        return kwargs

    def form_valid(self, form):
        aluno = form.save(commit=False)
        aluno.creator = self.request.user.utilizador
        aluno.escola = self.request.user.utilizador.escola
        aluno.ativo = True
        aluno.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def remover_aluno(request, pk):
    aluno_eliminar = get_object_or_404(Aluno,pk=pk)
    aluno_eliminar.delete()
    return redirect('alunos_list')

def arquivar_aluno(request, pk):
    aluno_arquivar = get_object_or_404(Aluno, pk=pk)
    ano = datetime.now().year

    aluno_arquivar.ano_saida = int(ano)
    aluno_arquivar.ativo = False
    aluno_arquivar.save()
    return redirect('alunos_list')

class AlunoEdit(UpdateView):
    model = Aluno
    form_class= AlunoForm
    success_url = reverse_lazy('alunos_list')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['escola'] = self.request.user.utilizador.escola

        return kwargs


class AlunoDetail(DetailView):
    model = Aluno
    context_object_name = 'aluno_detail'


class AlunoHistoric(ListView):
    model = Aluno
    context_object_name = "historic_alunos"
    template_name = 'aluno_list.html'


    def get_queryset(self):
        query = self.request.GET.get('query_alunos')
        escola = self.request.user.utilizador.escola

        if query:
            return Aluno.objects.filter(nome__icontains=query, escola=escola, ativo=False)
        else:
            return Aluno.objects.filter(escola=escola, ativo= False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query_alunos'] = self.request.GET.get('query_alunos','')
        context['tipo_lista'] = "historico"
        return context



def renovar_maticula(request, pk):
    aluno_renovar = get_object_or_404(Aluno, pk=pk)
    ano_inicio = int(datetime.now().year)
    num_mensalidade = 12

    for mes in range(9, 9+ num_mensalidade):
        mes_ano = divmod(mes - 1, 12)
        mes_atual = mes_ano[1] + 1
        ano_atual = ano_inicio + mes_ano[0]
        if mes_atual in [8,9]:
            continue

        mes_atual = meses_portugueses[mes_atual -1]

        mensalidade = MensalidadePagamento(aluno=aluno_renovar, mes=mes_atual,ano=ano_atual, paga=False, escola=aluno_renovar.escola)
        mensalidade.save()

    return redirect('alunos_list')

def ano_civil(data):
    if data.month <= 9:
        return data.year -1
    else:
        return data.year
meses_portugueses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
















