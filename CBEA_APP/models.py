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

