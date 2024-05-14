from decimal import Decimal
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files import File
from .models import Salarios
from apps.funcionarios.models import Funcionario
from apps.documentos.models import RecibosVencimento
from apps.gestao.models import Despesas,TipoDespesa
from openpyxl import load_workbook
from datetime import datetime


@receiver(post_save, sender=Salarios)
def criar_recibo(sender, instance, created, **kwargs):
    if created:
        guardar_recibo(instance.funcionario.nome, instance.
        data_inicio, instance.data_fim, instance.valor)
        caminho_do_arquivo = f'media/recibos/{instance.funcionario.nome}_{instance.data_fim}.xlsx'

        funcionario = Funcionario.objects.get(pk= instance.funcionario.pk)
        novo_recibo = RecibosVencimento.objects.create(
            funcionario = funcionario,
            data = instance.data_fim,
            ficheiro = File(open(caminho_do_arquivo,'rb'))
        )
        


@receiver(post_save,sender=Salarios)
def calcular_salario(sender,instance, created, **kwargs):
    if created:
        print(instance.valor)
        if instance.funcionario.duodecimos :
            duodecimos = (float(instance.funcionario.salario) / 12) * 2
            salario_sem_descontos = duodecimos + instance.valor
            print(float(instance.valor))
            seg_social = salario_sem_descontos * 0.11
            salario_final = salario_sem_descontos - seg_social
            print(salario_final)
            escola= instance.funcionario.escola
            tipo_despesa = TipoDespesa.objects.get(nome="Ordenado")
            print(f"Salario: {salario_final}")

            if tipo_despesa:
                processar_despesa = Despesas(tipo_despesa,valor = salario_final,escola = escola,data = datetime.datetime.now())
                processar_despesa.save()
                print("Encontrou tipo despesa")
                
            else:
                novo_tipo = TipoDespesa(nome = "Ordenado",escola = escola)
                novo_tipo.save()
                print("Nao encontrou tipo despesa")

                processar_despesa = Despesas(tipo = novo_tipo,valor = salario_final,escola = escola,data = datetime.datetime.now())
                processar_despesa.save()
                print("Gravou com sucesso")

        else:
            print("Sem duodecimos")
            salario_iliquido = instance.valor
            print(salario_iliquido)
            seg_social = salario_iliquido * Decimal('0.11')
            print(seg_social)
            salario_final = salario_iliquido - seg_social
            print(salario_final)
            escola = instance.funcionario.escola
            tipo_despesa = TipoDespesa.objects.get(nome="Ordenado")

            if tipo_despesa:
                processar_despesa = Despesas(tipo_despesa,valor = salario_final,escola = escola, data = datetime.datetime.now())
                processar_despesa.save()
                print("Encontrou tipo despesa")
                
            else:
                novo_tipo = TipoDespesa(nome = "Ordenado",escola = escola)
                novo_tipo.save()
                print("Nao encontrou tipo despesa")

                processar_despesa = Despesas(tipo = novo_tipo,valor = salario_final,escola = escola,data = datetime.datetime.now())
                processar_despesa.save()
                print("Gravou com sucesso")
            











        





def guardar_recibo(nome, data_inicio, data_fim, valor):
    try:
        wb = load_workbook("media/recibos/exemplorecibo.xlsx")
        ws = wb.active
        print(nome)
        print(data_inicio)
        print(data_fim)
        print(valor)

        ws['B7'] = nome
        arquivo_salvo = f'media/recibos/{nome}_{data_fim}.xlsx'
        wb.save(arquivo_salvo)
        print("Arquivo salvo com sucesso!")
        
    except FileNotFoundError:
        print("Arquivo exemplorecibo.xlsx não encontrado")
    except Exception as error:
        print(f"Ocorreu um erro {error}")
       
        
