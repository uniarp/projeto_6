# Register your models here.

from django.contrib import admin
from .models import Agendar_consulta, Tutor, Animal

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nome_tutor', 'numero_cad', 'cpf', 'cidade', 'estado', 'endereco', 'email', 'telefone')

@admin.register(Agendar_consulta)
class Agendar_consultaAdmin(admin.ModelAdmin):
    list_display = ('nome_tutor', 'nome_animal', 'telefone', 'data', 'hora')
    
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome_animal', 'raca', 'idade', 'especie', 'peso', 'rfid', 'castrado')