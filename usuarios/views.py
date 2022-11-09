from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # para facilitar a criação dos forms e validações
from django.contrib import messages
from .forms import UserRegisterForm

# Create your views here.
def novo_usuario(request):
    # Verificar tipo de info vinda do site, validar, informar se user criado ou não, e salvar no DB
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST) # Pega as infos enviadas do site para o servidor
        if formulario.is_valid():
            #salvar no DB
            formulario.save()
            # informar o usuario
            usuario = formulario.cleaned_data.get('username')
            messages.success(request,f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')
            
    else:
        formulario = UserRegisterForm() # Cria form vazio caso não seja post

    return render(request,'usuarios/registrar.html', {'formulario': formulario})