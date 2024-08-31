from django import forms
from django.contrib import admin
from .models import Atividades



class AtividadeForm(forms.ModelForm):
    class Meta:
        model = Atividades
        fields = ['nome', 'valor']

        widgets = {
            'nome': forms.TextInput(attrs={'class':'form-control'}),
            'valor': forms.TextInput(attrs={'class':'form-control'}),
        }




class AtividadeAdmin(admin.ModelAdmin):
    form = AtividadeForm