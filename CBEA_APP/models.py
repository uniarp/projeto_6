from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Animal(models.Model):
    codigo_animal = models.AutoField,
    nome_animal = models.CharField(max_length=100)
    raca = models.CharField(max_length=50)
    idade = models.IntegerField()
    especie = models.CharField(max_length=50)
    peso = models.CharField(max_length=10)
    rfid = models.CharField(max_length=50)
    castrado = models.BooleanField()

    def __str__(self):
        return self.nome_animal



class Funcionario(models.Model):
    codigo_funcionario = models.AutoField,
    nome_funcionario = models.CharField(max_length=100),
    usuario_funcionario = models.CharField(max_length=100),
    senha_funcionario = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_funcionario

class Tutor(models.Model):
    nome_tutor = models.CharField(max_length=100)
    numero_cad = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)

    def __str__(self):
        return self.nome_tutor