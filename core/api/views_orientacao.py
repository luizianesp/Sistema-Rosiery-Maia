from ninja import Router, File, Form  # Importe Form
from typing import List, Optional
from core.models import Orientacao
from core.api.schemas import OrientacaoSchema, OrientacaoIn
from django.shortcuts import get_object_or_404
from ninja.files import UploadedFile  # Mantenha UploadedFile

router = Router(tags=["Orientacao"])


@router.get("/", response=List[OrientacaoSchema])
def list_orientacoes(request):
    return Orientacao.objects.all()


@router.get("/{id}", response=OrientacaoSchema)
def get_orientacao(request, id: int):
    return get_object_or_404(Orientacao, id=id)


# MODIFICADO: Receber os campos via Form(...) e a imagem separadamente
@router.post("/", response=OrientacaoSchema)
def create_orientacao(
        request,
        form_data: OrientacaoIn = Form(...),  # Recebe dados do formulário
        imagem: Optional[UploadedFile] = File(None)  # Recebe a imagem
):
    try:
        orientacao = Orientacao(
            status=form_data.status,
            aluno=form_data.aluno,
            categoria=form_data.categoria,
            trabalho=form_data.trabalho,
            descricao=form_data.descricao,
            imagem=imagem  # Atribua o objeto UploadedFile
        )
        orientacao.full_clean()  # Validação do modelo Django
        orientacao.save()
        return orientacao
    except Exception as e:
        print(f"Erro ao criar orientação: {e}")
        raise e


# MODIFICADO: Receber os campos via Form(...) para PUT
@router.put("/{id}", response=OrientacaoSchema)
def update_orientacao(
        request,
        id: int,
        form_data: OrientacaoIn = Form(...),  # Recebe dados do formulário
        imagem: Optional[UploadedFile] = File(None)  # Recebe a nova imagem (se houver)
):
    orientacao = get_object_or_404(Orientacao, id=id)

    orientacao.status = form_data.status
    orientacao.aluno = form_data.aluno
    orientacao.categoria = form_data.categoria
    orientacao.trabalho = form_data.trabalho
    orientacao.descricao = form_data.descricao

    # Lógica de imagem: Se uma nova imagem foi enviada, atribua-a
    if imagem:
        orientacao.imagem = imagem
    # Se a intenção é remover a imagem existente sem substituí-la,
    # você precisaria de um checkbox 'remover_imagem' no frontend e lógica aqui.
    # Ex: if 'clear_image' in form_data and form_data.clear_image: orientacao.imagem = None

    try:
        orientacao.full_clean()
        orientacao.save()
        return orientacao
    except Exception as e:
        print(f"Erro ao atualizar orientação {id}: {e}")
        raise e


@router.delete("/{id}")
def delete_orientacao(request, id: int):
    orientacao = get_object_or_404(Orientacao, id=id)
    orientacao.delete()
    return {"success": True}
