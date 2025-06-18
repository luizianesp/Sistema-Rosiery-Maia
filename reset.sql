-- reset.sql (ATUALIZADO)

-- Derrubar tabelas intermediárias primeiro devido a chaves estrangeiras
DROP TABLE IF EXISTS AreaPesquisa_topico;
DROP TABLE IF EXISTS Projeto_objetivos;

-- Em seguida, derrubar as tabelas principais
DROP TABLE IF EXISTS MensagemContato;
DROP TABLE IF EXISTS Orientacao;
DROP TABLE IF EXISTS Publicacao;
DROP TABLE IF EXISTS Projeto;
DROP TABLE IF EXISTS AreaPesquisa;
DROP TABLE IF EXISTS Topicos;
DROP TABLE IF EXISTS Objetivos;


-- Recriar o esquema do banco de dados
.read schema.sql

-- Popular o banco de dados com dados iniciais
.read seed.sql