from ninja import Schema
from typing import Optional


class AreaPesquisaSchema(Schema):
    id: int
    nome: str


class AreaPesquisaIn(Schema):
    nome: str


class ProjetoSchema(Schema):
    id: int
    titulo: str
    descricao: str
    imagem: str
    categoria: str


class ProjetoIn(Schema):
    titulo: str
    descricao: str
    imagem: str
    categoria: str


class PublicacaoSchema(Schema):
    id: int
    titulo: str
    link: str


class PublicacaoIn(Schema):
    titulo: str
    link: str


class OrientacaoSchema(Schema):
    id: int
    aluno: str
    trabalho: str


class OrientacaoIn(Schema):
    aluno: str
    trabalho: str


class MensagemContatoSchema(Schema):
    id: int
    nome: str
    email: str
    assunto: str
    mensagem: str


class MensagemContatoIn(Schema):
    nome: str
    email: str
    assunto: str
    mensagem: str
