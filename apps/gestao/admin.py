from django.contrib import admin
from .models import Despesas, Receita,TipoDespesa,TipoReceita

admin.site.register(Despesas)
admin.site.register(Receita)
admin.site.register(TipoReceita)
admin.site.register(TipoDespesa)
