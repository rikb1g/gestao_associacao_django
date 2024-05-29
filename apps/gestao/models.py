from django.db import models
from django.core.validators import MinValueValidator
from django.dispatch import receiver
from django.urls import reverse
from django.db.models.signals import post_delete
from apps.escolas.models import Escola
from django.db.models import Sum
import os
from datetime import datetime


class TipoEntrada(models.Model):
    nome = models.CharField(max_length= 100)
    escola = models.ForeignKey(Escola,on_delete= models.CASCADE)

    def __str__(self) -> str:
        return self.nome
    

class TipoDespesa(models.Model):
    nome = models.CharField(max_length=100)
    escola = models.ForeignKey(Escola,on_delete= models.CASCADE)


    def __str__(self) -> str:
        return self.nome


class Despesas(models.Model):
    tipo = models.ForeignKey(TipoDespesa, on_delete=models.CASCADE)
    fatura = models.CharField(max_length=50,blank=True, null=True)
    ficheiro = models.FileField(blank=True, upload_to='despesas/')
    descricao = models.CharField(max_length=100,blank=True,null=True)
    valor = models.DecimalField(max_digits=10,decimal_places=2,validators=[MinValueValidator(0.00)])
    escola = models.ForeignKey(Escola,on_delete=models.CASCADE)
    data = models.DateTimeField(null= True, blank=True)

    def __str__(self):
        return f"{self.tipo}, {self.fatura},{self.descricao}, {self.data}"
    
    def get_absolute_url(self):
        return reverse('despesas_list')
    
    
    @classmethod
    def total_despesa_mensal(cls,escola ,mes, ano):
        match mes:
            case "Setembro":
                return cls.objects.filter(escola =escola,data__range=[f"01-09-{ano}",f"30-09-{ano}"]).aggregate(total=Sum('valor'))['total'] or 0
            
    

        
    
    @classmethod
    def total_despesa(cls, escola):
        return cls.objects.filter(escola= escola).aggregate(total=Sum('valor'))['total'] or 0
        
@receiver(post_delete, sender=Despesas)
def delete_file_on_post_delete(sender, instance, **kwargs):
    if instance.ficheiro:
        if os.path.isfile(instance.ficheiro.path):
            os.remove(instance.ficheiro.path)

class Entradas(models.Model):
    tipo = models.ForeignKey(TipoEntrada,on_delete=models.CASCADE)
    ficheiro = models.FileField(blank=True,upload_to='Entradas/')
    descricao = models.CharField(max_length=100, blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0.00)])
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    data = models.DateTimeField(null=True,blank=True)

    def get_absolute_url(self):
        return reverse('receitas_list')

    def __str__(self):
        return f"{self.tipo},{self.descricao}, {self.data}"
    
    @classmethod
    def total_receita_mensal(cls,escola, data_inicio, data_fim):
        return cls.objects.filter(escola=escola, data__range =[data_inicio,data_fim]).aggregate(total=Sum('valor'))['total'] or 0
    

    @classmethod
    def total_receita(cls, escola):
        return cls.objects.filter(escola= escola).aggregate(total=Sum('valor'))['total'] or 0

@receiver(post_delete, sender=Entradas)
def delete_file_on_post_delete(sender, instance, **kwargs):
    if instance.ficheiro:
        if os.path.isfile(instance.ficheiro.path):
            os.remove(instance.ficheiro.path)



meses_ano_letivo_ano_atual = ["Setembro", "Outubro","Novembro", "Dezembro"]

meses_ano_letivo_ano_seguinte = ["Janeiro","Fevereiro","Março","Abril","Maio", "Junho","Julho","Agosto"]