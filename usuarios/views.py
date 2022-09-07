from django.shortcuts import render, redirect
from .forms import UserRegisterForm
from django.contrib import messages

# Create your views here.

def novo_usuario(request):
    if request.method == 'POST':
        formulario = UserRegisterForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            usuario = formulario.cleaned_data.get('username')
            messages.success(request, f'O usuário {usuario} foi criado com sucesso!')
            return redirect('login')
    else:
        formulario = UserRegisterForm()
    return render(request,'usuario/registrar.html',{'formulario': formulario})

