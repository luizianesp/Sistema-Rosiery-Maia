from django import forms
from .models import MensagemContato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = MensagemContato
        # Adicione 'noticias' aqui
        fields = ['nome', 'email', 'assunto', 'mensagem', 'noticias']
