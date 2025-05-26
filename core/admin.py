from django.contrib import admin
from django.contrib.auth.models import User
from .models import *

# Register your models here.
admin.site.register(AreaPesquisa)
admin.site.register(Projeto)
admin.site.register(Publicacao)
admin.site.register(Orientacao)
admin.site.register(MensagemContato)