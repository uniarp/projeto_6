# Register your models here.

from django.contrib import admin
from .models import Tutor, Animal

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nome_tutor', 'numero_cad', 'cpf', 'cidade', 'estado', 'endereco', 'email', 'telefone')
    
@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    list_display = ('nome_animal','tipo', 'raca', 'idade', 'especie', 'peso', 'rfid', 'castrado')