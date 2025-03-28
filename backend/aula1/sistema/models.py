from django.utils import timezone
from django.db import models

# Aqui vai ficar a classe modelo do usuário
#none, sobrenome, cpf, telefone, email, foto, endereco
# data_cadastro, ativo
class Usuario(models.Model):
    nome = models.CharField(max_length=50)
    sobrenome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=20)
    email = models.EmailField()
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(default=timezone.now) #DATA E HORA DO CADASTRO
    ativo = models.BooleanField(default=True)
    # foto = 

class Filme(models.Model):
    nome_do_filme= models.CharField(max_length=100)
    ano_lancamento = models.IntegerField()
    estudio = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    sinopse = models.TextField()
    data_de_cadastro = models.DateTimeField(default=timezone.now)

class Genero(models.Model):
    genero = models.CharField(max_length=50)
    data_de_cadastro = models.DateTimeField(default=timezone.now)




