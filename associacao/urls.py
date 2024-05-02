from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from associacao import settings

urlpatterns = [
    path('',include('apps.core.urls'), name='home'),
    path('admin/', admin.site.urls),
    path("alunos/", include("apps.estudantes.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("escolas/", include("apps.escolas.urls")),
    path('gestaoFinanceira/', include("apps.gestao.urls")),
    path('funcionarios/', include("apps.funcionarios.urls")),
    path('salarios/', include("apps.salarios.urls")),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
