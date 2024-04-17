from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

from apps.escolas.models import Escola, Atividades, Mensalidade
from django.core.validators import MinValueValidator
from django.utils import timezone

# Create your models here.

def validate_year(value):
    if value < 1000 or value > 9999:
        raise ValidationError("O ano deve estar entre 1900 e 2100.")

class AnoField(models.IntegerField):
    default_validators = [validate_year]

    def __init__(self, *args, **kwargs):
        kwargs['validators'] = kwargs.get('validators',[]) + [validate_year]
        super().__init__(*args, **kwargs)


class Aluno(models.Model):
    nome = models.CharField(max_length=100,)
    escola = models.ForeignKey(Escola, on_delete=models.PROTECT)
    ano_matricula = AnoField()
    ano_saida = AnoField( null=True,blank=True)
    atividade = models.ManyToManyField(Atividades, blank=True)
    mensalidade = models.ManyToManyField(Mensalidade)

    def get_absolute_url(self):
        return reverse('alunos_list')

    def __str__(self):
        return self.nome









class MensalidadePagamento(models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.CASCADE, related_name='mensalidades')
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    mes = models.CharField(verbose_name="Mês",max_length=20)
    ano = models.IntegerField(verbose_name="Ano")
    paga = models.BooleanField(default=False, verbose_name="Paga")


    def __str__(self):

        return f"Mensalidade de {self.aluno.nome} do mês {self.mes} do ano {self.ano}"

class MensalidadeAtividade(models.Model):
    atividade = models.ForeignKey(Atividades, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0.00)])


    def __str__(self):
        return self.atividade.nome

    class Meta:
        verbose_name = "Mensalidade Atividade"
        verbose_name_plural = "Mensalidades Atividades"




