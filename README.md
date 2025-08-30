
# 📚 Web_Scraping_IA

## 👨‍🏫 Integrantes 
Matheus Hungaro Fidelis – RM:555677
Tiago Toshio Kumagai Gibo – RM:556984
Danilo Ramalho Silva – RM:555183
João Vitor Pires da Silva – RM:556213
Pablo Menezes Barreto – RM:556389
Israel Dalcin Alves Diniz – RM:554668

## 📝 Descrição do Projeto
O **Web_Scraping_IA** é um projeto de **RPA (Robotic Process Automation)** que utiliza **Python, Selenium WebDriver** e técnicas de **Inteligência Artificial** para realizar raspagem e análise inteligente de dados no site [Books to Scrape](https://books.toscrape.com).  
O objetivo é automatizar a coleta de informações de livros, aplicar análise estatística/machine learning para identificar padrões e gerar relatórios detalhados.

---

## 🎯 Objetivos
- Automatizar a navegação em páginas web dinâmicas.
- Extrair dados estruturados (título, preço, disponibilidade e classificação).
- Armazenar os dados em formato **CSV** ou **JSON**.
- Aplicar análise com IA para classificar e encontrar padrões.
- Gerar relatório final com estatísticas e insights.

---

## ⚙️ Tecnologias Utilizadas
- **Linguagem**: Python 3
- **Bibliotecas Principais**:
  - `selenium` – automação de navegação e coleta de dados.
  - `webdriver_manager` – gerenciamento automático do driver.
  - `pandas` – manipulação e análise de dados.
  - `numpy` – cálculos estatísticos.
  - `scikit-learn` – suporte à classificação e análise de padrões.
- **Formato de Saída**:
  - Arquivo `.csv` ou `.json` com dados brutos.
  - Relatório em `.pdf`.

---

## 📂 Estrutura do Projeto
```
Web_Scraping_IA/
│
├── src/
│   ├── coleta_dados.py          # Funções para automação e extração
│   ├── processamento.py         # Limpeza e preparação dos dados
│   ├── analise_ia.py             # Classificação e detecção de padrões
│   ├── relatorio.py              # Geração de relatório final
│   └── utils.py                  # Funções auxiliares
│
├── dados/
│   ├── livros.csv                # Dados coletados
│   └── livros.json               # Dados coletados (opcional)
│
├── relatorios/
│   └── relatorio_final.pdf       # Relatório com análises e insights
│
├── requirements.txt              # Dependências do projeto
├── README.md                     # Documentação do projeto
└── main.py                       # Script principal
```

---

## 🔄 Fluxo da Automação
1. **Inicialização do WebDriver**  
   O Selenium acessa o site e percorre todas as páginas de listagem.
   
2. **Coleta de Dados**  
   Extração via **seletores CSS/XPath** dos seguintes campos:
   - Título do livro
   - Preço
   - Disponibilidade em estoque
   - Classificação em estrelas

3. **Armazenamento Bruto**  
   Salvamento dos dados no formato CSV ou JSON.

4. **Análise com IA**  
   - Cálculo da **mediana de preços**.
   - Classificação em:
     - **Alto Valor** → acima da mediana.
     - **Baixo Valor** → abaixo ou igual à mediana.
   - Identificação de categorias mais caras e padrões relevantes.

5. **Geração de Relatório**  
   Relatório final contendo:
   - Estatísticas (total de livros, preço médio, máximo, mínimo).
   - Distribuição das classificações (Alto/Baixo Valor).
   - Observações e justificativa das classificações.

---

## 📊 Saídas Esperadas
- **livros.csv** ou **livros.json** contendo todos os registros coletados.
- **relatorio_final.pdf** com:
  - Número total de livros.
  - Preço médio, mínimo e máximo.
  - Gráficos de distribuição.
  - Análise e justificativa de categorização.

---

## 🚀 Como Executar
### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/seuusuario/Web_Scraping_IA.git
cd Web_Scraping_IA
```

### 2️⃣ Criar e ativar o ambiente virtual
```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Executar o projeto
```bash
python main.py
```

---

## 📌 Requisitos Técnicos
- **Python 3.x** instalado.
- Conexão à internet para acessar o site e baixar WebDriver.
- Compatibilidade com Google Chrome ou Firefox.

---

## 🧠 Metodologia de Análise com IA
- Utiliza estatística descritiva para calcular a mediana dos preços.
- Classificação binária baseada no valor em relação à mediana.
- Detecção de padrões com agrupamento e análise exploratória.

---

## 🛠 Desafios e Soluções
- **Paginação**: Implementado loop de navegação até a última página detectando botões de "Next".
- **Sites dinâmicos**: Utilização de `WebDriverWait` para aguardar carregamento de elementos.
- **Classificação de preços**: Uso da mediana para evitar distorção por outliers.

---

## 🏆 Critérios de Avaliação
- Funcionalidade completa do robô.
- Implementação correta da análise de IA.
- Código organizado e modular.
- Clareza no relatório e nas análises.

---
