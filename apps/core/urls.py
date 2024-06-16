from django.contrib import admin
from django.urls import path
from .views import home,bar_chart_view

urlpatterns = [
    path('', home, name='home'),
    path('teste', bar_chart_view, name='bar'),

]
