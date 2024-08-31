from django import forms
from .models import Funcionario


class FuncionarioForm(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields= ['nome', 'salario', 'horas_contrato','funcao','irs', 'iban', 'duodecimos','contrato','data_inicio']

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Nome Funcionário"}),
            'salario': forms.NumberInput(attrs={'class':'form-control'}),
            'horas_contrato': forms.NumberInput(attrs={'class':'form-control'}),
            'funcao': forms.TextInput(attrs={'class':'form-control'}),
            'irs': forms.Select(attrs={'class':'form-control'}),
            'iban': forms.TextInput(attrs={'class':'form-control'}),
            'duodecimos': forms.NullBooleanSelect(attrs={'class':'form-control'}),
            'data_inicio': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'contrato': forms.FileInput(attrs={
                'class': 'form-control'})
        }



    def __init__(self, *args, **kwargs):
        super(FuncionarioForm, self).__init__(*args, **kwargs)



class FormTermoContrato(forms.ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'data_fim', 'carta_rescicao']

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control', 'placeholder':"Nome Funcionário"}),
            'data_fim': forms.DateInput(attrs={'type': 'date', 'class':'form-control'}),
            'carta_rescicao': forms.FileInput(attrs={
                'class': 'form-control'})
            
        }

    def __init__(self, *args, **kwargs):
        super(FormTermoContrato, self).__init__(*args, **kwargs)
