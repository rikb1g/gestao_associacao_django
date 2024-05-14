from django.db import models
from django.core.validators import MinValueValidator
from django.shortcuts import redirect
from django.urls import reverse
from apps.escolas.models import Escola

# Create your models here.


class EscalaoIRS(models.Model):
    nome = models.CharField(max_length=100)


    def get_absolute_url(self):
        return reverse('escaloes_list')

    
    def __str__(self) -> str:
        return self.nome




class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    salario = models.DecimalField(verbose_name="Salario", validators=[MinValueValidator(0)],max_digits=15,decimal_places=3)
    horas_contrato = models.IntegerField(verbose_name="Horas contratadas diárias")
    funcao = models.CharField(max_length=50, verbose_name="Função")
    irs = models.ForeignKey(EscalaoIRS,on_delete=models.PROTECT)
    iban = models.CharField(max_length=50,blank=True)
    duodecimos = models.BooleanField(default=False)
    escola = models.ForeignKey(Escola, on_delete=models.PROTECT)

    def get_absolute_url(self):
        return reverse('funcionarios_list')

    def __str__(self):
        return self.nome
    


class HorasExtra(models.Model):
    motivo = models.CharField(max_length=100)
    Funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT)
    horas = models.DecimalField(max_digits=5, decimal_places=2)