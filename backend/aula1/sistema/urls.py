from django.urls import path
from sistema import views


# informa qual rota será acessada view(funçaopython)
urlpatterns = [
    path('sistema/', views.index),
]
