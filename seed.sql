-- seed.sql (ATUALIZADO)

-- Inserir dados em Topicos (seus "tópicos" para AreaPesquisa)
INSERT INTO Topicos (nome) VALUES
('Acessibilidade Digital'),
('Ensino de Libras'),
('Desenvolvimento de Hardware'),
('Inclusão Social');

-- Inserir dados em Objetivos (seus "objetivos" para Projeto)
INSERT INTO Objetivos (nome) VALUES
('Reduzir Barreiras'),
('Promover Equidade'),
('Inovar em Tecnologia'),
('Capacitar Educadores');

-- Inserir dados em AreaPesquisa (agora com um campo de descrição)
INSERT INTO AreaPesquisa (nome, descricao) VALUES
('Tecnologia Assistiva', 'Foco no desenvolvimento e aplicação de tecnologias para pessoas com deficiência.'),
('Educação Inclusiva', 'Pesquisa e prática para tornar a educação acessível a todos os alunos.');

-- Relacionar Áreas de Pesquisa com Tópicos (tabela AreaPesquisa_topico)
-- Exemplo: 'Tecnologia Assistiva' (id=1) com 'Acessibilidade Digital' (id=1) e 'Desenvolvimento de Hardware' (id=3)
INSERT INTO AreaPesquisa_topico (areapesquisa_id, topicos_id) VALUES
(1, 1),
(1, 3);
-- Exemplo: 'Educação Inclusiva' (id=2) com 'Ensino de Libras' (id=2) e 'Inclusão Social' (id=4)
INSERT INTO AreaPesquisa_topico (areapesquisa_id, topicos_id) VALUES
(2, 2),
(2, 4);


-- Inserir dados em Projeto (com imagem, categoria, financiamento e equipe)
INSERT INTO Projeto (titulo, descricao, imagem, categoria, financiamento, equipe) VALUES
('Projeto Braille Digital', 'Criação de materiais em Braille digitalizados e interativos.', 'projetos/braille_digital.jpg', 'Extensão', 'FNDE', 'Equipe de Desenvolvimento'),
('Laboratório Acessível', 'Adaptação de laboratórios universitários para alunos com deficiência visual e motora, utilizando tecnologias assistivas.', 'projetos/lab_acessivel.jpg', 'Pesquisa', 'CNPq', 'Grupo de Pesquisa em Acessibilidade');

-- Relacionar Projetos com Objetivos (tabela Projeto_objetivos)
-- Exemplo: 'Projeto Braille Digital' (id=1) com 'Inovar em Tecnologia' (id=3) e 'Reduzir Barreiras' (id=1)
INSERT INTO Projeto_objetivos (projeto_id, objetivos_id) VALUES
(1, 3),
(1, 1);
-- Exemplo: 'Laboratório Acessível' (id=2) com 'Promover Equidade' (id=2) e 'Reduzir Barreiras' (id=1)
INSERT INTO Projeto_objetivos (projeto_id, objetivos_id) VALUES
(2, 2),
(2, 1);


-- Inserir dados em Publicacao (com categoria, autores, ano, publicado_no, descricao e arquivo)
INSERT INTO Publicacao (categoria, titulo, autores, ano, publicado_no, descricao, arquivo, link) VALUES
('Artigo', 'Inclusão nas Escolas: Desafios e Soluções', 'Maia R., Silva J.', 2023, 'Revista Brasileira de Educação', 'Artigo focado nas principais barreiras e estratégias para a inclusão educacional.', 'publicacao/inclusao_escolas.pdf', 'https://exemplo.com/inclusao-escolas-artigo'),
('Conferencia', 'Acessibilidade Digital em Plataformas E-learning', 'Oliveira M., Santos A., Maia R.', 2024, 'Anais do Congresso Nacional de Tecnologia', 'Trabalho apresentado em conferência sobre a importância da acessibilidade em ambientes virtuais de aprendizagem.', 'publicacao/acessibilidade_ead.pdf', 'https://exemplo.com/acessibilidade-digital-conf');

-- Inserir dados em Orientacao (com status, categoria e imagem)
INSERT INTO Orientacao (status, aluno, categoria, trabalho, descricao, imagem) VALUES
('em Andamento', 'João Silva', 'Doutorado', 'Desenvolvimento de uma Interface Háptica para Ensino de Matemática', 'Pesquisa de doutorado focada em criar ferramentas táteis para auxiliar o ensino de conceitos matemáticos a alunos com deficiência visual.', 'orientacao/joao_silva.jpg'),
('Concluido', 'Maria Oliveira', 'Mestrado', 'Estudo Comparativo de Metodologias de Ensino Inclusivo no Ensino Fundamental', 'Dissertação de mestrado que analisa a eficácia de diferentes abordagens pedagógicas inclusivas em escolas públicas.', 'orientacao/maria_oliveira.jpg');

-- Inserir dados em MensagemContato (com notícias)
INSERT INTO MensagemContato (nome, email, assunto, mensagem, noticias) VALUES
('Fulano de Tal', 'fulano@email.com', 'Dúvida sobre Projetos', 'Gostaria de saber mais detalhes sobre o "Projeto Braille Digital" e como posso contribuir.', TRUE),
('Ciclana Souza', 'ciclana@outlook.com', 'Sugestão de Parceria', 'Minha instituição tem interesse em colaborar com seus estudos sobre Tecnologia Assistiva.', FALSE);