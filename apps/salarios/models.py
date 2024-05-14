from django.db import models
from django.core.validators import MinValueValidator
from django.urls import reverse
from apps.funcionarios.models import Funcionario
# Create your models here.


class Salarios(models.Model):
    funcionario = models.ForeignKey(Funcionario,on_delete=models.PROTECT)
    data_inicio = models.DateField()
    data_fim = models.DateField()
    falta = models.DecimalField(validators=[MinValueValidator(0)],max_digits=10,decimal_places=2)
    valor = models.DecimalField(max_digits= 10,decimal_places=2)
    

    def get_absolute_url(self):
        return reverse('funcionarios_list')

    def __str__(self) -> str:
        return f"{self.funcionario} data {self.data_inicio} a {self.data_fim}"

