Intro
O objetivo deste exercício é desenvolver um robô de automação de processos utilizando a biblioteca Selenium WebDriver em conjunto com técnicas de Inteligência Artificial para interpretar e extrair dados relevantes de
páginas web dinâmicas.
Contexto
Robotic Process Automation (RPA) consiste na utilização de scripts e agentes virtuais para executar tarefas repetitivas, normalmente realizadas por
humanos, de forma automática e eficiente. O uso de IA neste contexto permite que o robô vá além da execução mecânica, tomando decisões baseadas
em padrões, previsões ou análise de conteúdo.
O Books to Scrape é um site público projetado para treinamento e testes
de automação e raspagem de dados, contendo uma lista paginada de livros
com informações como título, preço, disponibilidade e classificação por estrelas.
Tarefa
Implemente um script Python que:
1. Acesse o site https://books.toscrape.com e percorra todas as páginas
da listagem de livros.
2. Utilize seletores CSS e/ou expressões XPath para extrair:
• Título do livro.
• Preço.
1
• Disponibilidade em estoque.
• Classificação em estrelas.
3. Salve os dados brutos em um arquivo CSV ou JSON.
4. Aplique um módulo de para:
• Classificar os livros em duas categorias: Alto Valor (preço acima
da mediana dos preços coletados) ou Baixo Valor.
• Detectar padrões, como categorias com maior número de livros
acima da média de preço.
5. Gere um relatório final contendo:
• Resumo da coleta (número total de livros, preço médio, preço
máximo e mínimo).
• Distribuição das categorias Alto Valor e Baixo Valor.
• Observações relevantes e descritivo de como realizou a classificação
e o motivo.
Requisitos Técnicos
• Implementação em Python 3.
• Uso obrigatório da biblioteca Selenium e do webdriver_manager.
• Para a IA, pode-se utilizar scikit-learn, pandas e numpy para análise
estatística ou aprendizado de máquina.
• O código deve estar modularizado, com funções claras para coleta, processamento e análise.
Entregáveis
1. Código-fonte do robô.
2. Arquivo CSV/JSON com os dados coletados.
3. Relatório em PDF contendo os resultados e análises.
4. Documento curto descrevendo:
• O fluxo da automação.
• A metodologia da análise com IA.
• Desafios e soluções.
2
Critérios de Avaliação
• Funcionamento correto do robô Selenium (coleta completa de todas as
páginas).
• Implementação coerente da análise com IA.
• Qualidade do código e organização.
• Clareza e profundidade das análises apresentadas no relatório.



