from django.shortcuts import render
from .forms import TutorForm

def tutor_form(request):
    if request.method == 'POST':
        form = TutorForm(request.POST)
        if form.is_valid():
            form.save()  # Salvar o formulário
            # Redirecionar para a mesma página com uma variável de contexto
            return render(request, 'tela_tutor/tutor_form.html', {'form': TutorForm(), 'show_modal': True})
    else:
        form = TutorForm()
    return render(request, 'tela_tutor/tutor_form.html', {'form': form, 'show_modal': False})
