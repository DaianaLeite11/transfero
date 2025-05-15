from django.urls import path               # Importa o módulo de rotas do Django
from usuarios import views                 # Importa as views do app usuarios

urlpatterns = [
    path('cadastro/', views.criarUsuario, name='criarusuario'),  # Rota para a página de cadastro
    path('login/', views.login, name='login'),           # Rota para a página de login
]