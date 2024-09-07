from django.db import models

# Create your models here.

class Animal(models.Model):

    nome_animal = models.CharField(max_length=100)
    especie = models.CharField(max_length=100)
    raca = models.CharField(max_length=100)
    peso = models.FloatField()
    idade = models.FloatField()
    rfid = models.CharField(max_length=20)
    
class Funcionario(models.Model):
    codigoFuncionario = models.AutoField,
    nomeFuncionario = models.CharField(max_length=100),
    loginFuncionario = models.CharField(max_length=100),
    senhaFuncionario = models.CharField(max_length=100)

class Tutor(models.Model):
    codigotutor = models.AutoField(primary_key=True)
    nometutor = models.CharField(max_length=100, unique=True)
    cpf = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    rg = models.CharField(max_length=100)
    cadunico = models.CharField(max_length=100)