from django import forms
from .models import Aluno, Mensalidade

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','escola','ano_matricula','ano_saida','atividade']

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['escola'].disabled = True
        self.initial['escola'] = user.utilizador.escola


