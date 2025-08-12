# Documentação do Projeto

## Fluxo da Automação
1. Inicializa o WebDriver com `selenium` e acessa `https://books.toscrape.com`.
2. Percorre todas as páginas utilizando o botão "Next".
3. Extrai título, preço, disponibilidade e classificação de cada livro.
4. Armazena os dados coletados em `dados/livros.csv`.

## Metodologia de Análise com IA
- Calcula a mediana dos preços.
- Classifica cada livro em **Alto Valor** (preço acima da mediana) ou **Baixo Valor** (preço abaixo ou igual à mediana).
- Gera estatísticas resumidas e distribuição das categorias.

## Desafios e Soluções
- **Paginação**: utilização de um laço que avança por `li.next a` até que não existam mais páginas.
- **Ambiente Headless**: uso de opções do Chrome para execução em modo headless.
- **Geração de Relatório**: uso do `matplotlib` para criar um PDF simples com as informações básicas.
