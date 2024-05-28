from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, CreateView
from .models import Salarios
from .forms import FormSalarios
# Create your views here.


class ListSalarios(ListView):
    model = Salarios
    context_object_name = "Salarios_list"

    def get_queryset(self) -> QuerySet[Any]:
        escola = self.request.user.utilizador.escola
        return Salarios.objects.filter() 



class CreateSalarios(CreateView):
    model = Salarios
    form_class = FormSalarios

    def form_valid(self, form: BaseModelForm) -> HttpResponse:
        salarios = form.save()
        salarios.creator = self.request.user.utilizador
        return super().form_valid(form)
    
    def form_invalid(self, form: BaseModelForm) -> HttpResponse:
        return super().form_invalid(form)
    
    def get_form_kwargs(self) -> dict[str, Any]:
        kwargs = super().get_form_kwargs()
        kwargs['escola'] = self.request.user.utilizador.escola
        return kwargs