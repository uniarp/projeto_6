from django import forms
from .models import Tutor

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
            'telefone': 'Telefone',
            'tipo': 'Tipo',
            'raca': 'Raça',
            'idade': 'Idade',
            'especie': 'Espécie',
            'peso': 'Peso médio',
            'rfid': 'N° RFID',
            'castrado': 'Castrado'
        }
