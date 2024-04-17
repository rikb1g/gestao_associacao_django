from django import forms
from .models import Despesas, Entradas

class FormDespesas(forms.ModelForm):
    class Meta:
        model = Despesas
        fields = ['tipo', 'fatura', 'ficheiro', 'descricao', 'valor', 'data']
        widgets = {
            'tipo': forms.Select(attrs={'class':'form-control', 'placeholder':'Tipo de despesas'}),
            'fatura': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número da fatura'}),
            'ficheiro': forms.FileInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.NumberInput(attrs={'class':'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date'})
        }
    

    def __init__(self, *args, **kwargs):
        super(FormDespesas, self).__init__(*args, **kwargs)


class FormEntradas(forms.ModelForm):
    class Meta:
        model = Entradas
        fields = ['tipo', 'ficheiro', 'descricao', 'valor', 'data']
        widgets = {
            'tipo': forms.Select(attrs={'class':'form-control', 'placeholder':'Tipo de despesas'}),
            'ficheiro': forms.FileInput(attrs={'class':'form-control'}),
            'descricao': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.NumberInput(attrs={'class':'form-control'}),
            'data': forms.DateInput(attrs={'type': 'date'})
        }

    def __init__(self, *args, **kwargs):
        super(FormEntradas, self).__init__(*args, **kwargs)