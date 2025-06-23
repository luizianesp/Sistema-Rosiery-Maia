# Sistema Rosiery Maia

Este é um sistema web desenvolvido com Django como parte do trabalho final da disciplina **Desenvolvimento para Web**. O projeto visa apresentar o portfólio profissional da professora Rosiery Maia, com foco em acessibilidade, clareza e boa experiência do usuário.

##  Funcionalidades principais

- Interface clara e moderna com Bootstrap 4
- CRUD de projetos (administrador)
- Página pública com apresentação e exibição de projetos
- Integração com Django Ninja para API REST

---

##  Como rodar o projeto localmente

### 1. Clone o repositório

```bash
git clone https://github.com/luizianesp/Sistema-Rosiery-Maia.git
cd Sistema-Rosiery-Maia
git checkout entrega3
```

### 2. Crie e ative um ambiente virtual

**Windows:**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Configure o banco de dados

O projeto utiliza o banco de dados padrão do Django (SQLite) por padrão. Não é necessário configurar variáveis de ambiente para isso.

### 5. Aplique as migrações

Ao aplicar as migrações algumas tabelas serão preenchidas através de um script do arquivo signals.py

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Crie um superusuário (opcional, para acessar o admin)

```bash
python manage.py createsuperuser
```

### 7. Rode o servidor de desenvolvimento

```bash
python manage.py runserver
```

Acesse o sistema em [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🧪 Testes

Você pode rodar os testes com:

```bash
python manage.py test
```

---

##  Estrutura do Projeto

```
├── core/
│   ├── api/
│   │   ├── __init__.py
│   │   ├── schemas.py             # Definição dos schemas de entrada/saída da API (Pydantic/Ninja)
│   │   ├── views_area.py          # Endpoints da API para Áreas de Pesquisa
│   │   ├── views_contato.py       # Endpoints da API para Mensagens de Contato
│   │   ├── views_orientacao.py    # Endpoints da API para Orientações
│   │   ├── views_projeto.py       # Endpoints da API para Projetos
│   │   └── views_publicacao.py    # Endpoints da API para Publicações
│   ├── migrations/
│   ├── templates/
│   │   └── core/
│   │       ├── base_admin.html    # Template base do painel administrativo
│   │       ├── gerenciar_orientacoes.html # Template para gerenciamento de Orientações
│   │       ├── gerenciar_publicacoes.html # Template para gerenciamento de Publicações
│   │       ├── mensagens_contato.html # Template para visualização de Mensagens de Contato
│   │       └── ... outros templates de frontend/admin
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py                   # Formulários Django (ex: ContatoForm)
│   ├── models.py                  # Definição dos modelos de banco de dados
│   ├── urls.py                    # URLs das views tradicionais do Django (frontend)
│   └── views.py                   # Views tradicionais do Django (frontend e dashboard admin)
|   |__signals.py                  # rotina d epopular o banco de dados
├── backend/             # Diretório raiz do seu projeto Django
│   ├── __init__.py
│   ├── settings.py                # Configurações do projeto
│   ├── urls.py                    # URLs PRINCIPAIS do projeto (incluindo API Ninja)
│   └── wsgi.py
├── manage.py
└── README.md   
```

---

##  Notas

- O projeto não requer arquivo `.env`.
- A API está implementada com Django Ninja e pode ser acessada via `/api/docs`.
- Certifique-se de estar na branch `backend3`.

---

##  Licença

Este projeto é de uso acadêmico e segue a licença [MIT](LICENSE).

---

##  Desenvolvido por

Boris Oliveira e colaboradores da disciplina *Desenvolvimento para Web*.