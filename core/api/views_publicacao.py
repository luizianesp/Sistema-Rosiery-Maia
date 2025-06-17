from ninja import Router
from typing import List
from core.models import Publicacao
from core.api.schemas import PublicacaoSchema, PublicacaoIn
from django.shortcuts import get_object_or_404

router = Router(tags=["Publicacao"])

@router.get("/", response=List[PublicacaoSchema])
def list_publicacoes(request):
    # Retorna todas as publicações. O PublicacaoSchema se encarregará da serialização dos campos.
    return Publicacao.objects.all()

@router.get("/{id}", response=PublicacaoSchema)
def get_publicacao(request, id: int):
    # Retorna uma publicação específica.
    return get_object_or_404(Publicacao, id=id)

@router.post("/", response=PublicacaoSchema)
def create_publicacao(request, data: PublicacaoIn):
    # Cria uma nova publicação com os dados fornecidos.
    # Os campos de FileField (arquivo) e URLField (link) serão tratados aqui.
    return Publicacao.objects.create(**data.dict())

@router.put("/{id}", response=PublicacaoSchema)
def update_publicacao(request, id: int, data: PublicacaoIn):
    publicacao = get_object_or_404(Publicacao, id=id)
    # Atualiza os campos da publicação.
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(publicacao, attr, value)
    publicacao.save()
    return publicacao

@router.delete("/{id}")
def delete_publicacao(request, id: int):
    publicacao = get_object_or_404(Publicacao, id=id)
    publicacao.delete()
    return {"success": True}
