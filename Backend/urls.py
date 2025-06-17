"""
URL configuration for Backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from core.api_urls import api

# Importar settings e static para servir arquivos em desenvolvimento
from django.conf import settings
from django.conf.urls.static import static

from core.views import user_logout, user_login, admin_panel_content, admin_dashboard

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),  # 🔥 API Django Ninja
    path('', include('core.urls')),  # 🔗 Rotas tradicionais

# URLs de autenticação
    path('login/', user_login, name='login'), # URL para a sua página de login
    path('logout/', user_logout, name='logout'), # URL para o logout

    # === URLs do Painel Administrativo ===
    path('dashboard/', admin_dashboard, name='dashboard'),  # URL do Dashboard

    # URLs para carregar conteúdo dinâmico no painel administrativo
    # Estes mapearão para as partes de template que criaremos
    path('admin/conteudo/<str:template_name>/', admin_panel_content, name='admin_content'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)