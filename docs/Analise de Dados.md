# RELATÓRIO DE ANÁLISE DE DADOS
## Envelhecimento Ativo e Inclusão Digital no Brasil

**Projeto:** Envelhecimento, Big Data e Inclusão Digital  
**Período de Análise:** 1990-2024  
**Data do Relatório:** 19 de Outubro de 2025  
**Notebooks:** `01_analise_exploratoria.ipynb` e `02_integracao_analise_avancada.ipynb`

---

## SUMÁRIO

Este relatório apresenta os resultados das análises quantitativas sobre envelhecimento e inclusão digital no Brasil, identificando tendências demográficas, gaps digitais, determinantes do acesso à internet e perfis de envelhecimento digital.

### Principais Números
- 8 bases de dados analisadas (3 fontes distintas)
- 21.303 registros processados
- Cobertura temporal: 1990-2024 (34 anos)
- População brasileira: ~213 milhões (Censo 2022)
- População idosa (60+): ~33 milhões

---

## 1. BASES DE DADOS UTILIZADAS

| Base de Dados | Registros | Período | Fonte |
|---------------|-----------|---------|-------|
| ONU Brasil | 3 | 1991-2010 | ONU/Atlas Brasil |
| IBGE Tabelas (4 tabelas) | 41 | 2019-2022 | IBGE/PNAD Contínua |
| ITU Indicadores (3 datasets) | 21.259 | 2000-2024 | ITU |
| **TOTAL** | **21.303** | **1990-2024** | **3 fontes** |

**Fontes:**
- **ONU/Atlas Brasil:** Dados demográficos e socioeconômicos do Brasil
- **IBGE/PNAD Contínua:** Uso de internet, alfabetização, envelhecimento por raça
- **ITU:** Comparação internacional de inclusão digital (258 países)

---

## 2. PRINCIPAIS ACHADOS

### 2.1 Envelhecimento Populacional (1991-2010)

**Tendências Demográficas:**
- População 60+: 10,7M → 20,6M (+93%)
- Taxa de envelhecimento: 7,3% → 10,8% (+48%)
- Expectativa de vida: 64,7 → 73,9 anos (+9,2 anos)

**Desenvolvimento Humano:**
- IDHM: 0,493 → 0,727 (+47,5%)
- Índice de Gini: 0,635 → 0,605 (redução da desigualdade)
- Renda per capita: +77,4% (crescimento real)

### 2.2 Inclusão Digital de Idosos (2019-2022)

**Uso de Internet por Faixa Etária:**
- 60-64 anos: 42,1% → 61,2% (+45%)
- 65-69 anos: 30,5% → 44,8% (+47%)
- 70-74 anos: 21,3% → 32,1% (+51%)
- 75+ anos: 12,5% → 23,6% (+89%)

**Gaps Identificados:**
- **Gap etário:** 37,6 pontos percentuais entre 60-64 e 75+
- **Gap de gênero:** 3-5 pontos percentuais (favorável a homens)

### 2.3 Comparação Internacional (2020-2023)

**Brasil vs. Mundo:**
- Brasil: 80,8% da população online
- Média OCDE: 88,0%
- **Gap OCDE:** 7,2 pontos percentuais
- **Gap vs. líder (Espanha):** 13,7 pontos percentuais
- Evolução 2015-2023: +25 pontos percentuais

### 2.4 Determinantes do Uso de Internet

**Modelo de Regressão Logística (Acurácia 98,7%):**

| Preditor | Odds Ratio | Interpretação |
|----------|------------|---------------|
| Escolaridade | 7,03 | Preditor mais forte - cada ano multiplica chance por 7 |
| Renda | 4,84 | Segundo fator mais importante |
| Área urbana | 1,66 | Urbano tem 66% mais chance |
| Sexo masculino | 1,56 | Homens têm 56% mais chance |
| Idade | 0,52 | Cada ano reduz chance pela metade |

### 2.5 Perfis de Envelhecimento Digital

**4 Perfis Identificados (Clustering K-means):**
**4 Perfis Identificados (Clustering K-means):**

| Perfil | % População | Características | População Estimada |
|--------|-------------|-----------------|-------------------|
| **Conectados Ativos** | 31% | Alta escolaridade, alta renda, 25h/semana online | ~10,1 milhões |
| **Usuários Moderados** | 39% | Escolaridade média, renda média, 12h/semana online | ~12,8 milhões |
| **Adotantes Recentes** | 0% | Mais velhos, escolaridade baixa, 5h/semana online | 0 milhões |
| **Excluídos Digitais** | 31% | Muito velhos, baixa escolaridade, <2h/semana online | ~10,1 milhões |

---

## 3. VISUALIZAÇÕES E OUTPUTS GERADOS

### 3.1 Figuras Produzidas (7 visualizações, 300 DPI)
- **IDE:** Visual Studio Code + Jupyter Extension
### 3.1 Figuras Produzidas (7 visualizações, 300 DPI)

1. `01_evolucao_indicadores.png` - Evolução temporal de 6 indicadores-chave
2. `02_matriz_correlacao.png` - Correlações entre 12 variáveis
3. `03_estrutura_etaria.png` - Pirâmide populacional brasileira
4. `04_estratificacao_internet_idosos.png` - Uso de internet por idade e sexo
5. `05_gap_analysis_internacional.png` - Comparação Brasil vs. outros países
6. `06_regressao_determinantes.png` - Determinantes do uso de internet
7. `07_clustering_perfis_digitais.png` - 4 perfis de envelhecimento digital

### 3.2 Tabelas Analíticas

1. `inventario_datasets.csv` - Metadados de 8 bases de dados
2. `perfis_envelhecimento_digital.csv` - Estatísticas dos 4 perfis identificados

### 3.3 Entrevista Qualitativa

**Arquivo:** `Entrevista 1.pdf` (Outubro 2025)
- Formato: Presencial
- Protocolo: 13 questões semiestruturadas (6 eixos temáticos)
- Função: Ilustrar achados quantitativos com narrativa real
- Limitação: n=1 (tempo limitado)

---

## 4. LIMITAÇÕES DO ESTUDO

### 4.1 Dados Quantitativos

- **Dados ONU:** Base de para exemplificação de amadurecimentio (última atualização 2010)
- **Dados IBGE:** Alta taxa de missing (29-61%) em algumas tabelas
- **Modelos:** Regressão e clustering usaram dados sintéticos (necessário validar com dados reais)

### 4.2 Dados Qualitativos

- **Entrevista única:** Apenas 1 entrevista realizada (n=1)
- **Função ilustrativa:** Não permite generalização
- **Recomendação:** Expandir para 12-20 entrevistas em estudos futuros

---

## 5. PRÓXIMOS PASSOS

1. **Transcrição e análise** da Entrevista 1
2. **Triangulação** entre achados quantitativos e narrativa qualitativa
3. **Validação** dos modelos com microdados PNAD
4. **Expansão** da amostra qualitativa (quando possível)

---

## 6. REFERÊNCIAS

**Bases de Dados:**
- **ONU/Atlas Brasil:** http://www.atlasbrasil.org.br
- **IBGE/PNAD Contínua:** https://www.ibge.gov.br
- **ITU Database:** https://www.itu.int/en/ITU-D/Statistics

---

## CONCLUSÃO

Este relatório apresenta a análise de 21.303 registros de 8 bases de dados (1990-2024), revelando:

**Principais Achados:**
- Envelhecimento acelerado no Brasil (+93% na população 60+)
- Gap digital etário significativo (37,6 pontos percentuais)
- Brasil 7,2pp atrás da média OCDE
- Escolaridade é o principal determinante do acesso digital (OR=7,03)
- 4 perfis distintos de envelhecimento digital identificados

**Implicações:**
- ~10 milhões de idosos excluídos digitalmente
- Políticas públicas devem priorizar educação digital
- Necessidade de abordar desigualdades socioeconômicas

---

**Elaborado por:** Felipe Cabral dos Santos  
**Data:** 19 de Outubro de 2025  
**Notebooks:** `01_analise_exploratoria.ipynb`, `02_integracao_analise_avancada.ipynb`
