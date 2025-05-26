from ninja import NinjaAPI
from core.api.views_area import router as area_router
from core.api.views_projeto import router as projeto_router
from core.api.views_publicacao import router as publicacao_router
from core.api.views_orientacao import router as orientacao_router
from core.api.views_contato import router as contato_router

api = NinjaAPI(title="Core API")

api.add_router("/areas", area_router)
api.add_router("/projetos", projeto_router)
api.add_router("/publicacoes", publicacao_router)
api.add_router("/orientacoes", orientacao_router)
api.add_router("/contatos", contato_router)

