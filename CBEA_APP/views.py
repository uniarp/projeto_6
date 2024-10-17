from django.shortcuts import render
from .forms import Agendar_consulta, TutorForm, AnimalForm

# Tela de Inicio
def home(request):
    if request.method == 'POST':
        return render(request, 'telas/form.html')
    return render(request, 'telas/form.html')

def login(request):
    if request.method == 'POST':
        return render(request, 'registration/login.html')
    else:
        return render(request, 'registration/login.html')


# Tela de cadastrar Tutor
def tutor_form(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()  # Salvar o formulário
            # Redirecionar para a mesma página com uma variável de contexto
            return render(request, 'telas/form.html', {'form': TutorForm(), 'show_modal': True})
    else:
        form = TutorForm()
    return render(request, 'telas/form.html', {'form': form, 'show_modal': False})

def Agendar_consulta_form(request):
    if request.method == 'POST':
        form = Agendar_consultaForm(request.POST)
        if form.is_valid():
            form.save()  # Salvar o formulário
            # Redirecionar para a mesma página com uma variável de contexto
            return render(request, 'telas/form.html', {'form': Agendar_consultaForm(), 'show_modal': True})
    else:
        form = Tutor2Form()
    return render(request, 'telas/form.html', {'form': form, 'show_modal': False})

# Tela de cadastrar Animal
def animal_form(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()  # Salvar o formulário
            # Redirecionar para a mesma página com uma variável de contexto
            return render(request, 'telas/form.html', {'form': AnimalForm(), 'show_modal': True})
    else:
        form = AnimalForm()
    return render(request, 'telas/form.html', {'form': form, 'show_modal': False})

def login2_view(request):
    return render(request, 'registration/login2.html')