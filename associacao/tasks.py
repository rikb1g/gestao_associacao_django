from associacao.celery import shared_task
from apps.estudantes.models import MensalidadePagamento
import datetime




@shared_task
def verificar_mensalidade_em_atraso():
    print("asdasdasdasd")
    mes_atual = datetime.datetime.now().month   
    ano = datetime.datetime.now().year

    
    if mes_atual > 8 or mes_atual <=12:
        while mes_atual < 8:
            mes = meses_portugueses[mes_atual +1]
            mensalidade_atrao = MensalidadePagamento.objects.filter(mes=mes,ano=ano ,pago=False)
            print(mensalidade_atrao)
            for mensalidade in mensalidade_atrao:
                mensalidade.atraso = True
                mensalidade.save()
            
            mes_atual -= 1

    
    if mes_atual < 9:
        print("finca")
        while mes_atual < 0:
            mes = meses_portugueses[mes_atual +1]
            mensalidade_atrao = MensalidadePagamento.objects.filter(mes=mes,ano= ano ,pago=False)
            print(mensalidade_atrao)
            for mensalidade in mensalidade_atrao:
                mensalidade.atraso = True
                mensalidade.save()

            mes_atual -= 1
        
        mes_atual = 8
        while mes_atual <12:
            ano_anterior = ano -1 
            mes = meses_portugueses[mes_atual +1]
            mensalidade_atrao = MensalidadePagamento.objects.filter(mes=mes, ano= ano_anterior ,pago=False)
            print(mensalidade_atrao)
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