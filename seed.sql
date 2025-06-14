INSERT INTO AreaPesquisa (nome) VALUES
('Tecnologia Assistiva'),
('Educação Inclusiva');

INSERT INTO Projeto (titulo, descricao, imagem, categoria) VALUES
('Projeto Braille Digital', 'Criação de materiais em Braille digitalizados.', 'projetos/braille.jpg', 'Extensao'),
('Laboratório Acessível', 'Adaptação de laboratórios para alunos com deficiência.', 'projetos/lab.jpg', 'Pesquisa');

INSERT INTO Publicacao (titulo, link) VALUES
('Inclusão nas Escolas', 'https://exemplo.com/inclusao-escolas'),
('Acessibilidade Digital', 'https://exemplo.com/acessibilidade-digital');

INSERT INTO Orientacao (aluno, trabalho) VALUES
('João Silva', 'TCC sobre Libras e Tecnologia'),
('Maria Oliveira', 'Estudo sobre Ensino Inclusivo');

INSERT INTO MensagemContato (nome, email, assunto, mensagem) VALUES
('Fulano', 'fulano@email.com', 'Dúvida', 'Gostaria de saber mais sobre os projetos.');