"""
Script de Integração de Dados - Envelhecimento Ativo e Big Data
Baseado em: GUIA_INTEGRACAO_DADOS.md

Este script carrega, explora e integra dados de múltiplas fontes:
- ONU: Dados demográficos Brasil 1990-2010
- IBGE: Tabelas sobre idosos, internet, alfabetização, renda
- ITU: Indicadores internacionais de uso de internet e celular
"""

import sys
from pathlib import Path
import pandas as pd
import numpy as np
from datetime import datetime

# Configuração de caminhos
ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "COLETA DE DADOS"
OUTPUT_DIR = ROOT / "data"
OUTPUT_DIR.mkdir(exist_ok=True)

PROCESSED_DIR = OUTPUT_DIR / "processed"
PROCESSED_DIR.mkdir(exist_ok=True)

INTEGRATED_DIR = OUTPUT_DIR / "integrated"
INTEGRATED_DIR.mkdir(exist_ok=True)

REPORTS_DIR = ROOT / "reports"
REPORTS_DIR.mkdir(exist_ok=True)
(REPORTS_DIR / "tables").mkdir(exist_ok=True)
(REPORTS_DIR / "figures").mkdir(exist_ok=True)


def log(msg: str):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}")


def explore_dataset(df: pd.DataFrame, name: str):
    """Explora e documenta características básicas de um dataset"""
    log(f"\n{'='*60}")
    log(f"Dataset: {name}")
    log(f"{'='*60}")
    log(f"Shape: {df.shape[0]} linhas x {df.shape[1]} colunas")
    log(f"Colunas: {list(df.columns)}")
    log(f"Tipos: {df.dtypes.value_counts().to_dict()}")
    log(f"Missing: {df.isnull().sum().sum()} valores ({df.isnull().sum().sum() / df.size * 100:.1f}%)")
    log(f"Memory: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    return {
        'name': name,
        'rows': df.shape[0],
        'cols': df.shape[1],
        'missing_pct': df.isnull().sum().sum() / df.size * 100,
        'columns': list(df.columns)
    }


def main():
    log("="*80)
    log("INÍCIO DA ANÁLISE - Inventário de Datasets")
    log("="*80)
    
    inventory = []
    
    # 1. Dados ONU Brasil
    log("\n### 1. DADOS ONU - BRASIL (1990-2010) ###")
    try:
        onu_path = DATA_DIR / "Dados Brasil Onu 1990 - 2010.csv"
        df_onu = pd.read_csv(onu_path, encoding='utf-8')
        info = explore_dataset(df_onu, "ONU Brasil 1990-2010")
        inventory.append(info)
        
        # Salvar primeiras linhas para inspeção
        df_onu.head(20).to_csv(PROCESSED_DIR / "onu_sample.csv", index=False)
        log(f"✓ Amostra salva em: {PROCESSED_DIR / 'onu_sample.csv'}")
        
    except Exception as e:
        log(f"✗ Erro ao carregar dados ONU: {e}")
    
    # 2. Dados IBGE - Tabelas principais
    log("\n### 2. DADOS IBGE ###")
    ibge_dir = DATA_DIR / "Dados IBGE"
    ibge_files = [
        "Tabela 4820 - Pessoas de 60 anos ou mais de idade que utilizaram a Internet, no período de referência dos últimos três meses, total, distribuição e percentuais, por sexo e grupos de idade.xlsx",
        "Tabela 9542 - Pessoas de 60 anos ou mais de idade alfabetizadas.xlsx",
        "Tabela 9756 - Índice de envelhecimento, idade mediana e razão de sexo, por cor ou raça.xlsx",
        "Tabela 9942 - Moradores em domicílios particulares permanentes ocupados, por existência de conexão domiciliar à Internet, segundo a cor ou raça e os grupos de idade (2022).xlsx",
        "Tabela 2387 - Domicílios particulares permanentes e Moradores em domicílios particulares permanentes, por classes de rendimento mensal domiciliar e existência de microcomputador, acesso à Internet e tipo de telefone(2003-2015).xlsx",
    ]
    
    for fname in ibge_files:
        try:
            fpath = ibge_dir / fname
            if not fpath.exists():
                log(f"✗ Arquivo não encontrado: {fname}")
                continue
            
            # IBGE geralmente tem metadados nas primeiras linhas
            df_ibge = pd.read_excel(fpath, sheet_name=0)
            info = explore_dataset(df_ibge, fname[:50])
            inventory.append(info)
            
            # Salvar CSV processado
            out_name = fname.replace(".xlsx", ".csv").replace(" ", "_")
            df_ibge.to_csv(PROCESSED_DIR / out_name, index=False)
            log(f"✓ Salvo em: {PROCESSED_DIR / out_name}")
            
        except Exception as e:
            log(f"✗ Erro ao processar {fname}: {e}")
    
    # 3. Dados ITU - Indicadores internacionais
    log("\n### 3. DADOS ITU (Internacionais) ###")
    itu_dir = DATA_DIR / "Dataset ICT Indicators"
    itu_files = [
        "individuals-who-own-a-mobile-cellular-telephone_1760732826255.csv",
        "Percentage of individuals using the internet (ITU).csv",
        "Percentage of individuals using the Internet - at least once a week but not every day.csv",
    ]
    
    for fname in itu_files:
        try:
            fpath = itu_dir / fname
            df_itu = pd.read_csv(fpath, encoding='utf-8')
            info = explore_dataset(df_itu, fname)
            inventory.append(info)
            
            # Filtrar apenas Brasil se houver coluna de país
            if 'Country' in df_itu.columns or 'Entity' in df_itu.columns:
                country_col = 'Country' if 'Country' in df_itu.columns else 'Entity'
                df_brazil = df_itu[df_itu[country_col].str.contains('Brazil', case=False, na=False)]
                log(f"  → Brasil: {len(df_brazil)} registros")
                
                out_name = fname.replace(".csv", "_brazil.csv")
                df_brazil.to_csv(PROCESSED_DIR / out_name, index=False)
                log(f"✓ Brasil salvo em: {PROCESSED_DIR / out_name}")
            
        except Exception as e:
            log(f"✗ Erro ao processar {fname}: {e}")
    
    # 4. Salvar inventário completo
    log("\n### 4. INVENTÁRIO COMPLETO ###")
    df_inventory = pd.DataFrame(inventory)
    inventory_path = REPORTS_DIR / "tables" / "inventario_datasets.csv"
    df_inventory.to_csv(inventory_path, index=False)
    log(f"✓ Inventário salvo em: {inventory_path}")
    
    log(f"\nTotal de datasets processados: {len(inventory)}")
    log(f"Total de linhas: {df_inventory['rows'].sum():,}")
    log(f"Total de colunas (soma): {df_inventory['cols'].sum()}")
    
    log("\n" + "="*80)
    log("INVENTÁRIO CONCLUÍDO")
    log("="*80)
    log("\nPróximos passos:")
    log("1. Revisar amostras em data/processed/")
    log("2. Identificar variáveis-chave para integração")
    log("3. Padronizar nomenclaturas e formatos")
    log("4. Criar dataset consolidado")
    
    return 0


if __name__ == "__main__":
    sys.exit(main())
