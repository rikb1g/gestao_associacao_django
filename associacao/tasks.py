from associacao.celery import shared_task
from .models import MensalidadePagamento
from django.utils import timezone




@shared_task
def verificar_mensalidade_em_atraso():
    mes_atual = timezone.now().month
    
    ano = timezone.now().year

    
    if mes_atual >=8 or mes_atual <12:
        while mes_atual < 8:
            mes = meses_portugueses[mes_atual +1]
            mensalidade_atrao = MensalidadePagamento.objects.filter(mes=mes, pago=False)
            for mensalidade in mensalidade_atrao:
                mensalidade.atraso = True
                mensalidade.save()
            
            mes_atual -= 1

    
    if mes_atual <=7:
        while mes_atual <0:
            mes = meses_portugueses[mes_atual +1]
            mensalidade_atrao = MensalidadePagamento.objects.filter(mes=mes, pago=False)
            for mensalidade in mensalidade_atrao:
                mensalidade.atraso = True
                mensalidade.save()
            
            mes_atual -= 1
        
        mes_atual = 8
        while mes_atual <12:
            mes = meses_portugueses[mes_atual +1]
            mensalidade_atrao = MensalidadePagamento.objects.filter(mes=mes, pago=False)
            for mensalidade in mensalidade_atrao:
                mensalidade.atraso = True
                mensalidade.save()
            
            mes_atual += 1 
            

    



    atualizar_apos_pagamento = MensalidadePagamento.objects.filter(mes=mes, pago= True)
    for mensalidade in atualizar_apos_pagamento:
        mensalidade.atraso = False

        mensalidade.save()




meses_portugueses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]