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
git clone -b entrega2 https://github.com/luizianesp/Sistema-Rosiery-Maia.git
cd Sistema-Rosiery-Maia
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

```bash
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
Backend/
├── core/                 # Aplicações Django
├── static/              # Arquivos estáticos (CSS, JS, Imagens)
├── templates/           # Templates HTML
├── manage.py            # Comando principal do Django
├── requirements.txt     # Dependências do projeto
└── ...
```

---

##  Notas

- O projeto não requer arquivo `.env`.
- A API está implementada com Django Ninja e pode ser acessada via `/api/`.
- Certifique-se de estar na branch `backend2`.

---

##  Licença

Este projeto é de uso acadêmico e segue a licença [MIT](LICENSE).

---

## 🙋‍♀️ Desenvolvido por

Prof. Rosiery Maia e colaboradores da disciplina *Desenvolvimento para Web*.