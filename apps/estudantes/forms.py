from django import forms
from django.contrib import admin
from .models import Aluno, Mensalidade

class AlunoForm(forms.ModelForm):
    class Meta:
        model = Aluno
        fields = ['nome','escola','ano_matricula','ano_saida','atividade','enc_educacao', 'contato']
    
    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['escola'].disabled = True
        self.initial['escola'] = user.utilizador.escola

    def save(self,commit=True):
        instance = super().save(commit=commit)
        if commit:

            instance.save()

        return instance


class AlunoAdmin(admin.ModelAdmin):
    form = AlunoForm
    


