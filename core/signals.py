from django.db.models.signals import post_migrate
from django.dispatch import receiver
import random
from datetime import datetime, timedelta
from django.utils import timezone

# Importe todos os seus modelos do app 'core'
from .models import (
    Topicos, Objetivos, AreaPesquisa, Projeto,
    Publicacao, Orientacao, MensagemContato
)


@receiver(post_migrate)
def populate_initial_data(sender, **kwargs):
    """
    Popula o banco de dados com dados de exemplo após a migração do app 'core',
    atribuindo caminhos de arquivo para imagens e PDFs com os nomes fornecidos.
    """
    # Verifica se o sinal é para o app 'core' para evitar execução em outros apps
    if sender.name == 'core':
        print("\nIniciando a população de dados de exemplo para o app 'core'...")

        # Verifica se já existem dados para evitar duplicação em execuções repetidas
        if Topicos.objects.exists() or AreaPesquisa.objects.exists() or Projeto.objects.exists():
            print("Dados iniciais já existem. Pulando a população.")
            return

        # --- Dados extraídos do database.py (adaptados para os modelos Django) ---

        # Para Topicos (não existe diretamente no database.py, mas é ManyToMany)
        # Usaremos uma lista de tópicos genéricos que podem ser associados
        topicos_list_initial = [
            "Inteligência Artificial", "Aprendizado de Máquina", "Visão Computacional",
            "Processamento de Linguagem Natural", "Robótica", "Sistemas Embarcados",
            "Banco de Dados", "Engenharia de Software", "Cibersegurança", "Redes Neurais"
        ]
        topicos_objects = {}  # Usaremos um dicionário para fácil acesso por nome
        for nome in topicos_list_initial:
            topico_obj = Topicos.objects.create(nome=nome)
            topicos_objects[nome] = topico_obj
        print(f"-> Criados {len(topicos_objects)} Tópicos base.")

        # Para Objetivos (não existe diretamente no database.py, mas é ManyToMany)
        objetivos_list_initial = [
            "Análise e Otimização", "Desenvolvimento de Soluções", "Pesquisa Fundamental",
            "Educação e Capacitação", "Impacto Social e Extensão"
        ]
        objetivos_objects = {}  # Usaremos um dicionário para fácil acesso por nome
        for nome in objetivos_list_initial:
            objetivo_obj = Objetivos.objects.create(nome=nome)
            objetivos_objects[nome] = objetivo_obj
        print(f"-> Criados {len(objetivos_objects)} Objetivos base.")

        # Dados de Áreas de Pesquisa (adaptados)
        # Associar tópicos manualmente, pois database.py não tem essa relação direta
        areas_pesquisa_data = [
            {"nome": "Engenharia Elétrica / Aprendizagem Robótica",
             "descricao": "Foco em sistemas de engenharia elétrica e robótica com componentes de aprendizado.",
             "topicos_nomes": ["Robótica", "Aprendizado de Máquina"]},
            {"nome": "Ciência da Computação / Inteligência Artificial",
             "descricao": "Estudo e desenvolvimento de sistemas inteligentes e algoritmos de computação.",
             "topicos_nomes": ["Inteligência Artificial", "Redes Neurais", "Visão Computacional"]},
        ]

        # Dados de Projetos (adaptados)
        # ATUALIZADO: Caminhos das imagens de acordo com os arquivos carregados (.png)
        projetos_data = [
            # Projetos de Pesquisa
            {
                "titulo": """Análise de aplicação do Modelo de Inteligência IDeM-MRS na Logística""",
                "categoria": "Pesquisa",
                "descricao": """Edital n.23/2022-CIPI/PROPEG/UERN. Projeto dedicado a analisar como o IDEM-MRS pode atuar em situações complexas e identificar possibilidades de otimização nas operações de assimilação e acomodação do conhecimento.""",
                "imagem": "projetos/idem_mrs_logistica.jpg",  # De .jpg para .png
                "financiamento": """UERN (via Edital CIPI/PROPEG)""",
                "equipe": """Rosiery da Silva Maia - Coordenador / Renato José de Sobral Cintra - Integrante.""",
                "objetivos_nomes": ["Análise e Otimização", "Pesquisa Fundamental"]
            },
            {
                "titulo": """Soluções em automação e inteligência computacional para a entrada de mercadoria do setor supermercadista""",
                "categoria": "Pesquisa",
                "descricao": """Edital n.001/2017-CIPI/PROPEG/UERN. Projeto dedicado a identificar soluções em automação e inteligência computacional, contribuindo para uma real vantagem competitiva para o negócio supermercadista.""",
                "imagem": "projetos/automacao_supermercado.png",
                "financiamento": """UERN (via Edital CIPI/PROPEG)""",
                "equipe": """Rosiery da Silva Maia - Coordenador / Adriana Takahashi - Integrante / Isaac de Lima Oliveira Filho - Integrante / Bruno Agenor Soares Santana - Integrante / Felipe Mariano de Barros - Integrante. Graduação: (2)""",
                "objetivos_nomes": ["Desenvolvimento de Soluções", "Análise e Otimização"]
            },
            {
                "titulo": """Planejamento de caminho de robôs utilizando mapas em grades de ocupação 2.5D""",
                "categoria": "Pesquisa",
                "descricao": """Edital PIBIC n.003/2015-PROPEG/UERN. Projeto dedicado a desenvolver uma heurística para planejamento de caminho de robôs, partindo de uma representação do ambiente através de mapas em grades de ocupação 2.5D, com informações discretas e tridimensionais.""",
                "imagem": "projetos/planejamento_rota_25d.png",  # De .jpg para .png
                "financiamento": """Programa Institucional de Bolsas de Iniciação Científica - Bolsa.""",
                "equipe": """Rosiery da Silva Maia - Coordenador / Anderson Abner S. Souza - Integrante / Bruno Agenor Soares Santana - Integrante / MARIA GRACIELLY FERNANDES COUTINHO - Integrante. Graduação: (2)""",
                "objetivos_nomes": ["Pesquisa Fundamental", "Desenvolvimento de Soluções"]
            },
            # Projetos de Ensino
            {
                "titulo": """Grupo de Estudos Tutoriais em Aprendizagem Robótica""",
                "categoria": "Ensino",
                "descricao": """Edital n.066/2024-PROEG/UERN. Projeto para estabelecer um Grupo de Estudos Tutoriais em Aprendizagem Robótica, vinculado ao Laboratório de Aprendizagem Robótica (LAR) do Campus de Natal da UERN, para oferecer momentos ricos de aprendizado a alunos com interesses em atividades extraclasses.""",
                "imagem": "projetos/grupo_estudos_robotica.png",
                "financiamento": """UERN (via Edital PROEG)""",
                "equipe": """Rosiery da Silva Maia - Coordenador / Anderson Abner S. Souza - Integrante / Wilfredo Blanco Figuerola - Integrante / Mateus Vinícius Rocha da Costa - Integrante / Yuri Dantas da Silva - Integrante. Graduação: (2)""",
                "objetivos_nomes": ["Educação e Capacitação"]
            },
            {
                "titulo": """Produção de material didático para o ensino de Compiladores na UERN: metodologias Notas de Aulas""",
                "categoria": "Ensino",
                "descricao": """Edital n.007/2022-PROEG/UERN. Projeto para continuar os anteriores, tomando como base o trabalho de criação e desenvolvimento de materiais didáticos nas universidades.""",
                "imagem": "projetos/material_didatico_compiladores.png",
                "financiamento": """UERN (via Edital PROEG)""",
                "equipe": """Rosiery da Silva Maia - Coordenador / Anderson Abner S. Souza - Integrante / Bartira Paraguaçu Falcão Dantas da Rocha - Integrante.""",
                "objetivos_nomes": ["Educação e Capacitação"]
            },
            {
                "titulo": """Encarando o ENADE: Parte II""",
                "categoria": "Ensino",
                "descricao": """Edital n.016/2021-PROEG/UERN. Projeto para trabalhar tarefas visando a melhoria do índice ENADE do curs de Ciência da Computação do Campus de Natal da Universidade do Estado do Rio Grande do Norte.""",
                "imagem": "projetos/enade_uern.png",
                "financiamento": """UERN (via Edital PROEG)""",
                "equipe": """Rosiery da Silva Maia - Integrante / Anderson Abner S. Souza - Coordenador. Graduação: (15)""",
                "objetivos_nomes": ["Educação e Capacitação", "Análise e Otimização"]
            },
            # Projetos de Extensão
            {
                "titulo": """Robótica como potencial terapêutico para idosos""",
                "categoria": "Extensão",
                "descricao": """Edital PIBEX n.008/2024-PROEX/UERN. Projeto para investigar o impacto do uso do robô Roboldo como ferramenta terapêutica para idosos que enfrentam problemas de degeneração cognitiva e demência.""",
                "imagem": "projetos/robotica_terapeutica.png",
                "financiamento": """UERN (via Edital PROEX)""",
                "equipe": """Rosiery da Silva Maia - Coordenador / Anderson Abner S. Souza - Integrante / Raul Benites Paradeda - Integrante / Yuri Dantas da Silva - Integrante / Lara Maia Pereira - Integrante.""",
                "objetivos_nomes": ["Impacto Social e Extensão", "Desenvolvimento de Soluções"]
            },
            {
                "titulo": """Curso de capacitação em Informática para colaboradores de uma rede de supermercados da grande Natal""",
                "categoria": "Extensão",
                "descricao": """Edital 001/2018-PROEX/UERN. Projeto dedicado a oferecer cursos de capacitação em Informática para colaboradores de uma rede de supermercados da grande Natal, de forma itinerante.""",
                "imagem": "projetos/capacitacao_informatica.png",
                "financiamento": """UERN (via Edital PROEX)""",
                "equipe": """Rosiery da Silva Maia - Integrante / Isaac Lima de Oliveira Filho - Coordenador.""",
                "objetivos_nomes": ["Impacto Social e Extensão", "Educação e Capacitação"]
            },
            {
                "titulo": """Inclusão Tecnológica: Robótica""",
                "categoria": "Extensão",
                "descricao": """Projeto para despertar e estimular o interesse de alunos dos cursos de Ciência da Computação, Engenharia de Computação, Engenharia Elétrica, Engenharia Mecatrônica ou cursos afins das Instituições de ensino superior do Estado do Rio Grande do Norte, na área da Robótica. Trabalho em parceria com a UERN e a UFRN.""",
                "imagem": "projetos/inclusao_robotica.png",  # De .jpg para .png
                "financiamento": None,
                "equipe": """Rosiery da Silva Maia - Integrante / Anderson Abner S. Souza - Coordenador / Alex Aquino dos Santos - Integrante / Lucas Vieira Chacon - Integrante. Graduação: (15)""",
                "objetivos_nomes": ["Impacto Social e Extensão", "Educação e Capacitação"]
            },
        ]

        # Dados de Publicações (adaptados)
        # Caminhos para 'publicacao/<nome>.pdf' (nomes fictícios para PDFs)
        publicacoes_data = [
            # Artigos
            {
                "titulo": """N-learning: An Approach for Learning and Teaching Skills in Multirobot Teams""",
                "categoria": "Artigo",
                "ano": 2019,
                "autores": """COSTA, LUÍS FELIPHE S.; NASCIMENTO, TIAGO P.; MAIA, ROSIERY DA S.; GONÇALVES, LUIZ MARCOS G.""",
                "publicado_no": """ROBOTICA, v. 1, p. 1-21, 2019.""",
                "descricao": """Abordagem para aprendizado e ensino de habilidades em equipes de múltiplos robôs. Citacoes: WEB OF SCIENCE = 4 | SCOPUS 4.""",
                "arquivo": "publicacao/n_learning_multirobot.pdf",
                "link": "http://example.com/n_learning_multirobot"
            },
            {
                "titulo": """A Cloud Robotics Architecture Clone Based for a Cellbots Team""",
                "categoria": "Artigo",
                "ano": 2017,
                "autores": """DA SILVA PEREIRA, DIEGO AGENOR SANTANA, BRUNO SILVA MAIA, ROSIERY; SOUZA, ANDERSON.""",
                "publicado_no": """IEEE Latin America Transactions, v. 15, p. 1587-1594, 2017.""",
                "descricao": """Apresenta uma arquitetura de robótica em nuvem baseada em clones para uma equipe de Cellbots. Citacoes: WEB OF SCIENCE 1 | SCOPUS 1.""",
                "arquivo": "publicacao/cloud_robotics_cellbots.pdf",
                "link": "http://example.com/cloud_robotics_cellbots"
            },
            {
                "titulo": """Intellectual Development Model for Multi-Robot Systems""",
                "categoria": "Artigo",
                "ano": 2015,
                "autores": """MAIA, R. S.; GONÇALVES, L. M. G.""",
                "publicado_no": """JOURNAL OF INTELLIGENT & ROBOTIC SYSTEMS, v. 1, p. 1-23, 2015.""",
                "descricao": """Modelo de Desenvolvimento Intelectual para Sistemas Multi-Robôs. Citacoes: WEB OF SCIENCE 5 | SCOPUS 6.""",
                "arquivo": "publicacao/intellectual_dev_multi_robot.pdf",
                "link": "http://example.com/intellectual_dev_multi_robot"
            },
            # Livros (Adaptado de Teses/Dissertações)
            {
                "titulo": """Modelo de Desenvolvimento Intelectual para Agentes Robóticos""",
                "categoria": "Livro",
                "ano": 2012,
                "autores": """MAIA, R. S.""",
                "publicado_no": """Tese de Doutorado""",
                "descricao": """Tese de Doutorado apresentada à Universidade Federal do Rio Grande do Norte para obtenção do título de Doutora em Engenharia Elétrica e de Computação.""",
                "arquivo": "publicacao/modelo_dev_intelectual_agentes.pdf",
                "link": "http://example.com/modelo_dev_intelectual_agentes"
            },
            {
                "titulo": """Um Sistema de apoio à decisão para o Gerenciamento Dinâmico das Sondas de Produção Terrestres na Bacia Potiguar""",
                "categoria": "Livro",
                "ano": 2004,
                "autores": """MAIA, R. S.""",
                "publicado_no": """Dissertação de Mestrado""",
                "descricao": """Dissertação de Mestrado apresentada à Universidade Federal do Rio Grande do Norte para obtenção do título de Mestre em Sistemas e Computação.""",
                "arquivo": "publicacao/sistema_apoio_decisao_sondas.pdf",
                "link": "http://example.com/sistema_apoio_decisao_sondas"
            },
            # Capítulos de Livros
            {
                "titulo": """3D Probabilistic Occupancy Grid to Robotic Mapping with Stereo Vision""",
                "categoria": "Capitulo",
                "ano": 2012,
                "autores": """S. Souza, Anderson A.; Maia, Rosiery; G. Gonalves, Luiz M.""",
                "publicado_no": """In: Current Advancements in Stereo Vision. 1ed.: InTech, 2012.""",
                "descricao": """Capítulo de livro que aborda o mapeamento robótico 3D com visão estéreo usando grade de ocupação probabilística.""",
                "arquivo": "publicacao/3d_prob_occupancy_grid.pdf",
                "link": "http://example.com/3d_prob_occupancy_grid"
            },
            # Conferências
            {
                "titulo": """Rules for Robotic Cooperation Based on Vygotsky and Piaget""",
                "categoria": "Conferencia",
                "ano": 2015,
                "autores": """Maia, Rosiery; SOUZA, ANDERSON ABNER; GONALVES, LUIZ MARCOS""",
                "publicado_no": """In: 2015 12th Latin American Robotics Symposium (LARS) and 2015 3rd Brazilian Symposium on Robotics (SBR), 2015, Uberlandia.""",
                "descricao": """Apresentação de regras para cooperação robótica baseadas nas teorias de Vygotsky e Piaget.""",
                "arquivo": "publicacao/rules_robotic_cooperation.pdf",
                "link": "http://example.com/rules_robotic_cooperation"
            },
            {
                "titulo": """Multi-robot Cooperation Based on Learning Social Models""",
                "categoria": "Conferencia",
                "ano": 2012,
                "autores": """Maia, Rosiery; GONCALVES, LUIZ MARCOS""",
                "publicado_no": """In: 2012 Brazilian Robotics Symposium and Latin American Robotics Symposium (SBR-LARS), 2012, Fortaleza.""",
                "descricao": """Cooperação multirrobô baseada na aprendizagem de modelos sociais.""",
                "arquivo": "publicacao/multi_robot_cooperation_social_models.pdf",
                "link": "http://example.com/multi_robot_cooperation_social_models"
            },
            {
                "titulo": """Concepção de um Formalismo de Aprendizagem baseado em Modelos Sociais para um Time de Robôs em execução cooperativa de tarefas""",
                "categoria": "Conferencia",
                "ano": 2011,
                "autores": """MAIA, R. S.; SOUZA, A. A. S. GONÇALVES, L. M. G.""",
                "publicado_no": """In: Simpósio Brasileiro de Automação Inteligente, 2011, São João del-Rei.""",
                "descricao": """Trabalho sobre um formalismo de aprendizagem para robôs cooperativos.""",
                "arquivo": "publicacao/formalism_learning_social_models.pdf",
                "link": "http://example.com/formalism_learning_social_models"
            },
        ]

        # Dados de Orientações (adaptados)
        # Caminhos alterados para 'orientacao/<nome>.png'
        orientacoes_data = [
            # Mestrado
            {
                "aluno": """Jurasildo Oliveira Reinaldo""",
                "categoria": "Mestrado",
                "trabalho": """Reconhecimento de Objetos no Desenvolvimento de um Sistema de Navegação Inteligente para Robôs Móveis""",
                "descricao": """Dissertação de Mestrado. Co-orientador: Rosiery da Silva Maia. Financiamento: Conselho Nacional de Desenvolvimento Científico e Tecnológico.""",
                "status": "Concluido",
                "imagem": "orientacao/jurasildo_reinaldo.png",
            },
            # TCC
            {
                "aluno": """Fernando Carlos Moura Vieira""",
                "categoria": "TCC",
                "trabalho": """FloydRouter: Planejador de Rota Mínima para Múltiplos Destinos""",
                "descricao": """Trabalho de Conclusão de Curso. Orientador Principal: Rosiery da Silva Maia.""",
                "status": "Concluido",
                "imagem": "orientacao/fernando_vieira.png",
            },
            {
                "aluno": """Bruno Agenor Soares Santana""",
                "categoria": "TCC",
                "trabalho": """Desenvolvimento de um Sistema de Controle e Planejamento de Rotas para Cellbots""",
                "descricao": """Trabalho de Conclusão de Curso. Orientador Principal: Rosiery da Silva Maia.""",
                "status": "Concluido",
                "imagem": "orientacao/bruno_santana.png",
            },
            {
                "aluno": """Jefferson Willian da Cruz Lucena""",
                "categoria": "TCC",
                "trabalho": """Desenvolvimento de Software para Gestão de Armazém""",
                "descricao": """Trabalho de Conclusão de Curso. Orientador Principal: Rosiery da Silva Maia.""",
                "status": "Concluido",
                "imagem": "orientacao/jefferson_lucena.png",
            },
            # Iniciação Científica
            {
                "aluno": """Bruno Agenor Soares Santana""",
                "categoria": "Iniciacao Cientifica",
                "trabalho": """Desenvolvimento de um Sistema de Navegação Autônoma para um time de Cellbots""",
                "descricao": """Projeto de Iniciação Científica. Orientador Principal: Rosiery da Silva Maia. Financiamento: Conselho Nacional de Desenvolvimento Científico e Tecnológico.""",
                "status": "Concluido",
                "imagem": "orientacao/bruno_santana_ic.png",
            },
            {
                "aluno": """Hemerson Rafael Pereira Pontes""",
                "categoria": "Iniciacao Cientifica",
                "trabalho": """Construção de uma Fechadura Eletrônica de baixo custo""",
                "descricao": """Projeto de Iniciação Científica. Orientador Principal: Rosiery da Silva Maia. Financiamento: Conselho Nacional de Desenvolvimento Científico e Tecnológico.""",
                "status": "Concluido",
                "imagem": "orientacao/hemerson_pontes.png",
            },
            {
                "aluno": """Rayssa Catharina Cunha de Mesquita""",
                "categoria": "Iniciacao Cientifica",
                "trabalho": """Construção das Regras formais para robôs móveis, oriundas de teorias de Vygotsky""",
                "descricao": """Projeto de Iniciação Científica. Orientador Principal: Rosiery da Silva Maia. Financiamento: Conselho Nacional de Desenvolvimento Científico e Tecnológico.""",
                "status": "Concluido",
                "imagem": "orientacao/rayssa_mesquita.png",
            },
        ]

        # Dados de Mensagem de Contato (não existem no database.py, mantém dummy)
        mensagens_data = [
            {"nome": "Visitante Curioso", "email": "curioso@exemplo.com", "assunto": "Dúvida sobre Área de Pesquisa",
             "mensagem": "Gostaria de saber mais sobre a área de sistemas autônomos.", "noticias": False},
            {"nome": "Parceiro Potencial", "email": "parceiro@empresa.com",
             "assunto": "Proposta de Colaboração em Projeto",
             "mensagem": "Temos uma oportunidade de parceria no projeto de IA.", "noticias": True},
            {"nome": "Ex-Aluno", "email": "exaluno@email.com", "assunto": "Agradecimento e Contato",
             "mensagem": "Só para agradecer a orientação e manter contato.", "noticias": True},
        ]

        # --- População dos Modelos ---

        # 1. Popula AreaPesquisa
        areas_objects_created = []
        for data in areas_pesquisa_data:
            area = AreaPesquisa.objects.create(nome=data["nome"], descricao=data["descricao"])
            # Associa os tópicos
            associated_topicos = [topicos_objects[t_name] for t_name in data["topicos_nomes"] if
                                  t_name in topicos_objects]
            area.topico.set(associated_topicos)
            areas_objects_created.append(area)
        print(f"-> Criadas {len(areas_objects_created)} Áreas de Pesquisa.")

        # 2. Popula Projeto
        projetos_objects_created = []
        for data in projetos_data:
            projeto = Projeto.objects.create(
                titulo=data["titulo"],
                descricao=data["descricao"],
                categoria=data["categoria"],
                financiamento=data["financiamento"],
                equipe=data["equipe"],
                imagem=data["imagem"]  # Atribui o caminho da imagem diretamente
            )
            # Associa os objetivos
            associated_objetivos = [objetivos_objects[o_name] for o_name in data["objetivos_nomes"] if
                                    o_name in objetivos_objects]
            projeto.objetivos.set(associated_objetivos)
            projetos_objects_created.append(projeto)
        print(f"-> Criados {len(projetos_objects_created)} Projetos.")

        # 3. Popula Publicacao
        publicacoes_objects_created = []
        for data in publicacoes_data:
            publicacao = Publicacao.objects.create(
                categoria=data["categoria"],
                titulo=data["titulo"],
                autores=data["autores"],
                ano=data["ano"],
                publicado_no=data["publicado_no"],
                descricao=data["descricao"],
                link=data["link"],
                arquivo=data["arquivo"]  # Atribui o caminho do arquivo diretamente
            )
            publicacoes_objects_created.append(publicacao)
        print(f"-> Criadas {len(publicacoes_objects_created)} Publicações.")

        # 4. Popula Orientacao
        orientacoes_objects_created = []
        for data in orientacoes_data:
            orientacao = Orientacao.objects.create(
                status=data["status"],
                aluno=data["aluno"],
                categoria=data["categoria"],
                trabalho=data["trabalho"],
                descricao=data["descricao"],
                imagem=data["imagem"]  # Atribui o caminho da imagem diretamente
            )
            orientacoes_objects_created.append(orientacao)
        print(f"-> Criadas {len(orientacoes_objects_created)} Orientações.")

        # 5. Popula MensagemContato
        for data in mensagens_data:
            sent_time = timezone.now() - timedelta(days=random.randint(1, 60), hours=random.randint(1, 23))
            MensagemContato.objects.create(
                nome=data["nome"],
                email=data["email"],
                assunto=data["assunto"],
                mensagem=data["mensagem"],
                noticias=data["noticias"],
                enviada_em=sent_time  # Agora é uma datetime "aware"
            )
        print(f"-> Criadas {len(mensagens_data)} Mensagens de Contato.")

        print("População de dados de exemplo para o app 'core' concluída com sucesso.")
