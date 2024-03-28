from django.db import models
from django.core.validators import MinValueValidator
from apps.escolas.models import Escola



class Despesas(models.Model):
    tipo = models.CharField(max_length=100)
    fatura = models.CharField(max_length=50,blank=True, null=True)
    descricao = models.CharField(max_length=100,blank=True,null=True)
    valor = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.00)])
    escola = models.ForeignKey(Escola,on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo, self.fatura,self.descricao, self.escola.name


class Receita(models.Model):
    tipo = models.CharField(max_length=100)
    fatura = models.CharField(max_length=50, blank=True, null=True)
    descricao = models.CharField(max_length=100, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)

    def __str__(self):
        return self.tipo, self.fatura,self.descricao, self.escola.name

