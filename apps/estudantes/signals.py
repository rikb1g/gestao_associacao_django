from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Aluno, MensalidadePagamento
from datetime import datetime



@receiver(post_save, sender=Aluno)
def criar_mensalidade(sender, instance, created, **Kwargs):
    print("teste")
    if created:
        ano_inicio = ano_civil(datetime.now())
        num_mensalidade = 12

        for mes in range(9, 9+num_mensalidade):
            mes_ano = divmod(mes -1, 12)
            mes_atual = mes_ano[1] + 1
            ano_atual = ano_inicio + mes_ano[0]
            mes_atual = meses_portugueses[mes_atual -1]

            mensalidade = MensalidadePagamento(aluno=instance, mes= mes_atual, ano=ano_atual, paga=False)
            mensalidade.save()


meses_portugueses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

def ano_civil(data):
    if data.month <= 9:
        return data.year -1
    else:
        return data.year

