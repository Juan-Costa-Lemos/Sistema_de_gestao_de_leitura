from django.shortcuts import render,redirect
from .forms import LeituraForm
from .models import Leituras

# Create your views here.


def home(request):

    return render(request,'gestao_leitura/home.html',context={})


def minhas_leituras(request):
    dados = {
        'dados':Leituras.objects.all()
    }
    return render(request,'gestao_leitura/minhas_leituras.html', context=dados)

def detalhe(request, id_leituras):
    dados = {
        'dados' : Leituras.objects.get(pk=id_leituras)
    }
    return render(request,'gestao_leitura/detalhe.html', dados)

def criar(request,):
    if request.method =='POST':
        leituras_form = LeituraForm(request.POST)
        if leituras_form.is_valid():
            leituras_form.save()
        return redirect('minhas_leituras')        
    leituras_form = LeituraForm()
    formulario = {
        'formulario': leituras_form
    }
    return render(request, 'gestao_leitura/nova_leitura.html',context=formulario)


def editar(request, id_leituras):
    leitura = Leituras.objects.get(pk=id_leituras)
    if request.method == 'GET':
        formulario = LeituraForm(instance=leitura)
        return render(request,'gestao_leitura/nova_leitura.html',{'formulario':formulario})
    else:
        if request.method == 'POST':
            formulario = LeituraForm(request.POST, instance=leitura)
        if formulario.is_valid():
            formulario.save()
        return redirect('minhas_leituras')

def excluir(request,id_leituras):
    leitura = Leituras.objects.get(pk=id_leituras)
    if request.method == 'POST':
        leitura.delete()
        return redirect('minhas_leituras')
    return render(request,'gestao_leitura/confirmar_exclusao.html',{'item':leitura})