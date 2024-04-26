from django.contrib import admin
from .models import Aluno, Mensalidade, Atividades,MensalidadeAtividade,MensalidadePagamento
from .forms import AlunoAdmin

admin.site.register(Aluno, AlunoAdmin)
admin.site.register(Mensalidade)
admin.site.register(Atividades)
admin.site.register(MensalidadeAtividade)
admin.site.register(MensalidadePagamento)
