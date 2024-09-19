from django.shortcuts import render
from .forms import TutorForm, AnimalForm

def tutor_form(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()  # Salvar o formulário
            # Redirecionar para a mesma página com uma variável de contexto
            return render(request, 'tela_formulario/form.html', {'form': TutorForm(), 'show_modal': True})
    else:
        form = TutorForm()
    return render(request, 'tela_formulario/form.html', {'form': form, 'show_modal': False})

def animal_form(request):
    if request.method == 'POST':
        form = AnimalForm(request.POST)
        if form.is_valid():
            form.save()  # Salvar o formulário
            # Redirecionar para a mesma página com uma variável de contexto
            return render(request, 'tela_formulario/form.html', {'form': AnimalForm(), 'show_modal': True})
    else:
        form = AnimalForm()
    return render(request, 'tela_formulario/form.html', {'form': form, 'show_modal': False})

