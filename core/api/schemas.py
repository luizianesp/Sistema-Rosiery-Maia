from ninja import Schema, File # Importe File para usar UploadFile
from typing import List, Optional
from datetime import datetime

from ninja.files import UploadedFile


class AreaPesquisaSchema(Schema):
    id: int
    nome: str
    descricao: Optional[str]
    # Certifique-se de que 'topico' está definido como uma lista de TopicosSchema
    topico: List['TopicosSchema'] = []

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
    imagem: Optional[str] # Para saída, é a URL da imagem
    categoria: str
    financiamento: Optional[str]
    equipe: Optional[str]
    objetivos: List[ObjetivosSchema] = [] # Lista de objetos ObjetivosSchema

    class Config:
        from_attributes = True


class ProjetoIn(Schema):
    titulo: str
    descricao: str
    # Para entrada, a imagem será um arquivo UploadedFile, não uma string de URL.
    # Usaremos Optional[File[UploadedFile]] para aceitar o upload de arquivo.
    imagem: Optional[File[UploadedFile]] = None
    categoria: str
    financiamento: Optional[str]
    equipe: Optional[str]
    # Se você precisar associar objetivos diretamente via este formulário,
    # precisaria de um campo como objetivos_ids: List[int] = [] e lógica adicional.
    # Por enquanto, focaremos nos campos diretos e na imagem.


class PublicacaoSchema(Schema):
    id: int
    categoria: str
    titulo: str
    autores: str
    ano: int
    publicado_no: str
    descricao: Optional[str]
    arquivo: Optional[str] # Para saída, ainda será uma URL (string)
    link: str

    class Config:
        from_attributes = True


# Para a entrada (POST/PUT), o 'arquivo' deve ser UploadedFile
class PublicacaoIn(Schema):
    categoria: str
    titulo: str
    autores: str
    ano: int
    publicado_no: str
    descricao: Optional[str]
    arquivo: Optional[File[UploadedFile]] = None # <--- MUDADO DE VOLTA PARA UploadedFile
    link: str

class OrientacaoSchema(Schema):
    id: int
    status: str
    aluno: str
    categoria: str
    trabalho: str
    descricao: Optional[str]
    imagem: Optional[str] # Para saída, continua sendo string (URL)

    class Config:
        from_attributes = True


class OrientacaoIn(Schema):
    status: str
    aluno: str
    categoria: str
    trabalho: str
    descricao: Optional[str]
    imagem: Optional[File[UploadedFile]] = None # <--- ALTERADO PARA UploadedFile para entrada!


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
