from django.db import models

class Topicos(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome

class Objetivos(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome



class AreaPesquisa(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    topico = models.ManyToManyField(Topicos, blank=True)

    def __str__(self):
        return self.nome

class Projeto(models.Model):
    CATEGORIA_CHOICES = [
        ('Pesquisa', 'Pesquisa'),
        ('Ensino', 'Ensino'),
        ('Extensão', 'Extensão'),
    ]
    titulo = models.CharField(max_length=200)
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='projetos/', blank=True, null=True)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES)
    financiamento = models.CharField(max_length=100, blank=True, null=True)
    equipe = models.TextField(blank=True, null=True)
    objetivos = models.ManyToManyField(Objetivos, blank=True)

    def __str__(self):
        return self.titulo

class Publicacao(models.Model):
    CATEGORIA_CHOICES = [
        ('Artigo', 'Artigo'),
        ('Livro', 'Livro'),
        ('Capitulo', 'Capitulo'),
        ('Conferencia', 'Conferencia'),
    ]
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='Artigo')
    titulo = models.CharField(max_length=200)
    autores = models.CharField(max_length=100, default="Maia R")
    ano = models.IntegerField(default=2025)
    publicado_no = models.CharField(max_length=100, default="Revista")
    descricao = models.TextField(blank=True, null=True)
    arquivo = models.FileField(upload_to='publicacao/', blank=True, null=True)
    link = models.URLField()

    def __str__(self):
        return self.titulo

class Orientacao(models.Model):
    STATUS_CHOICES = [
        ('em Andamento', 'em Andamento'),
        ('Concluido', 'Concluido'),
    ]

    CATEGORIA_CHOICES = [
        ('Doutorado', 'Doutorado'),
        ('Mestrado', 'Mestrado'),
        ('TCC', 'TCC'),
        ('Iniciacao Cientifica', 'Iniciacao Cientifica'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='em Andamento')
    aluno = models.CharField(max_length=100)
    categoria = models.CharField(max_length=20, choices=CATEGORIA_CHOICES, default='TCC')
    trabalho = models.CharField(max_length=200)
    descricao = models.TextField(blank=True, null=True)
    imagem = models.ImageField(upload_to='orientacao/', blank=True, null=True)

    def __str__(self):
        return f"{self.aluno} - {self.trabalho}"

class MensagemContato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    assunto = models.CharField(max_length=100)
    mensagem = models.TextField()
    noticias = models.BooleanField(default=False)
    enviada_em = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.nome
