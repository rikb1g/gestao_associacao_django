from django.db import models
from django.core.exceptions import ValidationError
from django.urls import reverse

from apps.escolas.models import Escola, Atividades, Mensalidade
from django.core.validators import MinValueValidator
from django.utils import timezone

class AnoField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 4  # Definindo o comprimento máximo para 4 caracteres
        kwargs['blank'] = True  # Permitir valores em branco
        kwargs['null'] = True  # Permitir valores nulos
        super().__init__(*args, **kwargs)


class Aluno(models.Model):
    nome = models.CharField(max_length=100,)
    escola = models.ForeignKey(Escola, on_delete=models.PROTECT)
    ano_matricula = models.CharField(max_length=4)
    ano_saida = models.IntegerField(blank=True, null=True)
    contato = models.CharField(max_length=20,blank=True)
    enc_educacao = models.CharField(max_length=100, blank=True,verbose_name= "Encarregado de Educação")
    atividade = models.ManyToManyField(Atividades, blank=True)
    mensalidade = models.ManyToManyField(Mensalidade)
    ativo = models.BooleanField(default=True)
    atraso = models.BooleanField(default=False)


    def calcular_valor_mensalidade(self):
        mensalidade = sum(mensalidade.valor for mensalidade in self.mensalidade.all())
        atividade = sum(atividade.valor for atividade in self.atividade.all())
        print(atividade)
        total = mensalidade + atividade
        return total


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
    atraso = models.BooleanField(default=False)

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




