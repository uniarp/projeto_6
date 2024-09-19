from django import forms
from .models import Tutor, Animal

class TutorForm(forms.ModelForm):
    class Meta:
        model = Tutor
        fields = '__all__'  # Inclui todos os campos do modelo
        labels = {
            'nome_tutor': 'Nome do tutor',
            'numero_cad': 'N° CAD único',
            'cpf': 'CPF',
            'cidade': 'Cidade',
            'estado': 'Estado',
            'endereco': 'Endereço',
            'email': 'Email',
            'telefone': 'Telefone'
        }

class AnimalForm(forms.ModelForm):
    class Meta:
        model = Animal
        fields = '__all__'
        labels = {
            'nome_animal': 'Nome do animal',
            'tipo': 'Tipo',
            'raca': 'Raça',
            'idade': 'Idade',
            'especie': 'Espécie',
            'peso': 'Peso médio',
            'rfid': 'N° RFID',
            'castrado': 'Castrado'
        }
