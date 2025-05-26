from ninja import Router
from typing import List
from core.models import MensagemContato
from core.api.schemas import MensagemContatoSchema, MensagemContatoIn
from django.shortcuts import get_object_or_404

router = Router(tags=["Mensagem de Contato"])

@router.get("/", response=List[MensagemContatoSchema])
def list_contatos(request):
    return MensagemContato.objects.all()

@router.get("/{id}", response=MensagemContatoSchema)
def get_contato(request, id: int):
    return get_object_or_404(MensagemContato, id=id)

@router.post("/", response=MensagemContatoSchema)
def create_contato(request, data: MensagemContatoIn):
    return MensagemContato.objects.create(**data.dict())

@router.put("/{id}", response=MensagemContatoSchema)
def update_contato(request, id: int, data: MensagemContatoIn):
    contato = get_object_or_404(MensagemContato, id=id)
    for attr, value in data.dict().items():
        setattr(contato, attr, value)
    contato.save()
    return contato

@router.delete("/{id}")
def delete_contato(request, id: int):
    contato = get_object_or_404(MensagemContato, id=id)
    contato.delete()
    return {"success": True}
