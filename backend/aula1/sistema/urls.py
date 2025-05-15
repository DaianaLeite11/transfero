from django.urls import path
from sistema import views


# informa qual rota será acessada view(funçaopython)
urlpatterns = [
    path('', views.index, name='index'),
    path('apresentacao/', views.apresentacao),
    path('listar/', views.listarUsuario, name='listarusuarios'),
    path('listarfilmes/', views.listarFilme),
    

]
