from typing import Any, Mapping
from django import forms
from django.contrib import admin
from django.core.files.base import File
from django.db.models.base import Model
from django.forms.utils import ErrorList
from .models import Salarios
from apps.funcionarios.models import Funcionario


class FormSalarios(forms.ModelForm):
    def __init__(self,*args, **kwargs):
        escola = kwargs.pop('escola',None)
        super(FormSalarios,self).__init__(*args,**kwargs)
        if escola:
            self.fields['funcionario'].queryset = Funcionario.objects.filter(escola= escola)

    class Meta:
        model = Salarios
        fields = ['funcionario', 'data_inicio', 'data_fim', 'falta', 'valor']  
        widgets = {
            'funcionario': forms.Select(attrs={'class':'form-control'}),
            'data_inicio': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'data_fim': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'falta': forms.NumberInput(attrs={'class': 'form-control'}),
            'valor': forms.NumberInput(attrs={'class': 'form-control','class': 'valor'}),

        }
        
    