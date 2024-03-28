from django.db import models
from apps.escolas.models import Escola
from django.contrib.auth.models import User

# Create your models here.

class Utilizador(models.Model):
    nome = models.CharField(max_length=100)
    user = models.OneToOneField(User,on_delete=models.PROTECT)
    escola = models.OneToOneField(Escola, on_delete=models.PROTECT,blank=True,null=True)


    

    def __str__(self):
        return self.nome
