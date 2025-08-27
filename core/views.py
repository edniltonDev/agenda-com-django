from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.

def index(request):
    return redirect('/agenda/')  # Redireciona para a página de agenda

def login_user(request):
    return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('/login/')

def submit_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('agenda')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return redirect('/login/')
    return redirect('/login/')

@login_required(login_url='/login/')  # Exige que o usuário esteja logado para acessar a lista de eventos#(login_url='/admin/login/')
def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario=usuario) # Filtra os eventos do usuário logado 
    dados = {
        'eventos': eventos,
    }
    return render(request, 'agenda.html', dados)

@login_required(login_url='/login/')  # Exige que o usuário esteja logado para acessar a página de evento
def evento(request):
    id_evento = request.GET.get('id')  # Obtém o ID do evento da URL
    dados = {}
    if id_evento:
        dados['evento'] = Evento.objects.get(id=id_evento)
    return render(request, 'evento.html', dados)

@login_required(login_url='/login/')  # Exige que o usuário esteja logado para submeter um evento
def submit_evento(request):
    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('data_evento')
        descricao = request.POST.get('descricao')
        usuario = request.user
        id_evento = request.POST.get('id_evento')
        if id_evento:
            Evento.objects.filter(id=id_evento).update(titulo=titulo,
                                                        data_evento=data_evento,
                                                        descricao=descricao,
                                                        usuario=usuario)
        else:    
            Evento.objects.create(
                titulo=titulo,
                data_evento=data_evento,
                descricao=descricao,
                usuario=usuario  # Adicione esta linha
            )
        return redirect('/')


@login_required(login_url='/login/')  # Exige que o usuário esteja logado para deletar um evento    
def delete_evento(request, id_evento): # Função para deletar um evento pelo ID
    usuario = request.user
    evento = Evento.objects.get(id=id_evento)
    if usuario == evento.usuario: # Verifica se o usuário logado é o dono do evento
        evento.delete()
        messages.success(request, 'Evento deletado com sucesso.')
    return redirect('/')

