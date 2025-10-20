# PROCEDIMENTO DE PESQUISA
## Envelhecimento Ativo e Inclusão Digital no Brasil

**Projeto:** Envelhecimento, Big Data e Inclusão Digital  
**Tipo de Pesquisa:** Método Misto Sequencial Explanatório  
**Data:** Outubro de 2025  
**Versão:** 1.0

---

## SUMÁRIO

1. [Introdução](#introdução)
2. [Objetivos da Pesquisa](#objetivos-da-pesquisa)
3. [Desenho Metodológico](#desenho-metodológico)
4. [Fase 1: Análise Quantitativa (Big Data)](#fase-1-análise-quantitativa-big-data)
5. [Fase 2: Triangulação Analítica](#fase-2-triangulação-analítica)
6. [Fase 3: Coleta Qualitativa](#fase-3-coleta-qualitativa)
7. [Procedimentos Éticos](#procedimentos-éticos)
8. [Cronograma de Execução](#cronograma-de-execução)
9. [Controle de Qualidade](#controle-de-qualidade)
10. [Referências Metodológicas](#referências-metodológicas)

---

## INTRODUÇÃO

Este documento descreve o procedimento completo de pesquisa adotado no estudo sobre envelhecimento ativo e inclusão digital no Brasil. O procedimento foi estruturado para ser replicável, seguindo rigor metodológico e padrões científicos estabelecidos na literatura sobre métodos mistos.

## OBJETIVOS DA PESQUISA

### Objetivo Geral

Analisar a relação entre envelhecimento populacional e inclusão digital no Brasil, identificando determinantes, barreiras e perfis de envelhecimento digital através de abordagem quantitativa e qualitativa integrada.

### Objetivos Específicos

1. Caracterizar tendências demográficas de envelhecimento no Brasil (1990-2024)
2. Mensurar níveis de inclusão digital entre pessoas idosas (60+ anos)
3. Comparar padrões brasileiros com países desenvolvidos (benchmarking internacional)
4. Identificar determinantes estatísticos do uso de internet por idosos
5. Segmentar perfis de envelhecimento digital através de análise de clustering
6. Compreender experiências, motivações e barreiras vividas por idosos no acesso digital
7. Triangular achados quantitativos com narrativas qualitativas

---

## DESENHO METODOLÓGICO

### Tipo de Pesquisa

**Método Misto Sequencial Explanatório**

```
FASE 1 (QUANTITATIVA)
Análise de Big Data
↓
FASE 2 (INTEGRAÇÃO)
Triangulação Analítica
↓
FASE 3 (QUALITATIVA)
Entrevistas Semiestruturadas
↓
SÍNTESE FINAL
Integração de Resultados
```

### Fundamentação Teórica

O desenho sequencial explanatório é recomendado quando:
- A fase quantitativa precede e informa a qualitativa (Creswell & Plano Clark, 2018)
- Busca-se explicar resultados estatísticos através de dados narrativos
- Há necessidade de validação cruzada de achados

**Referências base:**
- Creswell, J. W., & Plano Clark, V. L. (2018). Designing and Conducting Mixed Methods Research (3rd ed.)
- Tashakkori, A., & Teddlie, C. (2010). Sage Handbook of Mixed Methods in Social & Behavioral Research

---

## FASE 1: ANÁLISE QUANTITATIVA (BIG DATA)

### 1.1 Fontes de Dados

#### Base 1: ONU/Atlas Brasil (1990-2010)
- **Fonte:** Programa das Nações Unidas para o Desenvolvimento (PNUD)
- **Acesso:** http://www.atlasbrasil.org.br
- **Dados:** CSV público com 229 variáveis demográficas/sociais/econômicas
- **Período:** 1991, 2000, 2010
- **Unidade:** Brasil (nível nacional)

#### Base 2: IBGE/PNAD Contínua (2019-2022)
- **Fonte:** Instituto Brasileiro de Geografia e Estatística
- **Acesso:** https://sidra.ibge.gov.br (Sistema SIDRA)
- **Tabelas utilizadas:**
  - Tabela 4820: Uso de internet por idosos 60+
  - Tabela 9542: Alfabetização por idade
  - Tabela 9756: Índice de envelhecimento por raça
  - Tabela 9942: Internet domiciliar por raça e idade
- **Período:** 2019-2022
- **Formato:** Excel (.xlsx)

#### Base 3: ITU - International Telecommunication Union (2000-2024)
- **Fonte:** União Internacional de Telecomunicações
- **Acesso:** https://www.itu.int/en/ITU-D/Statistics/
- **Datasets:**
  - Percentual de uso de internet (13.369 registros)
  - Uso semanal de internet (6.781 registros)
  - Posse de telefone celular (1.109 registros)
- **Período:** 2000-2024
- **Cobertura:** 258 países
- **Formato:** CSV

### 1.2 Procedimento de Coleta

#### Passo 1: Download dos Dados

**1.1 Dados ONU/Atlas Brasil:**
1. Acessar http://www.atlasbrasil.org.br
2. Navegar até seção "Consulta" > "Perfil Brasil"
3. Selecionar anos: 1991, 2000, 2010
4. Exportar arquivo CSV com todas as variáveis disponíveis
5. Salvar como: `Dados Brasil Onu 1990 - 2010.csv`

**1.2 Dados IBGE/PNAD:**
1. Acessar https://sidra.ibge.gov.br
2. Buscar por código de tabela (ex: 4820)
3. Selecionar variáveis de interesse:
   - Período: 2019-2022
   - Estratificações: idade, sexo, cor/raça (conforme tabela)
4. Exportar em formato Excel (.xlsx)
5. Repetir para as 4 tabelas necessárias
6. Salvar em pasta: `COLETA DE DADOS/Dados IBGE/`

**1.3 Dados ITU:**
1. Acessar https://www.itu.int/en/ITU-D/Statistics/Pages/stat/default.aspx
2. Navegar até "Data Explorer"
3. Selecionar indicadores:
   - "Percentage of individuals using the Internet"
   - "Percentage of individuals using the Internet - at least once a week"
   - "Individuals who own a mobile cellular telephone"
4. Filtrar países de interesse (ou baixar dataset completo)
5. Exportar em formato CSV
6. Salvar em pasta: `COLETA DE DADOS/Dataset ICT Indicators/`

#### Passo 2: Organização dos Arquivos

Criar estrutura de diretórios:

```
Projeto/
├── COLETA DE DADOS/
│   ├── Dados Brasil Onu 1990 - 2010.csv
│   ├── Dados IBGE/
│   │   ├── tabela4820.xlsx
│   │   ├── tabela9542.xlsx
│   │   ├── tabela9756.xlsx
│   │   └── tabela9942.xlsx
│   └── Dataset ICT Indicators/
│       ├── individuals-who-own-a-mobile-cellular-telephone_*.csv
│       ├── Percentage of individuals using the Internet - at least once a week.csv
│       └── Percentage of individuals using the internet (ITU).csv
├── data/
│   └── processed/ (dados limpos)
├── notebooks/
│   ├── 01_analise_exploratoria.ipynb
│   └── 02_integracao_analise_avancada.ipynb
├── reports/
│   ├── figures/ (visualizações)
│   └── tables/ (tabelas)
└── scripts/
    └── 01_inventario_datasets.py
```

### 1.3 Procedimento de Análise

#### Etapa 1: Inventário de Dados

**Objetivo:** Catalogar todas as bases disponíveis

**Ferramentas:** Python 3.13+, pandas 2.2+

**Script:** `scripts/01_inventario_datasets.py`

**Passos:**
1. Listar todos os arquivos nas pastas de dados
2. Extrair metadados: número de linhas, colunas, taxa de missing
3. Documentar variáveis disponíveis
4. Gerar CSV com inventário completo
5. Salvar em: `data/processed/inventario_datasets.csv`

#### Etapa 2: Análise Exploratória

**Objetivo:** Caracterizar tendências demográficas 1991-2010

**Notebook:** `notebooks/01_analise_exploratoria.ipynb`

**Passos detalhados:**

**2.1 Preparação do Ambiente**
```python
# Instalar dependências
pip install pandas numpy matplotlib seaborn

# Importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
```

**2.2 Carregamento de Dados**
```python
# Carregar dados ONU
df_onu = pd.read_csv('COLETA DE DADOS/Dados Brasil Onu 1990 - 2010.csv')

# Verificar estrutura
print(df_onu.shape)
print(df_onu.columns)
```

**2.3 Seleção de Indicadores-Chave**

Selecionar 12 variáveis principais:
- Expectativa de vida ao nascer
- Taxa de envelhecimento
- População 60+
- IDHM e subíndices
- Taxa de alfabetização
- Renda per capita
- Índice de Gini

**2.4 Análises Estatísticas**

a) Estatísticas descritivas:
   - Média, desvio-padrão, mínimo, máximo
   - Para cada indicador nos 3 anos

b) Análise temporal:
   - Evolução de 6 indicadores-chave
   - Cálculo de variação percentual
   - Gráficos de linha (6 painéis)

c) Correlação bivariada:
   - Matriz de correlação 12x12
   - Heatmap com coeficientes de Pearson
   - Identificação de relações fortes (|r| > 0.7)

d) Estrutura demográfica:
   - Distribuição por 3 faixas etárias (0-14, 15-59, 60+)
   - Gráfico de barras empilhadas
   - Evolução temporal da pirâmide

**2.5 Geração de Outputs**

Salvar em `reports/`:
- `figures/01_evolucao_indicadores.png`
- `figures/02_matriz_correlacao.png`
- `figures/03_estrutura_etaria.png`

#### Etapa 3: Análise Integrada Avançada

**Objetivo:** Integrar múltiplas fontes e realizar modelagem

**Notebook:** `notebooks/02_integracao_analise_avancada.ipynb`

**Passos detalhados:**

**3.1 Integração de Dados IBGE**

```python
# Carregar 4 tabelas IBGE
import glob

ibge_files = glob.glob('COLETA DE DADOS/Dados IBGE/*.xlsx')

# Processar cada tabela
for file in ibge_files:
    df = pd.read_excel(file, skiprows=5)  # Ajustar conforme estrutura
    # Limpar e padronizar
```

**3.2 Integração de Dados ITU**

```python
# Carregar dados ITU
df_itu = pd.read_csv('COLETA DE DADOS/Dataset ICT Indicators/Percentage of individuals using the internet (ITU).csv')

# Filtrar países de interesse
paises_selecionados = ['Brazil', 'Portugal', 'Spain', 'United States', 'Japan', ...]
df_itu_filtrado = df_itu[df_itu['Country'].isin(paises_selecionados)]

# Filtrar período 2015-2024
df_itu_filtrado = df_itu_filtrado[df_itu_filtrado['Year'] >= 2015]
```

**3.3 Análise de Estratificação**

Objetivo: Analisar uso de internet por idade e sexo

```python
# Criar dados sintéticos baseados em PNAD (até dados reais disponíveis)
grupos_idade = ['60-64', '65-69', '70-74', '75+']
anos = [2019, 2020, 2021, 2022]
sexos = ['Masculino', 'Feminino']

# Gerar matriz de estratificação
# Calcular gaps de gênero
# Visualizar em 4 painéis
```

**3.4 Gap Analysis Internacional**

Objetivo: Comparar Brasil com países desenvolvidos

```python
# Calcular média para Brasil (2020-2023)
brasil_media = df_itu_filtrado[df_itu_filtrado['Country']=='Brazil']['Value'].mean()

# Calcular média OCDE
ocde_paises = ['United States', 'Japan', 'Germany', 'France', ...]
ocde_media = df_itu_filtrado[df_itu_filtrado['Country'].isin(ocde_paises)]['Value'].mean()

# Calcular gaps
gap_ocde = brasil_media - ocde_media
gap_lider = brasil_media - df_itu_filtrado.groupby('Country')['Value'].mean().max()

# Visualizar em 4 painéis:
# - Ranking de países
# - Gap vs. líder
# - Evolução temporal
# - Brasil vs. OCDE
```

**3.5 Regressão Logística**

Objetivo: Identificar determinantes do uso de internet

**Variável dependente:** Uso de internet (0=não, 1=sim)

**Variáveis independentes:**
- Idade (anos)
- Escolaridade (anos de estudo)
- Renda (R$)
- Sexo (0=feminino, 1=masculino)
- Área (0=rural, 1=urbana)

**Procedimento:**
```python
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

# 1. Gerar dados sintéticos (n=500) baseados em literatura
# 2. Dividir treino/teste (70/30)
# 3. Padronizar variáveis
# 4. Ajustar modelo logístico
# 5. Calcular Odds Ratios
# 6. Avaliar acurácia
# 7. Gerar matriz de confusão
```

**Interpretação:**
- OR > 1: fator de risco (aumenta chance de uso)
- OR < 1: fator de proteção (diminui chance)
- OR = 1: sem associação

**3.6 Clustering K-means**

Objetivo: Identificar perfis de envelhecimento digital

**Variáveis de segmentação:**
- Idade
- Escolaridade
- Renda
- Horas online/semana
- Número de dispositivos
- Frequência de compras online

**Procedimento:**
```python
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# 1. Gerar dados sintéticos (n=300)
# 2. Padronizar variáveis (Z-score)
# 3. Determinar k ótimo (método do cotovelo + silhouette)
# 4. Ajustar K-means com k=4
# 5. Interpretar perfis
# 6. Calcular estatísticas por cluster
# 7. Visualizar em 7 painéis
```

**Perfis esperados:**
- Conectados Ativos (alta escolaridade, alta renda)
- Usuários Moderados (escolaridade média)
- Adotantes Recentes (mais velhos, baixa escolaridade)
- Excluídos Digitais (muito idosos, sem acesso)

**3.7 Geração de Outputs**

Salvar em `reports/`:
- `figures/04_estratificacao_internet_idosos.png`
- `figures/05_gap_analysis_internacional.png`
- `figures/06_regressao_determinantes.png`
- `figures/07_clustering_perfis_digitais.png`
- `tables/perfis_envelhecimento_digital.csv`

### 1.4 Controle de Qualidade - Dados Quantitativos

**Critérios de Qualidade:**

1. **Completude:** Taxa de missing < 30% (aceitável até 60% em tabulações IBGE)
2. **Consistência:** Valores dentro de ranges esperados (ex: % entre 0-100)
3. **Atualidade:** Dados ITU atualizados anualmente
4. **Comparabilidade:** Harmonização de variáveis entre fontes

**Procedimentos de Validação:**

- Verificar somas de percentuais = 100%
- Comparar tendências com literatura
- Cross-check com outras fontes (Censo, PNAD)
- Documentar todas as decisões de limpeza

---

## FASE 2: TRIANGULAÇÃO ANALÍTICA

### 2.1 Objetivo

Criar matriz de triangulação para integrar achados quantitativos com futuros dados qualitativos.

### 2.2 Procedimento

#### Passo 1: Identificar Temas Quantitativos

Da análise de dados, extrair 6 temas principais:
1. Envelhecimento populacional acelerado
2. Gap digital por idade
3. Gap digital por gênero
4. Desigualdades socioeconômicas (educação, renda)
5. Comparação internacional
6. Perfis de uso digital

#### Passo 2: Criar Matriz de Triangulação

**Ferramenta:** Excel com 5 abas

**Estrutura:**

| Tema Quantitativo | Indicador | Achado Principal | Questão Qualitativa | Citação Prevista |
|-------------------|-----------|------------------|---------------------|-------------------|
| Gap digital idade | % uso internet 75+ | 23.6% (2022) | Como você começou a usar internet? | [A completar] |

**Arquivo:** `TRIANGULACAO_ANALITICA.xlsx`

#### Passo 3: Validação

- Revisar matriz com orientador
- Ajustar questões qualitativas conforme necessário
- Preparar para orientar roteiro de entrevistas

## FASE 3: COLETA QUALITATIVA

### 3.1 Desenho Qualitativo

**Método:** Entrevistas

**Fundamentação:** 
- Permite aprofundamento de temas quantitativos
- Flexibilidade para explorar narrativas emergentes
- Adequado para população idosa (mais confortável que grupos focais)

**Referências:**
- Fontanella, B. J. B., et al. (2011). Amostragem em pesquisas qualitativas
- Minayo, M. C. S. (2017). Amostragem e saturação em pesquisa qualitativa

### 3.2 Participantes

#### Status da Coleta (Outubro 2025)

**Entrevistas realizadas:** 1 (uma)
- **Formato:** Presencial
- **Data:** Outubro de 2025
- **Arquivo:** `COLETA DE DADOS/Entrevistas/Entrevista 1.pdf`

#### Critérios de Inclusão:
- Idade: 60 anos ou mais
- Residência: Brasil (qualquer região)
- Capacidade: Comunicação verbal preservada
- Diversidade: Representar os 4 perfis de clustering

#### Critérios de Exclusão:
- Deficiências cognitivas severas
- Impossibilidade de consentimento informado


**Arquivo:** `docs/TCLE_Entrevistas.pdf`

### Proteção de Dados

**Conformidade com LGPD (Lei 13.709/2018):**

1. **Coleta:** Apenas dados necessários para pesquisa
2. **Armazenamento:**
   - Gravações: computador com senha + backup criptografado
   - Transcrições: removidas informações identificadoras
   - Prazo: 5 anos após publicação
3. **Acesso:** Apenas pesquisador e orientador
4. **Anonimização:** Substituir nomes por códigos (P01, P02...)
5. **Descarte:** Após 5 anos, deletar permanentemente

---

## ENTREVISTA REALIZADA: RELATÓRIO PILOTO

### Entrevista 1 - Outubro 2025

**Status:** CONCLUÍDA

**Formato:** Presencial (única entrevista realizada face a face)

**Arquivo:** `COLETA DE DADOS/Entrevistas/Entrevista 1.pdf`

### Contexto da Entrevista

Esta entrevista foi realizada presencialmente e constitui a única coleta qualitativa do projeto devido a restrições de tempo.

### Função no Estudo

A entrevista serve para:
- Ilustrar os padrões identificados nos dados quantitativos
- Contextualizar as estatísticas com uma narrativa real
- Demonstrar a aplicação do protocolo desenvolvido

### Análise Preliminar

- Usar a entrevista para ilustrar os padrões identificados

### Limitações

**Amostra reduzida:**
- Apenas 1 entrevista foi realizada (limitação de tempo)
- Os resultados qualitativos não podem ser generalizados
- A entrevista tem função ilustrativa dos achados quantitativos

**Recomendação para estudos futuros:**
- Realizar 12-20 entrevistas para maior representatividade

---

## LIMITAÇÕES DO ESTUDO

### Fase Qualitativa

**Limitação principal:** Apenas 1 entrevista foi realizada devido a restrições de tempo.

**Impacto:**
- Os dados qualitativos têm caráter ilustrativo, não generalizável
- A entrevista contextualiza os achados quantitativos com um exemplo real
- Não é possível representar a diversidade de experiências dos idosos

### Caracterização do Estudo

Este é um estudo **predominantemente quantitativo** (21.303 registros, 8 bases de dados) com uma entrevista qualitativa ilustrativa.

---

## REFERÊNCIAS METODOLÓGICAS

### Livros

1. **Creswell, J. W., & Plano Clark, V. L. (2018).** *Designing and Conducting Mixed Methods Research* (3rd ed.). SAGE Publications.
   - Capítulos 3-4: Desenhos sequenciais explanatórios

1.5. **Stake, R. E. (1995).** *The Art of Case Study Research.* SAGE Publications.
   - Estudo de caso único: metodologia e limitações

2. **Minayo, M. C. S. (2017).** *Amostragem e saturação em pesquisa qualitativa: consensos e controvérsias.* Revista Pesquisa Qualitativa, 5(7), 01-12.

3. **Braun, V., & Clarke, V. (2006).** Using thematic analysis in psychology. *Qualitative Research in Psychology*, 3(2), 77-101.

4. **Lincoln, Y. S., & Guba, E. G. (1985).** *Naturalistic Inquiry.* SAGE Publications.

### Artigos

5. **Fontanella, B. J. B., et al. (2011).** Amostragem em pesquisas qualitativas: proposta de procedimentos para constatar saturação teórica. *Cadernos de Saúde Pública*, 27(2), 388-394.

6. **Tashakkori, A., & Teddlie, C. (2010).** *Sage Handbook of Mixed Methods in Social & Behavioral Research* (2nd ed.). SAGE Publications.

### Websites

9. **Atlas Brasil:** http://www.atlasbrasil.org.br
10. **IBGE/SIDRA:** https://sidra.ibge.gov.br
11. **ITU Statistics:** https://www.itu.int/en/ITU-D/Statistics/
12. **Plataforma Brasil:** https://plataformabrasil.saude.gov.br

---

## ANEXOS

### Anexo A: Glossário de Termos

- **Big Data:** Conjuntos de dados volumosos, variados e de alta velocidade
- **Clustering:** Técnica de agrupamento de observações similares
- **Gap digital:** Diferença no acesso e uso de tecnologias digitais
- **IDHM:** Índice de Desenvolvimento Humano Municipal
- **ITU:** International Telecommunication Union (União Internacional de Telecomunicações)
- **K-means:** Algoritmo de clustering por partição
- **Odds Ratio (OR):** Razão de chances em modelos logísticos
- **PNAD:** Pesquisa Nacional por Amostra de Domicílios
- **Saturação teórica:** Ponto em que novos dados não acrescentam informações
- **TCLE:** Termo de Consentimento Livre e Esclarecido
- **Triangulação:** Uso de múltiplas fontes/métodos para validar achados

### Anexo B: Modelos de Documentos

**Disponíveis em `docs/`:**
- MATRIZ_TRIANGULACAO.csv
- TRIANGULACAO_ANALITICA.xlsx
- RESUMO_METODOLOGIA_PDFS.md
- Analise de Dados.md
- PROCEDIMENTO_PESQUISA.md

### Anexo C: Scripts e Notebooks

**Disponíveis em `notebooks/` e `scripts/`:**
- 01_inventario_datasets.py
- 01_analise_exploratoria.ipynb
- 02_integracao_analise_avancada.ipynb

### Anexo D: Entrevistas Qualitativas

**Disponível em `COLETA DE DADOS/Entrevistas/`:**
- Entrevista 1.pdf (Entrevista presencial, Outubro 2025)

**Observação:** Devido a restrições de tempo, apenas 1 entrevista foi realizada. Os dados têm função ilustrativa dos achados quantitativos.
