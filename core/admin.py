from django.contrib import admin
from core.models import Evento

# Register your models here.
class EventoAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'data_evento', 'data_criacao')# Exibe os campos na lista de eventos

    list_filter = ('titulo', 'usuario', 'data_evento', 'data_criacao')# Adiciona filtros no banco de dados, vc pode filtrar por título, usuario, etc.

admin.site.register(Evento, EventoAdmin)# Registra o modelo Evento com a classe EventoAdmin no site de administração do Django
