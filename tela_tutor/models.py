from django.db import models

# Create your models here.
from django.db import models

class Tutor(models.Model):
    nome_tutor = models.CharField(max_length=100)
    numero_cad = models.CharField(max_length=20)
    cpf = models.CharField(max_length=11)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    email = models.EmailField()
    telefone = models.CharField(max_length=15)
    tipo = models.CharField(max_length=20)
    raca = models.CharField(max_length=50)
    idade = models.IntegerField()
    especie = models.CharField(max_length=50)
    peso = models.CharField(max_length=10)
    rfid = models.CharField(max_length=50)
    castrado = models.CharField(max_length=3)

    def __str__(self):
        return self.nome_tutor
