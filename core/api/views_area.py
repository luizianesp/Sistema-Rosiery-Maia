# views_area.py (ATUALIZADO)

from ninja import Router
from typing import List
from core.models import AreaPesquisa, Topicos # Importe Topicos
from core.api.schemas import AreaPesquisaSchema, AreaPesquisaIn, TopicosSchema # Importe TopicosSchema
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch # Importe Prefetch

router = Router(tags=["Área de Pesquisa"])

@router.get("/", response=List[AreaPesquisaSchema])
def list_areas(request):
    return AreaPesquisa.objects.prefetch_related(
        Prefetch('topico', queryset=Topicos.objects.all())
    ).all()

@router.get("/{id}", response=AreaPesquisaSchema)
def get_area(request, id: int):
    return get_object_or_404(
        AreaPesquisa.objects.prefetch_related(
            Prefetch('topico', queryset=Topicos.objects.all())
        ),
        id=id
    )

@router.post("/", response=AreaPesquisaSchema)
def create_area(request, data: AreaPesquisaIn):
    area = AreaPesquisa.objects.create(
        nome=data.nome,
        descricao=data.descricao
    )
    if data.topicos_ids: # Se IDs de tópicos foram fornecidos
        topicos = Topicos.objects.filter(id__in=data.topicos_ids)
        area.topico.set(topicos) # Associa os tópicos
    return area

@router.put("/{id}", response=AreaPesquisaSchema)
def update_area(request, id: int, data: AreaPesquisaIn):
    area = get_object_or_404(AreaPesquisa, id=id)
    # Atualiza campos simples
    for attr, value in data.dict(exclude_unset=True).items():
        if attr != 'topicos_ids': # Não use setattr para ManyToMany
            setattr(area, attr, value)
    area.save()

    # Atualiza ManyToManyField 'topico'
    if data.topicos_ids is not None: # Se topicos_ids foi explicitamente fornecido (pode ser lista vazia)
        topicos = Topicos.objects.filter(id__in=data.topicos_ids)
        area.topico.set(topicos) # Seta os tópicos (remove os antigos e adiciona os novos)
    # Se data.topicos_ids for None (não enviado), a lista de tópicos existente permanece.
    # Se você quiser que a ausência de topicos_ids signifique remover todos, use:
    # else: area.topico.clear()

    return area

@router.delete("/{id}")
def delete_area(request, id: int):
    area = get_object_or_404(AreaPesquisa, id=id)
    area.delete()
    return {"success": True}

# NOVO ENDPOINT: Para listar todos os tópicos (útil para popular o select no frontend)
@router.get("/topicos/", response=List[TopicosSchema])
def list_topicos(request):
    return Topicos.objects.all()