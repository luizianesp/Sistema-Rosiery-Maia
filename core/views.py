from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import AreaPesquisa, Projeto, Publicacao, Orientacao
from .forms import ContatoForm

# Importações para autenticação
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages  # Para exibir mensagens de sucesso/erro


def home(request):
    return render(request, 'core/index.html')


def areas_pesquisa(request):
    areas = AreaPesquisa.objects.all()
    return render(request, 'core/pesquisa.html', {'areas': areas})


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
    form = ContatoForm()
    return render(request, 'core/contato.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        # Instancia o formulário de autenticação com os dados submetidos
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Obtém o username e password do formulário validado
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            # Autentica o usuário
            user = authenticate(username=username, password=password)

            if user is not None:
                # Se o usuário foi autenticado com sucesso, faz o login
                login(request, user)
                messages.success(request, f'Bem-vindo(a), {username}!')
                return redirect('dashboard')  # Redireciona para a URL definida em LOGIN_REDIRECT_URL
            else:
                # Se a autenticação falhou
                messages.error(request, 'Nome de usuário ou senha inválidos.')
        else:
            # Se o formulário não for válido (ex: campos vazios)
            messages.error(request, 'Por favor, insira um nome de usuário e senha válidos.')
    else:
        # Se for uma requisição GET, exibe o formulário de login vazio
        form = AuthenticationForm()

    # Renderiza a página de login, passando o formulário e as mensagens
    return render(request, 'core/login.html', {'form': form})


def user_logout(request):
    # Faz o logout do usuário
    logout(request)
    messages.info(request, 'Você foi desconectado(a).')
    return redirect('login')  # Redireciona para a URL definida em LOGOUT_REDIRECT_URL

@login_required
def admin_dashboard(request):
    return render(request, 'core/dashboard.html')

# === NOVAS VIEWS ESPECÍFICAS PARA CADA GERENCIAMENTO ===
@login_required
def admin_publicacoes(request):
    return render(request, 'core/gerenciar_publicacoes.html')

@login_required
def admin_projetos(request):
    return render(request, 'core/gerenciar_projetos.html')

@login_required
def admin_orientacoes(request):
    return render(request, 'core/gerenciar_orientacoes.html')

@login_required
def admin_mensagens(request):
    # Pode ser útil passar as mensagens aqui se você não for usar uma API Ninja para listar
    # mensagens diretamente no frontend. Se usar API, apenas renderize o template.
    # Exemplo: messages = MensagemContato.objects.all()
    return render(request, 'core/mensagens_contato.html') # , {'messages': messages}

@login_required
def admin_configuracoes(request):
    return render(request, 'core/configuracoes_site.html')

@login_required
def admin_areas_pesquisa(request):
    return render(request, 'core/gerenciar_areas_pesquisa.html')