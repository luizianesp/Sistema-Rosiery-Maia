from ninja import Router
from typing import List
from core.models import AreaPesquisa, Topicos # Importe Topicos
from core.api.schemas import AreaPesquisaSchema, AreaPesquisaIn, TopicosSchema # Importe TopicosSchema
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch # Importe Prefetch

router = Router(tags=["Área de Pesquisa"])

@router.get("/", response=List[AreaPesquisaSchema])
def list_areas(request):
    # MUITO IMPORTANTE: Use prefetch_related para carregar os tópicos
    # A string 'topico' deve corresponder ao nome do ManyToManyField no models.py
    return AreaPesquisa.objects.prefetch_related(
        Prefetch('topico', queryset=Topicos.objects.all())
    ).all()

@router.get("/{id}", response=AreaPesquisaSchema)
def get_area(request, id: int):
    # Também use prefetch_related para o endpoint de detalhe
    return get_object_or_404(
        AreaPesquisa.objects.prefetch_related(
            Prefetch('topico', queryset=Topicos.objects.all())
        ),
        id=id
    )

@router.post("/", response=AreaPesquisaSchema)
def create_area(request, data: AreaPesquisaIn):
    # Se você quiser adicionar tópicos na criação, precisaria de lógica extra aqui,
    # geralmente recebendo uma lista de IDs de tópicos. Por enquanto, criamos a área sem eles.
    area = AreaPesquisa.objects.create(
        nome=data.nome,
        descricao=data.descricao
    )
    return area

@router.put("/{id}", response=AreaPesquisaSchema)
def update_area(request, id: int, data: AreaPesquisaIn):
    area = get_object_or_404(AreaPesquisa, id=id)
    for attr, value in data.dict(exclude_unset=True).items():
        setattr(area, attr, value)
    area.save()
    # Se você quiser atualizar tópicos na edição, precisaria de lógica extra aqui,
    # ex: area.topico.set(data.topico_ids)
    return area

@router.delete("/{id}")
def delete_area(request, id: int):
    area = get_object_or_404(AreaPesquisa, id=id)
    area.delete()
    return {"success": True}
