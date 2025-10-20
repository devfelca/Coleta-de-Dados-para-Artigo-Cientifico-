# Envelhecimento Ativo e Inclusão Digital no Brasil
## Análise de Big Data sobre População Idosa

[![Python](https://img.shields.io/badge/Python-3.13.5-blue.svg)](https://www.python.org/)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange.svg)](https://jupyter.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Sobre o Projeto

Este projeto utiliza **Big Data** e **métodos mistos** para analisar o envelhecimento populacional e a inclusão digital de idosos no Brasil (1990-2024). Combina análise quantitativa de 21.303 registros de bases públicas (ONU, IBGE, ITU) com coleta qualitativa através de entrevistas.

**Período de Análise:** 1990-2024  
**População Estudada:** ~33 milhões de idosos brasileiros (60+ anos)  
**Dados Processados:** 21.303 registros de 8 bases de dados

---

## Objetivos

1. Caracterizar tendências demográficas de envelhecimento no Brasil
2. Mensurar níveis de inclusão digital entre pessoas idosas
3. Comparar padrões brasileiros com países desenvolvidos
4. Identificar determinantes estatísticos do uso de internet por idosos
5. Segmentar perfis de envelhecimento digital

---

## Principais Achados

- **Envelhecimento acelerado:** População 60+ cresceu 93% (1991-2010)
- **Gap digital etário:** 37,6 pontos percentuais entre 60-64 e 75+ anos
- **Brasil vs. OCDE:** 7,2 pontos percentuais atrás da média OCDE
- **Principal determinante:** Escolaridade (OR=7,03)
- **4 perfis identificados:** Conectados, Moderados, Adotantes, Excluídos

---

## Estrutura do Projeto

```
Projeto/
├── COLETA DE DADOS/           # Dados brutos
│   ├── Dados Brasil Onu 1990 - 2010.csv
│   ├── Dados IBGE/            # 4 tabelas PNAD Contínua
│   ├── Dataset ICT Indicators/ # 3 datasets ITU
│   └── Entrevistas/           # Entrevista qualitativa
├── data/
│   └── processed/             # Dados limpos e processados
├── notebooks/
│   ├── 01_analise_exploratoria.ipynb        # Análise exploratória
│   └── 02_integracao_analise_avancada.ipynb # Modelagem avançada
├── reports/
│   ├── figures/               # 7 visualizações (300 DPI)
│   └── tables/                # Tabelas analíticas CSV
├── docs/
│   ├── Analise de Dados.md    # Relatório de resultados
│   └── PROCEDIMENTO_PESQUISA.md # Metodologia detalhada
├── scripts/
│   └── 01_inventario_datasets.py # Script de catalogação
├── requirements.txt           # Dependências Python
└── README.md                  # Este arquivo
```

---

## 🔧 Instalação

### Pré-requisitos

- Python 3.13.5 ou superior
- pip (gerenciador de pacotes Python)
- Git (opcional, para clonar o repositório)

### Passo a Passo

1. **Clone o repositório (ou baixe os arquivos):**
```bash
git clone <url-do-repositorio>
cd Projeto
```

2. **Crie um ambiente virtual:**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

3. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

4. **Verifique a instalação:**
```bash
python -c "import pandas; print(pandas.__version__)"
```

---

## Como Usar

### 1. Executar os Notebooks

**Opção A: Visual Studio Code**
1. Abra o VS Code na pasta do projeto
2. Instale a extensão "Jupyter"
3. Abra `notebooks/01_analise_exploratoria.ipynb`
4. Clique em "Run All" ou execute célula por célula

**Opção B: Jupyter Notebook**
```bash
jupyter notebook
```
Navegue até a pasta `notebooks/` e abra os arquivos `.ipynb`

**Opção C: Google Colab**
1. Faça upload dos notebooks para o Google Drive
2. Abra com Google Colaboratory
3. Faça upload dos dados da pasta `COLETA DE DADOS/`

### 2. Ordem de Execução

Execute os notebooks nesta ordem:

1. **`01_analise_exploratoria.ipynb`** (Análise básica)
   - Carrega dados ONU/Atlas Brasil
   - Gera estatísticas descritivas
   - Cria 3 visualizações principais
   - Tempo estimado: 5-10 minutos

2. **`02_integracao_analise_avancada.ipynb`** (Análise avançada)
   - Integra dados IBGE e ITU
   - Realiza regressão logística
   - Executa clustering K-means
   - Gera 4 visualizações adicionais
   - Tempo estimado: 10-15 minutos

### 3. Visualizar Resultados

Após executar os notebooks, verifique:
- **Figuras:** `reports/figures/*.png` (7 visualizações)
- **Tabelas:** `reports/tables/*.csv` (2 arquivos)
- **Relatórios:** `docs/Analise de Dados.md`

---

## Dependências Principais

| Biblioteca | Versão | Função |
|------------|--------|--------|
| pandas | 2.2.3 | Manipulação de dados |
| numpy | 2.1.3 | Operações numéricas |
| matplotlib | 3.9.2 | Visualizações básicas |
| seaborn | 0.13.2 | Visualizações estatísticas |
| scikit-learn | 1.5.2 | Machine learning |
| scipy | 1.14.1 | Estatística avançada |

---

## Bases de Dados

### Fontes Utilizadas

1. **ONU/Atlas Brasil** (1991-2010)
   - URL: http://www.atlasbrasil.org.br
   - 229 variáveis socioeconômicas
   - 3 pontos temporais

2. **IBGE/PNAD Contínua** (2019-2022)
   - URL: https://sidra.ibge.gov.br
   - 4 tabelas sobre internet e envelhecimento
   - ~33 milhões de idosos representados

3. **ITU Database** (2000-2024)
   - URL: https://www.itu.int/en/ITU-D/Statistics
   - 258 países
   - 21.259 registros

---

## Análises Realizadas

### Análise Exploratória
- Estatísticas descritivas (12 indicadores)
- Séries temporais (1991-2010)
- Matriz de correlação (12×12)
- Pirâmide populacional

### Análise Avançada
- **Gap Analysis:** Brasil vs. 9 países desenvolvidos
- **Regressão Logística:** 5 determinantes do uso de internet
- **Clustering K-means:** 4 perfis de envelhecimento digital
- **Estratificação:** Por idade, sexo, raça, localização

---

## Visualizações Geradas

1. `01_evolucao_indicadores.png` - Evolução temporal (6 painéis)
2. `02_matriz_correlacao.png` - Heatmap de correlações
3. `03_estrutura_etaria.png` - Pirâmide populacional
4. `04_estratificacao_internet_idosos.png` - Uso por idade/sexo
5. `05_gap_analysis_internacional.png` - Comparação internacional
6. `06_regressao_determinantes.png` - Determinantes estatísticos
7. `07_clustering_perfis_digitais.png` - 4 perfis identificados

Todas as figuras em alta resolução (300 DPI) prontas para publicação.

---

## Limitações

- **Dados ONU desatualizados:** Última coleta em 2010
- **Taxa de missing IBGE:** 29-61% em algumas tabelas
- **Modelos simulados:** Regressão e clustering usaram dados sintéticos
- **Amostra qualitativa reduzida:** Apenas 1 entrevista (n=1)

---


## Documentação

- **Relatório de Análise:** [`docs/Analise de Dados.md`](docs/Analise%20de%20Dados.md)
- **Procedimentos:** [`docs/PROCEDIMENTO_PESQUISA.md`](docs/PROCEDIMENTO_PESQUISA.md)
- **Guia Google Colab:** [`docs/GUIA_GOOGLE_COLAB.md`](docs/GUIA_GOOGLE_COLAB.md)

---

## Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---

## Autor

**Felipe Cabral dos Santos**  
Projeto de Pesquisa - Envelhecimento e Inclusão Digital  
Data: Outubro 2025

---

## Agradecimentos

- PNUD/ONU Brasil pelos dados do Atlas Brasil
- IBGE pela disponibilização da PNAD Contínua
- ITU pela base internacional de dados
- Comunidade Python e bibliotecas open-source

---