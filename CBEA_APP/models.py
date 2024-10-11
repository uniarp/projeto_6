from django.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
import re

# Create your models here.

#############

def validate_nome_animal(value):
    if not value:
        raise ValidationError("O nome do animal não pode estar vazio.")

def validate_raca(value):
    if not value:
        raise ValidationError("A raça não pode estar vazia.")

def validate_especie(value):
    if not value:
        raise ValidationError("A espécie não pode estar vazia.")

def validate_idade(value):
    if value < 0:
        raise ValidationError("A idade deve ser um número positivo.")

def validate_peso(value):
    if not value.isdigit():
        raise ValidationError("O peso deve ser um número válido.")

def validate_rfid(value):
    if len(value) < 5:
        raise ValidationError("O RFID deve ter pelo menos 5 caracteres.")

def validate_idade_especie(especie, idade):
    if especie.lower() == 'gato' and idade > 30:
        raise ValidationError("A idade de um gato não pode exceder 30 anos.")
    elif especie.lower() == 'cachorro' and idade > 20:
        raise ValidationError("A idade de um cachorro não pode exceder 20 anos.")

class Animal(models.Model):
    codigo_animal = models.AutoField(primary_key=True)
    nome_animal = models.CharField(max_length=100, validators=[validate_nome_animal])
    raca = models.CharField(max_length=50, validators=[validate_raca])
    idade = models.IntegerField(validators=[validate_idade])
    especie = models.CharField(max_length=50, validators=[validate_especie])
    peso = models.CharField(max_length=10, validators=[validate_peso])
    rfid = models.CharField(max_length=50, validators=[validate_rfid])
    castrado = models.BooleanField()

    def clean(self):
        super().clean()  # Chama o clean dos campos individuais

        # Validação da idade dependendo da espécie
        validate_idade_especie(self.especie, self.idade)

    def save(self, *args, **kwargs):
        self.clean()  # Chamando o método de limpeza
        super().save(*args, **kwargs)

#################

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