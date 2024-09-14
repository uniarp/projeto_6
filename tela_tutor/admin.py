# Register your models here.

from django.contrib import admin
from .models import Tutor

@admin.register(Tutor)
class TutorAdmin(admin.ModelAdmin):
    list_display = ('nome_tutor', 'numero_cad', 'cpf', 'cidade', 'estado', 'endereco', 'email', 'telefone', 'tipo', 'raca', 'idade', 'especie', 'peso', 'rfid', 'castrado')