from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('',include('apps.core.urls'), name='home'),
    path('admin/', admin.site.urls),
    path("alunos/", include("apps.estudantes.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("escolas/", include("apps.escolas.urls")),
]
