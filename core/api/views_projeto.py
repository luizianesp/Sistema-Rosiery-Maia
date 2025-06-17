from ninja import Router, File, Form  # Importe Form
from typing import List, Optional
from core.models import Projeto, Objetivos  # Importe Objetivos
from core.api.schemas import ProjetoSchema, ProjetoIn, ObjetivosSchema  # Importe ObjetivosSchema
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch  # Importe Prefetch
from ninja.files import UploadedFile  # Mantenha UploadedFile

router = Router(tags=["Projeto"])


@router.get("/", response=List[ProjetoSchema])
def list_projetos(request):
    # Use prefetch_related para carregar os objetivos relacionados de forma eficiente
    return Projeto.objects.prefetch_related(
        Prefetch('objetivos', queryset=Objetivos.objects.all())
    ).all()


@router.get("/{id}", response=ProjetoSchema)
def get_projeto(request, id: int):
    # Carrega um único projeto com seus objetivos relacionados
    return get_object_or_404(
        Projeto.objects.prefetch_related(
            Prefetch('objetivos', queryset=Objetivos.objects.all())
        ),
        id=id
    )


# MODIFICADO: Receber os campos de ProjetoIn via Form(...) e a imagem separadamente
@router.post("/", response=ProjetoSchema)
def create_projeto(
        request,
        form_data: ProjetoIn = Form(...),  # Recebe dados do formulário
        imagem: Optional[UploadedFile] = File(None)  # Recebe a imagem
):
    try:
        projeto = Projeto(
            titulo=form_data.titulo,
            descricao=form_data.descricao,
            categoria=form_data.categoria,
            financiamento=form_data.financiamento,
            equipe=form_data.equipe,
            imagem=imagem  # Atribua o objeto UploadedFile
        )
        projeto.full_clean()  # Validação do modelo Django
        projeto.save()
        # Se 'objetivos_ids' fosse enviado, a lógica de associar viria aqui
        return projeto
    except Exception as e:
        print(f"Erro ao criar projeto: {e}")
        raise e


# MODIFICADO: Receber os campos de ProjetoIn via Form(...) para PUT
@router.put("/{id}", response=ProjetoSchema)
def update_projeto(
        request,
        id: int,
        form_data: ProjetoIn = Form(...),  # Recebe dados do formulário
        imagem: Optional[UploadedFile] = File(None)  # Recebe a nova imagem (se houver)
):
    projeto = get_object_or_404(Projeto, id=id)

    projeto.titulo = form_data.titulo
    projeto.descricao = form_data.descricao
    projeto.categoria = form_data.categoria
    projeto.financiamento = form_data.financiamento
    projeto.equipe = form_data.equipe

    # Lógica de imagem: Se uma nova imagem foi enviada, atribua-a
    if imagem:
        projeto.imagem = imagem
    # Nota: Se o frontend não enviar um arquivo novo, 'imagem' será None.
    # Se a intenção é remover a imagem existente sem substituí-la,
    # seria necessário um checkbox 'remover_imagem' no frontend e lógica aqui.
    # Por exemplo: if 'clear_image' in form_data and form_data.clear_image: projeto.imagem = None

    try:
        projeto.full_clean()
        projeto.save()
        # Se 'objetivos_ids' fosse enviado, a lógica de atualizar viria aqui
        return projeto
    except Exception as e:
        print(f"Erro ao atualizar projeto {id}: {e}")
        raise e


@router.delete("/{id}")
def delete_projeto(request, id: int):
    projeto = get_object_or_404(Projeto, id=id)
    projeto.delete()
    return {"success": True}
