from django.db import models

class Funcionario(models.Model):
    codigoFuncionario = models.AutoField,
    nomeFuncionario = models.CharField(max_length=100),
    loginFuncionario = models.CharField(max_length=100),
    senhaFuncionario = models.CharField(max_length=100)