from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    data_evento = models.DateTimeField(verbose_name='Data do Evento')# nome que vai aparecer na agenda
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Usuário')# relaciona o evento com o usuário que o criou
    
    class Meta:
        db_table = 'evento'# especifica o nome da tabela no banco de dados seja 'evento'

    def __str__(self):
        return self.titulo # Retorna o título do evento quando o objeto é convertido para string 
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M hs')# Formata a data do evento para o formato dia/mês/ano posso colocar na frente %H:%M para imprimir também hora:minuto
