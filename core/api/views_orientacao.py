from ninja import Router
from typing import List
from core.models import Orientacao
from core.api.schemas import OrientacaoSchema, OrientacaoIn
from django.shortcuts import get_object_or_404

router = Router(tags=["Orientacao"])

@router.get("/", response=List[OrientacaoSchema])
def list_orientacoes(request):
    # O OrientacaoSchema se encarregará de serializar todos os campos.
    return Orientacao.objects.all()

@router.get("/{id}", response=OrientacaoSchema)
def get_orientacao(request, id: int):
    return get_object_or_404(Orientacao, id=id)

@router.post("/", response=OrientacaoSchema)
def create_orientacao(request, data: OrientacaoIn):
    # Os novos campos serão passados através de data.dict()
    return Orientacao.objects.create(**data.dict())

@router.put("/{id}", response=OrientacaoSchema)
def update_orientacao(request, id: int, data: OrientacaoIn):
    orientacao = get_object_or_404(Orientacao, id=id)
    # Atualiza os campos da orientação
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(orientacao, attr, value)
    orientacao.save()
    return orientacao

@router.delete("/{id}")
def delete_orientacao(request, id: int):
    orientacao = get_object_or_404(Orientacao, id=id)
    orientacao.delete()
    return {"success": True}
