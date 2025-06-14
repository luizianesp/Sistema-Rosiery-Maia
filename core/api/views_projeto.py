from ninja import Router
from typing import List
from core.models import Projeto, Objetivos
from core.api.schemas import ProjetoSchema, ProjetoIn, ObjetivosSchema
from django.shortcuts import get_object_or_404
from django.db.models import Prefetch

router = Router(tags=["Projeto"])


@router.get("/", response=List[ProjetoSchema])
def list_projetos(request):
    return Projeto.objects.prefetch_related(
        Prefetch('objetivos', queryset=Objetivos.objects.all())  # <-- NOME CORRIGIDO AQUI!
    ).all()


@router.get("/{id}", response=ProjetoSchema)
def get_projeto(request, id: int):
    return get_object_or_404(
        Projeto.objects.prefetch_related(
            Prefetch('objetivos', queryset=Objetivos.objects.all())  # <-- NOME CORRIGIDO AQUI!
        ),
        id=id
    )


@router.post("/", response=ProjetoSchema)
def create_projeto(request, data: ProjetoIn):
    projeto = Projeto.objects.create(
        titulo=data.titulo,
        descricao=data.descricao,
        imagem=data.imagem,
        categoria=data.categoria,
        financiamento=data.financiamento,
        equipe=data.equipe
    )
    # Se você implementar a lógica de associar objetivos na criação, ela viria aqui.
    # Ex: if data.objetivos_ids:
    #         objetivos_to_add = Objetivos.objects.filter(id__in=data.objetivos_ids)
    #         projeto.objetivos.set(objetivos_to_add) # <-- USAR 'objetivos' AQUI
    return projeto


@router.put("/{id}", response=ProjetoSchema)
def update_projeto(request, id: int, data: ProjetoIn):
    projeto = get_object_or_404(Projeto, id=id)
    for attr, value in data.dict(exclude_unset=True).items():
        if attr not in ['objetivos_ids']:  # Se você tivesse objetivos_ids na entrada
            setattr(projeto, attr, value)
    projeto.save()

    # Se você implementar a lógica de associar objetivos na atualização, ela viria aqui.
    # Ex: if 'objetivos_ids' in data.dict(exclude_unset=True):
    #         objetivos_to_set = Objetivos.objects.filter(id__in=data.objetivos_ids)
    #         projeto.objetivos.set(objetivos_to_set) # <-- USAR 'objetivos' AQUI

    return projeto


@router.delete("/{id}")
def delete_projeto(request, id: int):
    projeto = get_object_or_404(Projeto, id=id)
    projeto.delete()
    return {"success": True}
