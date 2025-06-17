from ninja import Router, File, Form  # <--- Importe Form
from typing import List, Optional
from core.models import Publicacao
from core.api.schemas import PublicacaoSchema, PublicacaoIn  # PublicacaoIn é o schema base
from django.shortcuts import get_object_or_404
from ninja.files import UploadedFile

router = Router(tags=["Publicacao"])


@router.get("/", response=List[PublicacaoSchema])
def list_publicacoes(request):
    return Publicacao.objects.all()


@router.get("/{id}", response=PublicacaoSchema)
def get_publicacao(request, id: int):
    return get_object_or_404(Publicacao, id=id)


# MODIFICADO: Receber os campos de PublicacaoIn via Form(...) e o arquivo separadamente
@router.post("/", response=PublicacaoSchema)
def create_publicacao(
        request,
        # Use Form(PublicacaoIn) para que o Ninja espere os campos do schema diretamente do FormData
        form_data: PublicacaoIn = Form(...),  # <--- AGORA O ALIAS É 'form_data' E É OBRIGATÓRIO VIR DO FORM
        arquivo: Optional[UploadedFile] = File(None)
):
    try:
        publicacao = Publicacao(
            categoria=form_data.categoria,
            titulo=form_data.titulo,
            autores=form_data.autores,
            ano=form_data.ano,
            publicado_no=form_data.publicado_no,
            descricao=form_data.descricao,
            link=form_data.link,
            arquivo=arquivo  # Atribua o objeto UploadedFile diretamente
        )
        publicacao.full_clean()
        publicacao.save()
        return publicacao
    except Exception as e:
        print(f"Erro ao criar publicação: {e}")
        raise e


# MODIFICADO: Receber os campos de PublicacaoIn via Form(...) para PUT
@router.put("/{id}", response=PublicacaoSchema)
def update_publicacao(
        request,
        id: int,
        form_data: PublicacaoIn = Form(...),  # <--- AGORA O ALIAS É 'form_data' E É OBRIGATÓRIO VIR DO FORM
        arquivo: Optional[UploadedFile] = File(None)
):
    publicacao = get_object_or_404(Publicacao, id=id)

    # Atualiza os campos do modelo com base nos dados do form_data
    publicacao.categoria = form_data.categoria
    publicacao.titulo = form_data.titulo
    publicacao.autores = form_data.autores
    publicacao.ano = form_data.ano
    publicacao.publicado_no = form_data.publicado_no
    publicacao.descricao = form_data.descricao
    publicacao.link = form_data.link

    # Lógica de arquivo: Se um novo arquivo foi enviado, atribua-o
    if arquivo:
        publicacao.arquivo = arquivo
    # IMPORTANTE: Se o usuário quer remover o arquivo existente, e NÃO um novo foi enviado,
    # você precisaria de um checkbox 'remover_arquivo' no frontend e uma lógica aqui.
    # A lógica 'elif data.arquivo is not None and not arquivo:' que eu coloquei antes
    # é mais para cenários onde 'arquivo' pode vir como nulo via JSON, o que não
    # acontece com input type="file" vazio em FormData.
    # Para remover: `if 'clear_arquivo' in form_data and form_data.clear_arquivo:`
    # publicacao.arquivo = None

    try:
        publicacao.full_clean()
        publicacao.save()
        return publicacao
    except Exception as e:
        print(f"Erro ao atualizar publicação {id}: {e}")
        raise e


@router.delete("/{id}")
def delete_publicacao(request, id: int):
    publicacao = get_object_or_404(Publicacao, id=id)
    publicacao.delete()
    return {"success": True}
