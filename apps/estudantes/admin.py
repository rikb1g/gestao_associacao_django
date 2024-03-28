from django.contrib import admin
from .models import Aluno, Mensalidade, Atividades,MensalidadeAtividade,MensalidadePagamento

admin.site.register(Aluno)
admin.site.register(Mensalidade)
admin.site.register(Atividades)
admin.site.register(MensalidadeAtividade)
admin.site.register(MensalidadePagamento)
