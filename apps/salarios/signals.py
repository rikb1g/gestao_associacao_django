from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.files import File
from .models import Salarios
from openpyxl import load_workbook



@receiver(post_save, sender=Salarios)
def criar_recibo(sender, instance, created, **kwargs):
    if created:
        file = guardar_recibo(instance.funcionario.nome, instance.
        data_inicio, instance.data_fim, instance.valor)
        if file:
            with open(file, 'rb') as f:
                recibo = Salarios.objects.get(pk=instance.pk)
                recibo.recibo.save(f"{instance.funcionario.nome}_{instance.data_fim}.xlsx", File(f), save =True)
                recibo.save()
                print("recibo atribuido com sucesso")
        





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
        return arquivo_salvo
    except FileNotFoundError:
        print("Arquivo exemplorecibo.xlsx não encontrado")
    except Exception as error:
        print(f"Ocorreu um erro {error}")
        return None
        
