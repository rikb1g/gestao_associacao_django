from django.urls import path
from .views import DespesasList, DespesaCreate, TipoDespesaCreate,eliminar_despesa


urlpatterns = [
    path('Despesas/',DespesasList.as_view(),name="despesas_list"),
    path('DespesasNoba/',DespesaCreate,name="despesas_create"),
    path('novoTipo',TipoDespesaCreate.as_view(),name='tipo_despesa_create'),
    path('eliminarDespesa/<int:pk>/',eliminar_despesa,name='despesas_delete'),
]