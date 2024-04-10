from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.contrib import messages

from .models import Aluno, Atividades, Mensalidade
from django.views.generic import ListView, UpdateView,CreateView, DetailView
# Create your views here.

class AlunoList(ListView):
    model = Aluno
    template_name = 'aluno_list.html'
    context_object_name = 'alunos_list'

    def get_queryset(self):
        query = self.request.GET.get('query')
        escola = self.request.user.utilizador.escola

        if query:
            # Filtra os alunos cujo nome contém a query
            return Aluno.objects.filter(nome__icontains=query, escola= escola)
        else:
            # Retorna todos os alunos se não houver uma query
            return Aluno.objects.filter(escola=escola)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Passa a query atual para o contexto para exibi-la no template
        context['query'] = self.request.GET.get('query', '')
        return context






class AlunoCreate(CreateView):
    model = Aluno
    fields = ['nome','ano_matricula','atividade', 'mensalidade']

    def form_valid(self, form):
        aluno = form.save(commit=False)
        aluno.escola = self.request.user.utilizador.escola
        aluno.save()
        return super().form_valid(form)
    def form_invalid(self, form):
        return self.render_to_response(self.get_context_data(form=form))


def remover_aluno(request, pk):
    aluno_eliminar = get_object_or_404(Aluno,pk=pk)
    aluno_eliminar.delete()
    return redirect('alunos_list')

class AlunoEdit(UpdateView):
    model = Aluno
    fields = ['nome', 'ano_matricula','ano_saida','atividade', 'mensalidade']
    success_url = reverse_lazy('alunos_list')


















