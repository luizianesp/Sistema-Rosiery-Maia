from django.db import models

class AreaPesquisa(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    CATEGORIA_CHOICES = [
        ('Pesquisa', 'Pesquisa'),
        ('Ensino', 'Ensino'),
        ('Extensao', 'Extensão'),
    ]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/')
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)

    def __str__(self):
        return self.titulo

class Publicacao(models.Model):
    titulo = models.CharField(max_length=200)
    link = models.URLField()

    def __str__(self):
        return self.titulo

class Orientacao(models.Model):
    aluno = models.CharField(max_length=100)
    trabalho = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.aluno} - {self.trabalho}"

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()
    enviada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome