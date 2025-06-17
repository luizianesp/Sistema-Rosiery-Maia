from ninja import Schema
from typing import List, Optional
from datetime import datetime # Importar datetime para o campo enviada_em

class AreaPesquisaSchema(Schema):
    id: int
    nome: str
    descricao: Optional[str]

    class Config:
        from_attributes = True


class AreaPesquisaIn(Schema):
    nome: str
    descricao: Optional[str]


class TopicosSchema(Schema):
    id: int
    nome: str

    class Config:
        from_attributes = True


class ObjetivosSchema(Schema):
    id: int
    nome: str

    class Config:
        from_attributes = True


class ProjetoSchema(Schema):
    id: int
    titulo: str
    descricao: str
    imagem: Optional[str]
    categoria: str
    financiamento: Optional[str]
    equipe: Optional[str]
    objetivos: List[ObjetivosSchema] = []

    class Config:
        from_attributes = True


class ProjetoIn(Schema):
    titulo: str
    descricao: str
    imagem: Optional[str]
    categoria: str
    financiamento: Optional[str]
    equipe: Optional[str]


class PublicacaoSchema(Schema):
    id: int
    categoria: str # Novo campo
    titulo: str
    autores: str # Novo campo
    ano: int # Novo campo
    publicado_no: str # Novo campo
    descricao: Optional[str] # Novo campo, opcional
    arquivo: Optional[str] # Novo campo para FileField, opcional
    link: str

    class Config:
        from_attributes = True


class PublicacaoIn(Schema):
    categoria: str
    titulo: str
    autores: str
    ano: int
    publicado_no: str
    descricao: Optional[str]
    arquivo: Optional[str]
    link: str


class OrientacaoSchema(Schema):
    id: int
    status: str
    aluno: str
    categoria: str # Garanta que este campo está aqui e é do tipo str
    trabalho: str
    descricao: Optional[str]
    imagem: Optional[str]

    class Config:
        from_attributes = True


class OrientacaoIn(Schema):
    status: str
    aluno: str
    categoria: str
    trabalho: str
    descricao: Optional[str]
    imagem: Optional[str]


class MensagemContatoSchema(Schema):
    id: int
    nome: str
    email: str
    assunto: str
    mensagem: str

    class Config:
        from_attributes = True


class MensagemContatoIn(Schema):
    nome: str
    email: str
    assunto: str
    mensagem: str
    noticias: bool  # Novo campo (entrada)
