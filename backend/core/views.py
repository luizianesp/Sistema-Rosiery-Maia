from django.shortcuts import render, redirect
from .models import AreaPesquisa, Projeto, Publicacao, Orientacao
from .forms import ContatoForm


def home(request):
    return render(request, 'core/home.html')

def areas_pesquisa(request):
    areas = AreaPesquisa.objects.all()
    return render(request, 'core/areas_pesquisa.html', {'areas': areas})

def projetos(request):
    projetos = Projeto.objects.all()
    return render(request, 'core/projetos.html', {'projetos': projetos})

def publicacoes(request):
    publicacoes = Publicacao.objects.all()
    return render(request, 'core/publicacoes.html', {'publicacoes': publicacoes})

def orientacoes(request):
    orientacoes = Orientacao.objects.all()
    return render(request, 'core/orientacoes.html', {'orientacoes': orientacoes})

def contato(request):
    if request.method == 'POST':
        form = ContatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contato')
    else:
        form = ContatoForm()
    return render(request, 'core/contato.html', {'form': form})