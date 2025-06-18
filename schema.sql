-- schema.sql (ATUALIZADO)

-- Tabela para Topicos
CREATE TABLE Topicos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL
);

-- Tabela para Objetivos
CREATE TABLE Objetivos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL
);

-- Tabela para AreaPesquisa
CREATE TABLE AreaPesquisa (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT -- BLANK/NULL=TRUE no Django vira TEXT no SQLite
);

-- Tabela intermediária para AreaPesquisa.topico (ManyToManyField)
-- Nome padrão do Django: <app_label>_<model_name>_<field_name>
-- Assumindo 'core' como app_label
CREATE TABLE AreaPesquisa_topico (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    areapesquisa_id INTEGER NOT NULL,
    topicos_id INTEGER NOT NULL,
    FOREIGN KEY (areapesquisa_id) REFERENCES AreaPesquisa(id) ON DELETE CASCADE,
    FOREIGN KEY (topicos_id) REFERENCES Topicos(id) ON DELETE CASCADE,
    UNIQUE (areapesquisa_id, topicos_id) -- Garante que a combinação é única
);


-- Tabela para Projeto
CREATE TABLE Projeto (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo VARCHAR(200) NOT NULL,
    descricao TEXT NOT NULL,
    imagem VARCHAR(100), -- ImageField vira VARCHAR no SQLite para a URL/caminho, blank=True, null=True permite NULL
    categoria VARCHAR(20) NOT NULL, -- CATEGORIA_CHOICES no Django
    financiamento VARCHAR(100), -- blank=True, null=True permite NULL
    equipe TEXT -- blank=True, null=True permite NULL, Textfield vira TEXT
);

-- Tabela intermediária para Projeto.objetivos (ManyToManyField)
-- Nome padrão do Django: <app_label>_<model_name>_<field_name>
-- Assumindo 'core' como app_label
CREATE TABLE Projeto_objetivos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    projeto_id INTEGER NOT NULL,
    objetivos_id INTEGER NOT NULL,
    FOREIGN KEY (projeto_id) REFERENCES Projeto(id) ON DELETE CASCADE,
    FOREIGN KEY (objetivos_id) REFERENCES Objetivos(id) ON DELETE CASCADE,
    UNIQUE (projeto_id, objetivos_id)
);

-- Tabela para Publicacao
CREATE TABLE Publicacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    categoria VARCHAR(20) NOT NULL, -- CATEGORIA_CHOICES no Django
    titulo VARCHAR(200) NOT NULL,
    autores VARCHAR(100) NOT NULL,
    ano INTEGER NOT NULL,
    publicado_no VARCHAR(100) NOT NULL,
    descricao TEXT, -- blank=True, null=True permite NULL
    arquivo VARCHAR(100), -- FileField vira VARCHAR no SQLite para a URL/caminho, blank=True, null=True permite NULL
    link VARCHAR(200) NOT NULL -- URLField vira VARCHAR
);

-- Tabela para Orientacao
CREATE TABLE Orientacao (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    status VARCHAR(20) NOT NULL, -- STATUS_CHOICES no Django
    aluno VARCHAR(100) NOT NULL,
    categoria VARCHAR(20) NOT NULL, -- CATEGORIA_CHOICES no Django
    trabalho VARCHAR(200) NOT NULL,
    descricao TEXT, -- blank=True, null=True permite NULL
    imagem VARCHAR(100) -- ImageField vira VARCHAR no SQLite, blank=True, null=True permite NULL
);

-- Tabela para MensagemContato
CREATE TABLE MensagemContato (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(254) NOT NULL, -- EmailField vira VARCHAR
    assunto VARCHAR(100) NOT NULL,
    mensagem TEXT NOT NULL,
    noticias BOOLEAN NOT NULL -- BooleanField vira BOOLEAN no SQLite
    -- enviada_em (DateTimeField com auto_now_add=True) é gerenciado pelo Django no models.py,
    -- mas se quiser adicionar explicitamente no SQL, seria: enviada_em DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP
);