from django.urls import path               # Importa o módulo de rotas do Django
from filmes import views                 # Importa as views do app usuarios

urlpatterns = [
    path('cadastrar/', views.criarFilme, name='cadastrar'),  # Rota para a página de cadastro
    path('listagem/', views.listagem, name='listagem'),    
]       # Rota para a página de login