from ninja import Schema
from typing import List, Optional


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
    objetivos: List[ObjetivosSchema] = [] # <-- NOME CORRIGIDO AQUI!

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
    titulo: str
    link: str

    class Config:
        from_attributes = True


class PublicacaoIn(Schema):
    titulo: str
    link: str


class OrientacaoSchema(Schema):
    id: int
    aluno: str
    trabalho: str

    class Config:
        from_attributes = True


class OrientacaoIn(Schema):
    aluno: str
    trabalho: str


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
