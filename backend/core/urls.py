from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('areas/', views.areas_pesquisa, name='areas_pesquisa'),
    path('projetos/', views.projetos, name='projetos'),
    path('publicacoes/', views.publicacoes, name='publicacoes'),
    path('orientacoes/', views.orientacoes, name='orientacoes'),
    path('contato/', views.contato, name='contato'),
]
