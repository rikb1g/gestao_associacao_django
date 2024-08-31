from django import forms
from django.contrib import admin
import re
from .models import Aluno, Mensalidade, Atividades



class AlunoForm(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        escola = kwargs.pop('escola',None)
        super().__init__(*args,**kwargs)
        if escola:
            self.fields['atividade'].queryset = Atividades.objects.filter(escola=escola)
            self.fields['mensalidade'].queryset = Mensalidade.objects.filter(escola=escola)
        if not Atividades.objects.filter(escola=escola):
            self.fields['atividade'].empty_label = "Nenhuma atividade"
        
    class Meta:
        model = Aluno
        fields = ['nome','ano_matricula','ano_saida','atividade','mensalidade','enc_educacao', 'contato']
        
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'ano_matricula': forms.TextInput(attrs={'class':'form-control'}),
            'ano_saida': forms.TextInput(attrs={'class':'form-control'}),
            'atividade': forms.SelectMultiple(attrs={'class':'form-control'}),
            'mensalidade': forms.SelectMultiple(attrs={'class':'form-control'}),
            'enc_educacao': forms.TextInput(attrs={'class':'form-control'}),
            'contato': forms.TextInput(attrs={'class':'form-control'}),
        }
    

class AlunoAdmin(admin.ModelAdmin):
    form = AlunoForm
    


