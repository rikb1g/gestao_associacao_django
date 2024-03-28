from django.core.validators import MinValueValidator
from django.db import models
from django.urls import reverse

# Create your models here.

class Escola(models.Model):
    nome = models.CharField(max_length=100)



    def __str__(self):
        return self.nome

    def get_absolute_url(self):
        return reverse('home')



class Funcionario(models.Model):
    nome = models.CharField(max_length=100)
    horas_contrato = models.IntegerField(verbose_name="Horas contratadas diárias",name="Horas",
                                         validators=[MinValueValidator(0)])
    salario = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0.00)],
                                  verbose_name="Salário")
    funcao = models.CharField(max_length=50, verbose_name="Função")

    def __str__(self):
        return self.nome, self.funcao.verbose_name



class Atividades(models.Model):
    nome = models.CharField(max_length=100)
    escola = models.ForeignKey(Escola, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0.00)])

    def __str__(self):
        return self.nome
    def get_absolute_url(self):
        return reverse('alunos_list')

    def contar_alunos(self):
        return self.aluno_set.count()

    class Meta:
        verbose_name = "Atividade"
        verbose_name_plural = "Atividades"



class Mensalidade(models.Model):
    nome = models.CharField(max_length=100)
    valor = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(0.00)])
    escola = models.ForeignKey(Escola,on_delete=models.CASCADE)



    def get_absolute_url(self):
        return reverse('mensalidade_list')

    def contar_alunos(self):
        return self.aluno_set.count()

    def __str__(self):
        return self.nome
