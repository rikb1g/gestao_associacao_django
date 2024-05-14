from django.db import models
from apps.funcionarios.models import Funcionario
# Create your models here.


class RecibosVencimento(models.Model):
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    data = models.CharField(max_length=50)
    ficheiro = models.FileField(blank=True,upload_to="salarios/recibos")