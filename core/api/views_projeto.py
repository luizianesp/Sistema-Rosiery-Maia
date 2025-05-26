from ninja import Router
from typing import List
from core.models import Projeto
from core.api.schemas import ProjetoSchema, ProjetoIn
from django.shortcuts import get_object_or_404

router = Router(tags=["Projeto"])

@router.get("/", response=List[ProjetoSchema])
def list_projetos(request):
    return Projeto.objects.all()

@router.get("/{id}", response=ProjetoSchema)
def get_projeto(request, id: int):
    return get_object_or_404(Projeto, id=id)

@router.post("/", response=ProjetoSchema)
def create_projeto(request, data: ProjetoIn):
    return Projeto.objects.create(**data.dict())

@router.put("/{id}", response=ProjetoSchema)
def update_projeto(request, id: int, data: ProjetoIn):
    projeto = get_object_or_404(Projeto, id=id)
    for attr, value in data.dict().items():
        setattr(projeto, attr, value)
    projeto.save()
    return projeto

@router.delete("/{id}")
def delete_projeto(request, id: int):
    projeto = get_object_or_404(Projeto, id=id)
    projeto.delete()
    return {"success": True}
