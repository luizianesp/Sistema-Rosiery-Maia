from ninja import Router
from typing import List
from core.models import AreaPesquisa
from core.api.schemas import AreaPesquisaSchema, AreaPesquisaIn
from django.shortcuts import get_object_or_404

router = Router(tags=["Área de Pesquisa"])

@router.get("/", response=List[AreaPesquisaSchema])
def list_areas(request):
    return AreaPesquisa.objects.all()

@router.get("/{id}", response=AreaPesquisaSchema)
def get_area(request, id: int):
    return get_object_or_404(AreaPesquisa, id=id)

@router.post("/", response=AreaPesquisaSchema)
def create_area(request, data: AreaPesquisaIn):
    return AreaPesquisa.objects.create(**data.dict())

@router.put("/{id}", response=AreaPesquisaSchema)
def update_area(request, id: int, data: AreaPesquisaIn):
    area = get_object_or_404(AreaPesquisa, id=id)
    for attr, value in data.dict().items():
        setattr(area, attr, value)
    area.save()
    return area

@router.delete("/{id}")
def delete_area(request, id: int):
    area = get_object_or_404(AreaPesquisa, id=id)
    area.delete()
    return {"success": True}
