# Análise de Dados sobre Home Office na Pandemia (2020–2021)

## Descrição do Projeto
Este projeto acadêmico de Ciência de Dados tem como objetivo analisar dados relevantes sobre o cenário de **home office durante a pandemia de COVID-19 (2020–2021)**.

A proposta é entender como o trabalho remoto impactou a produtividade, preferências e percepções dos trabalhadores durante o período de lockdown.

---

## Objetivos
- Analisar a adoção do trabalho remoto durante a pandemia  
- Avaliar a percepção de produtividade dos trabalhadores  
- Identificar barreiras e benefícios do home office  
- Compreender as expectativas para o futuro do trabalho remoto  

---

## Integrantes do Grupo - 1 fase
- Igor Werneck Jacobosque  
- João Vitor Cândido de Andrade  
- Christian Neis Rodrigues
- Francisco Cury Bernardi
- Admilson Muniz Ramos 

## Integrantes do Grupo - Participantes efetivos da 2 fase
- Igor Werneck Jacobosque  
- João Vitor Cândido de Andrade 

---

## Tecnologias Utilizadas
- Python 3.14.4
- Pandas (análise de dados)
- Matplotlib / Seaborn (visualizações)
- Streamlit (dashboard interativo)
- NumPy (cálculos numéricos)

---

## Dataset
- **Total de respondentes**: 3.019 pessoas
- **Total de variáveis**: 73 colunas
- **Período**: 2020-2021 (durante a pandemia de COVID-19)
- **Formato**: CSV (Dataset.csv + Dataset_PT.csv traduzido)
- **Tamanho**: ~1.5 MB (cada versão)
- **Idioma**: Original em Inglês | Versão Traduzida em Português

---

## Tradução do Dataset

O projeto inclui um **script de tradução automática** (`src/traducao.py`) que:
- Traduz todos os valores do dataset para português
- Converte 121.698+ valores individuais
- Mantém integridade estrutural dos dados
- Gera arquivo `Dataset_PT.csv` para análise em português

### Executar Tradução
```bash
python src/traducao.py
```

---

## Estrutura do Projeto

```
ciencia-dados-trabalho-remoto-pandemia/
├── README.md                 # Este arquivo
├── data/
│   ├── Dataset.csv          # Dataset original (inglês)
│   └── Dataset_PT.csv       # Dataset traduzido (português) 🆕
├── src/
│   ├── etl.py               # Carregamento e exploração
│   ├── metrics.py           # Cálculo das 5 métricas principais
│   ├── visualizations.py    # Geração de gráficos PNG
│   └── traducao.py          # Script de tradução 🆕
├── app/
│   └── dashboard.py         # Dashboard Streamlit (v3 - traduzido) 🆕
├── visualizations/          # Gráficos gerados (PNG)
├── .gitignore              # Arquivo de controle Git 🆕
└── .venv/                  # Ambiente virtual Python
```

---

## Dashboard Streamlit (Versão 3 - Completo)

### 📖 Seções Disponíveis

#### 1️⃣ 📈 **Resumo Executivo**
- Estatísticas gerais do projeto
- Principais descobertas resumidas
- Lacuna entre realidade e preferência de trabalho remoto
- Insights críticos para decisões

#### 2️⃣ 👥 **Adoção do Trabalho Remoto**
- Comparação: tempo real vs. tempo preferido
- Gráficos horizontais com contexto
- Identificação de demanda reprimida
- Tendências de flexibilização

#### 3️⃣ 💼 **Produtividade Percebida**
- Autopercepção detalhada
- Cards com percentuais (positiva/neutra/reduzida)
- Distribuição de 12 categorias
- Análise por tipo de resposta

#### 4️⃣ 🚧 **Principais Barreiras**
- Top 15 obstáculos ao trabalho remoto
- Slider dinâmico para exploração
- Classificação por criticidade
- Insights sobre desafios motivacionais vs. técnicos

#### 5️⃣ ✨ **Benefícios Identificados**
- Top 15 aspectos positivos
- Slider dinâmico de visualização
- Progress bars de frequência
- Destaque em equilíbrio vida-trabalho

#### 6️⃣ 🔮 **Perspectiva Pós-Pandemia**
- Preferências para futuro do trabalho
- Classificação: Muito Remoto / Híbrido / Presencial
- Análise de tendências estruturais
- Recomendações estratégicas

### ✨ Características Técnicas

- ✅ **100% em Português** - Sem palavras em inglês
- ✅ **Visualizações Enriquecidas** - Com contexto, títulos informativos e anotações
- ✅ **Cores Temáticas** - Paletas profissionais (Greens, Reds, Blues, etc.)
- ✅ **Interatividade** - Sliders, progress bars e navegação fluida
- ✅ **Responsividade** - Layout adaptativo para diferentes tamanhos
- ✅ **Performance** - Cache de dados para carregamento rápido
- ✅ **Acessibilidade** - Textos descritivos e legendas explicativas

---

## Como Executar o Projeto

### 1. Ativar o Ambiente Virtual
```bash
.\.venv\Scripts\activate
```

### 2. Instalar Dependências
```bash
pip install pandas matplotlib seaborn streamlit numpy
```

### 3. Executar Tradução do Dataset (Primeiro Uso)
```bash
python src/traducao.py
```
Isso criará o arquivo `Dataset_PT.csv` com todos os dados traduzidos para português.

### 4. Rodar o Dashboard Streamlit
```bash
streamlit run app/dashboard.py
```

O dashboard estará disponível em: **http://localhost:8501**

### 5. (Opcional) Gerar Visualizações PNG Estáticas
```bash
python src/visualizations.py
```

---

## Resultados Principais

### 📊 Adoção do Trabalho Remoto
- **20%** é o tempo mais comum de trabalho remoto realizado
- **50% - About half of my time** é a preferência mais mencionada
- Discrepância entre realidade e preferência indica demanda reprimida de trabalho remoto

### 💼 Percepção de Produtividade
- **34%** dos trabalhadores percebem produtividade **positiva** no home office
- **34%** percebem produtividade **neutra** (igual ao presencial)
- **32%** percebem produtividade **negativa**
- Principais categorias: "Somewhat Positive" (19.3%) e "Strongly Positive" (14.7%)

### 🚧 Principais Barreiras
1. **Falta de motivação** (2.211 menções)
2. **Dificuldade em colaborar remotamente** (1.763 menções)
3. **Sentimento de isolamento** (1.561 menções)
4. **Equipamento de TI inadequado** (1.299 menções)
5. **Conectividade/Internet** (1.155 menções)

### ✨ Melhores Aspectos
1. **Equilíbrio vida/trabalho** (1.829 menções)
2. **Economia em deslocamento** (1.485 menções)
3. **Gerenciamento de compromissos pessoais** (1.082 menções)
4. **Redução de despesas** (972 menções)
5. **Responsabilidades familiares** (733 menções)

### 🔮 Preferência Pós-Pandemia
- **36%** desejam continuar trabalhando remotamente após a pandemia
- **37%** têm respostas neutras ou indefinidas
- **27%** preferem retornar ao trabalho presencial
- Indica mudança permanente na dinâmica do trabalho

---

## Dashboard Streamlit

O dashboard interativo possui **6 seções principais**:

#### 📈 Visão Geral
- Estatísticas gerais do projeto (3.019 respondentes, 73 variáveis)
- Resumo das áreas de análise

#### 👥 Adoção Remota
- Gráficos comparativos: tempo real vs. tempo preferido
- Top 10 categorias em ambas dimensões

#### 💼 Produtividade
- Distribuição detalhada da percepção de produtividade
- Métricas: % positiva, neutra e negativa
- Top 15 categorias de respostas

#### 🚧 Barreiras
- **Slider interativo** para ajustar número de barreiras (5-15)
- Gráfico dinâmico das principais barreiras mencionadas
- Filtros automáticos para dados inválidos

#### ✨ Aspectos Positivos
- **Slider interativo** para ajustar número de aspectos (5-15)
- Visualização dos melhores aspectos mencionados
- Insights sobre benefícios do home office

#### 🔮 Futuro (Pós-Pandemia)
- Distribuição de preferências futuras
- Top 15 categorias de respostas
- Insights sobre mudanças permanentes no trabalho

---

## Arquivos de Código

### `src/etl.py`
- Carregamento do dataset com tratamento de encoding
- Exploração inicial (primeiras linhas, tipos de dados, valores nulos)
- Limpeza e renomeação de colunas para facilitar análise
- Função main() para rodar ETL completo

### `src/metrics.py`
Cálcula 5 métricas principais:
1. Adoção do trabalho remoto
2. Percepção de produtividade
3. Principais barreiras
4. Melhores aspectos
5. Preferência futura pós-pandemia

Cada métrica inclui análise detalhada, contagens e percentuais.

### `src/visualizations.py`
Gera 5 gráficos em PNG:
1. `produtividade.png` - Top 10 categorias de produtividade
2. `barreiras.png` - Top 10 principais barreiras
3. `aspectos_positivos.png` - Top 10 melhores aspectos
4. `tempo_remoto.png` - Distribuição de tempo remoto realizado
5. `preferencia_futura.png` - Preferência de trabalho remoto pós-pandemia

### `app/dashboard.py`
Dashboard Streamlit com:
- Navegação por sidebar com 6 seções
- Cache de dados para performance
- Gráficos interativos com Matplotlib
- Sliders para ajuste dinâmico de visualizações
- Métricas e insights em cards

---

## Insights Principais

1. **Discrepância entre realidade e preferência**: Trabalhadores gostariam de trabalhar mais remotamente do que efetivamente trabalham

2. **Produtividade mista**: Não há consenso sobre impacto na produtividade, mas ligeira tendência positiva (34% positiva vs 32% negativa)

3. **Motivação é desafio**: A falta de motivação é citada mais de 2.200 vezes como barreira principal

4. **Benefício maior é equilíbrio vida/trabalho**: Mais importante que economia de tempo ou dinheiro

5. **Mudança permanente**: Mesmo após pandemia, 36% querem continuar remotamente, indicando transformação duradoura

---

## Autores

### Fase 1
- Igor Werneck Jacobosque  
- João Vitor Cândido de Andrade  
- Christian Neis Rodrigues
- Francisco Cury Bernardi
- Admilson Muniz Ramos 

### Fase 2 (Implementação & Dashboard)
- Igor Werneck Jacobosque  
- João Vitor Cândido de Andrade 

---

## Link do Trello
https://trello.com/invite/b/69a8a83d30e71f6c46aa708c/ATTI3f9fddcd2e08ec4e89cead6954a1378cC49058B8/analise-trabalho-remoto-na-pandemia

---

## Observações

- Todos os scripts utilizam Pandas para análise exploratória
- O nível de implementação é iniciante-intermediário, conforme solicitado
- O dashboard é interativo e permite exploração visual dos dados
- Dados com encoding latin-1 (tratado no ETL)
- Visualizações focadas em clareza e compreensão dos dados

**Desenvolvido em**: Maio de 2026
