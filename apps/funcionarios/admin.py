from django.contrib import admin
from .models import Funcionario, HorasExtra, EscalaoIRS

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(HorasExtra)
admin.site.register(EscalaoIRS)