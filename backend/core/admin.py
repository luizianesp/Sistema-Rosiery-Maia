from django.contrib import admin
from .models import AreaPesquisa, Projeto, Publicacao, Orientacao, MensagemContato

admin.site.register(AreaPesquisa)
admin.site.register(Projeto)
admin.site.register(Publicacao)
admin.site.register(Orientacao)
admin.site.register(MensagemContato)

