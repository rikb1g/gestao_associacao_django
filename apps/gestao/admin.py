from django.contrib import admin
from .models import Despesas, Entradas,TipoDespesa,TipoEntrada

admin.site.register(Despesas)
admin.site.register(Entradas)
admin.site.register(TipoEntrada)
admin.site.register(TipoDespesa)
