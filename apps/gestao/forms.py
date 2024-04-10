from django import forms
from .models import Despesas

class FormDespesas(forms.ModelForm):
    class Meta:
        model = Despesas
        fields = ['tipo', 'fatura', 'ficheiro', 'descricao', 'valor', 'escola', 'data']
        widgets = {
            'data': forms.DateInput(attrs={'type': 'date'})
        }
        # Se você quiser todos os campos do modelo, você pode simplesmente usar '__all__' em vez de listá-los manualmente

    def __init__(self, *args, **kwargs):
        super(FormDespesas, self).__init__(*args, **kwargs)


