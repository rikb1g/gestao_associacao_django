from django.db.models.signals import post_save
from django.dispatch import receiver
from apps.estudantes.models import MensalidadePagamento, Aluno
from apps.gestao.models import Entradas, TipoEntrada
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=MensalidadePagamento)
def inserir_valor_mensalidade(sender, instance, created, **kwargs):
    
    if not created:
        try:
            original_instance = sender.objects.get(pk=instance.pk)
            print(original_instance.paga)
            if original_instance.paga:
                print(f"paga field changed: {original_instance.paga} -> {instance.paga}")
                if instance.paga:
                    aluno = Aluno.objects.prefetch_related('atividade','mensalidade').get(pk=instance.aluno.pk)
                    tipo_entrada = TipoEntrada.objects.get(nome="Mensalidade")
                    
                    atividades = aluno.atividade.all()
                    mensalidades = aluno.mensalidade.all()
                    total_atividades = 0
                    total_mensalidades = 0 
                    for atividade in atividades:
                        valor_atividade = atividade.valor
                        total_atividades += valor_atividade

                    for mensalidade in mensalidades:
                        valor_mesalidade = mensalidade.valor
                        total_mensalidades += valor_mesalidade
                    
                    mes = meses.index(instance.mes) + 1
                    ano = instance.ano
                    data = f"{ano}-{mes}-01"
                    total_pago = total_atividades +total_mensalidades

                    entrada = Entradas(
                        tipo=tipo_entrada,
                        descricao=f"{instance.aluno.nome} mês {mes} do ano {ano}",
                        data=data,
                        valor=total_pago,
                        escola=instance.escola
                    )
                    try:
                        entrada.full_clean()
                        entrada.save()
                        print("saved sucessfully")
                        
                    except Exception as e:
                        print(f"Erro: {e}")
            else:
                    print("Payment marked as not paid")
                    mes = meses.index(instance.mes) + 1
                    ano = instance.ano
                    data = f"{ano}-{mes}-01"
                    descricao=f"{instance.aluno.nome} mês {mes} do ano {ano}"
                    print(descricao)
                    entrada = Entradas.objects.filter(descricao=descricao)
                    if entrada:
                        print("deleted")
                        entrada.delete()
                    
        except sender.DoesNotExist:
            print("erro")




meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
    "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]