from django.urls import path
from .views import DespesasList, DespesaCreate,DespesaEdit, TipoDespesaCreate,eliminar_despesa,TiposDespesaList, eliminar_tipos_Despesa, TiposDespesaEdit,EntradasList, EntradaCreate, EntradaEdit, eliminar_entrada, TipoEntradaCreate, TipoEntradaEdit, TipoEntradaList, tipo_entradas_delete


urlpatterns = [
    path('Despesas/',DespesasList.as_view(),name="despesas_list"),
    path('DespesasNova/',DespesaCreate.as_view(),name="despesas_create"),
    path('DespesasEdit/<int:pk>/',DespesaEdit.as_view(),name="despesas_edit"),
    path('novoTipo',TipoDespesaCreate.as_view(),name='tipo_despesa_create'),
    path('eliminarDespesa/<int:pk>/',eliminar_despesa,name='despesas_delete'),
    path('TipoDespesasLista/',TiposDespesaList.as_view(),name='tipo_despesas_list'),
    path('TipoDespesaDelete/<int:pk>/',eliminar_tipos_Despesa,name='tipo_despesas_delete'),
    path('TipoDespesaEditar/<int:pk>/',TiposDespesaEdit.as_view(), name='tipo_despesas_edit'),
    path('Entradas/', EntradasList.as_view(), name= 'entradas_list'),
    path('EntradasNova/', EntradaCreate.as_view(), name= 'entradas_create'),
    path('EntradasEdit/<int:pk>/', EntradaEdit.as_view(), name= 'entradas_edit'),
    path('EntradaDelete/<int:pk>/', eliminar_entrada, name= 'entradas_delete'),
    path('TipoEntradasList/', TipoEntradaList.as_view(), name= 'tipo_entradas_list'),
    path('TipoEntradasEdit/<int:pk>/', TipoEntradaEdit.as_view(), name= 'tipo_entradas_edit'),
    path('TipoEntradasNew/', TipoEntradaCreate.as_view(), name= 'tipo_entradas_create'),
    path('TipoEntradasDelete/<int:pk>/', tipo_entradas_delete, name= 'tipo_entradas_delete'),


]