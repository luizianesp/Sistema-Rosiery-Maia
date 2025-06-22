from django.db.models.signals import post_migrate
from django.dispatch import receiver
# Removido ContentFile, base64
import random
from datetime import datetime, timedelta

# Importe todos os seus modelos do app 'core'
from .models import (
    Topicos, Objetivos, AreaPesquisa, Projeto,
    Publicacao, Orientacao, MensagemContato
)

@receiver(post_migrate)
def populate_initial_data(sender, **kwargs):
    """
    Popula o banco de dados com dados de exemplo após a migração do app 'core',
    atribuindo caminhos de arquivo para imagens e PDFs.
    """
    # Verifica se o sinal é para o app 'core' para evitar execução em outros apps
    if sender.name == 'core':
        print("\nIniciando a população de dados de exemplo para o app 'core'...")

        # Verifica se já existem dados para evitar duplicação em execuções repetidas
        if Topicos.objects.exists() or AreaPesquisa.objects.exists() or Projeto.objects.exists():
            print("Dados iniciais já existem. Pulando a população.")
            return

        # Removidas as funções get_dummy_png_file e get_dummy_pdf_file

        # 1. Popula Topicos
        topicos_data = ["Inteligência Artificial", "Aprendizado de Máquina", "Visão Computacional", "Processamento de Linguagem Natural", "Segurança da Informação"]
        topicos_objects = []
        for nome in topicos_data:
            topicos_objects.append(Topicos.objects.create(nome=nome))
        print(f"-> Criados {len(topicos_objects)} Tópicos.")

        # 2. Popula Objetivos
        objetivos_data = ["Desenvolvimento de Plataformas", "Análise de Big Data", "Pesquisa e Inovação", "Ensino e Treinamento", "Extensão Comunitária"]
        objetivos_objects = []
        for nome in objetivos_data:
            objetivos_objects.append(Objetivos.objects.create(nome=nome))
        print(f"-> Criados {len(objetivos_objects)} Objetivos.")

        # 3. Popula AreaPesquisa
        areas_data = [
            {"nome": "Sistemas Autônomos", "descricao": "Foco em sistemas de IA e robótica.", "topicos": [topicos_objects[0], topicos_objects[2]]}, # IA, Visão Computacional
            {"nome": "Ciência de Dados Aplicada", "descricao": "Aplicação de técnicas de análise em diversos domínios.", "topicos": [topicos_objects[1], topicos_objects[3]]}, # Aprendizado de Máquina, PLN
            {"nome": "Cibersegurança e Privacidade", "descricao": "Estudos sobre proteção de dados e sistemas de informação.", "topicos": [topicos_objects[4]]}, # Segurança da Informação
        ]
        areas_objects = []
        for data in areas_data:
            area = AreaPesquisa.objects.create(nome=data["nome"], descricao=data["descricao"])
            area.topico.set(data["topicos"]) # Associa os tópicos
            areas_objects.append(area)
        print(f"-> Criadas {len(areas_objects)} Áreas de Pesquisa.")

        # 4. Popula Projeto
        projetos_data = [
            {"titulo": "Sistema de Recomendação Inteligente", "descricao": "Projeto de pesquisa para desenvolver um motor de recomendação personalizado.", "categoria": "Pesquisa", "financiamento": "CNPq", "equipe": "Equipe A, Profa. Rosiery", "objetivos_relacionados": [objetivos_objects[0], objetivos_objects[2]], "imagem_path": "projetos/projeto_ia_rec.png"},
            {"titulo": "Curso Online de Python para Iniciantes", "descricao": "Projeto de ensino visando capacitar novos desenvolvedores em Python.", "categoria": "Ensino", "financiamento": "FAPERN", "equipe": "Equipe B, Monitores", "objetivos_relacionados": [objetivos_objects[3]], "imagem_path": "projetos/projeto_python_curso.png"},
            {"titulo": "Monitoramento Ambiental com Drones", "descricao": "Projeto de extensão para uso de drones na coleta de dados ambientais.", "categoria": "Extensão", "financiamento": "Parceria Pública", "equipe": "Equipe C, Voluntários", "objetivos_relacionados": [objetivos_objects[4]], "imagem_path": "projetos/projeto_drones_ambiental.png"},
        ]
        projetos_objects = []
        for data in projetos_data:
            projeto = Projeto.objects.create(
                titulo=data["titulo"],
                descricao=data["descricao"],
                categoria=data["categoria"],
                financiamento=data["financiamento"],
                equipe=data["equipe"],
                imagem=data["imagem_path"] # Atribui o caminho da imagem diretamente
            )
            projeto.objetivos.set(data["objetivos_relacionados"]) # Associa os objetivos
            projetos_objects.append(projeto)
        print(f"-> Criados {len(projetos_objects)} Projetos.")

        # 5. Popula Publicacao
        publicacoes_data = [
            {"categoria": "Artigo", "titulo": "Metodologias Ágeis em Ambientes de Pesquisa", "autores": "Maia R, Souza C", "ano": 2024, "publicado_no": "Revista Brasileira de Computação", "descricao": "Artigo sobre a aplicação de metodologias ágeis em projetos de pesquisa.", "link": "http://example.com/agile_research", "arquivo_path": "publicacao/artigo_agil.pdf"},
            {"categoria": "Livro", "titulo": "Fundamentos de Data Science", "autores": "Silva A", "ano": 2023, "publicado_no": "Editora Acadêmica", "descricao": "Livro texto para cursos de graduação em Data Science.", "link": "http://example.com/data_science_book", "arquivo_path": "publicacao/livro_datascience.pdf"},
            {"categoria": "Conferencia", "titulo": "Desafios da Cibersegurança na Indústria 4.0", "autores": "Pereira D", "ano": 2022, "publicado_no": "Anais da Conferência de Segurança", "descricao": "Apresentação sobre os riscos e soluções em segurança para a indústria.", "link": "http://example.com/industry4_security", "arquivo_path": "publicacao/conferencia_ciberseguranca.pdf"},
        ]
        publicacoes_objects = []
        for data in publicacoes_data:
            publicacao = Publicacao.objects.create(
                categoria=data["categoria"],
                titulo=data["titulo"],
                autores=data["autores"],
                ano=data["ano"],
                publicado_no=data["publicado_no"],
                descricao=data["descricao"],
                link=data["link"],
                arquivo=data["arquivo_path"] # Atribui o caminho do arquivo diretamente
            )
            publicacoes_objects.append(publicacao)
        print(f"-> Criadas {len(publicacoes_objects)} Publicações.")

        # 6. Popula Orientacao
        orientacoes_data = [
            {"status": "em Andamento", "aluno": "Mariana Santos", "categoria": "Mestrado", "trabalho": "Aprendizado Profundo para Classificação de Imagens Médicas", "descricao": "Tese de mestrado com foco em diagnóstico assistido por computador.", "imagem_path": "orientacao/orientacao_mariana.png"},
            {"status": "Concluido", "aluno": "Lucas Almeida", "categoria": "Doutorado", "trabalho": "Otimização de Redes Neurais para Edge Computing", "descricao": "Tese de doutorado sobre IA em dispositivos com recursos limitados.", "imagem_path": "orientacao/orientacao_lucas.png"},
            {"status": "em Andamento", "aluno": "Isabela Rocha", "categoria": "TCC", "trabalho": "Desenvolvimento de um Sistema Web para Gestão de Projetos", "descricao": "TCC focado em desenvolvimento full-stack.", "imagem_path": "orientacao/orientacao_isabela.png"},
        ]
        orientacoes_objects = []
        for data in orientacoes_data:
            orientacao = Orientacao.objects.create(
                status=data["status"],
                aluno=data["aluno"],
                categoria=data["categoria"],
                trabalho=data["trabalho"],
                descricao=data["descricao"],
                imagem=data["imagem_path"] # Atribui o caminho da imagem diretamente
            )
            orientacoes_objects.append(orientacao)
        print(f"-> Criadas {len(orientacoes_objects)} Orientações.")

        # 7. Popula MensagemContato
        mensagens_data = [
            {"nome": "Visitante Curioso", "email": "curioso@exemplo.com", "assunto": "Dúvida sobre Área de Pesquisa", "mensagem": "Gostaria de saber mais sobre a área de sistemas autônomos.", "noticias": False},
            {"nome": "Parceiro Potencial", "email": "parceiro@empresa.com", "assunto": "Proposta de Colaboração em Projeto", "mensagem": "Temos uma oportunidade de parceria no projeto de IA.", "noticias": True},
            {"nome": "Ex-Aluno", "email": "exaluno@email.com", "assunto": "Agradecimento e Contato", "mensagem": "Só para agradecer a orientação e manter contato.", "noticias": True},
        ]
        for data in mensagens_data:
            # Adiciona variação na data de envio para parecer mais real
            sent_time = datetime.now() - timedelta(days=random.randint(1, 60), hours=random.randint(1, 23))
            MensagemContato.objects.create(
                nome=data["nome"],
                email=data["email"],
                assunto=data["assunto"],
                mensagem=data["mensagem"],
                noticias=data["noticias"],
                enviada_em=sent_time # Define a data e hora de envio
            )
        print(f"-> Criadas {len(mensagens_data)} Mensagens de Contato.")

        print("População de dados de exemplo para o app 'core' concluída com sucesso.")

