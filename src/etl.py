import pandas as pd
import numpy as np
from pathlib import Path

# Definir caminhos
BASE_PATH = Path(__file__).parent.parent
DATA_PATH = BASE_PATH / "data"

def load_data():
    """Carrega o dataset do CSV"""
    df = pd.read_csv(DATA_PATH / "Dataset.csv", encoding='latin-1')
    print(f"Dataset carregado com sucesso!")
    print(f"Dimensões: {df.shape[0]} linhas e {df.shape[1]} colunas\n")
    return df

def explore_data(df):
    """Explora o dataset para entender sua estrutura"""
    print("=" * 80)
    print("EXPLORAÇÃO INICIAL DO DATASET")
    print("=" * 80)
    
    # Primeiras linhas
    print("\n Primeiras linhas do dataset:")
    print(df.head(2))
    
    # Tipos de dados
    print("\n Tipos de dados:")
    print(df.dtypes)
    
    # Valores nulos
    print("\n Valores nulos por coluna (top 20):")
    null_counts = df.isnull().sum()
    print(null_counts[null_counts > 0].sort_values(ascending=False).head(20))
    
    # Estatísticas básicas
    print("\n Estatísticas do dataset:")
    print(f"Total de linhas: {df.shape[0]}")
    print(f"Total de colunas: {df.shape[1]}")
    print(f"Total de células nulas: {df.isnull().sum().sum()}")
    
    return df

def clean_column_names(df):
    """Simplifica nomes de colunas muito longos"""
    # Criar mapeamento de nomes simplificados
    rename_map = {
        "What year were you born?": "ano_nascimento",
        "What is your gender?": "genero",
        "Which of the following best describes your industry?": "industria",
        "Which of the following best describes your current occupation?": "ocupacao",
        "How many people are currently employed by your organisation?": "tamanho_empresa",
        "Do you manage people as part of your current occupation?": "gerencia_pessoas",
        "Which of the following best describes your household?": "tipo_moradia",
        "How long have you been in your current job?": "tempo_no_cargo",
        "Metro / Regional": "localizacao",
        "Thinking about your current job, how much of your time did you spend remote working last year?": "tempo_remoto_ultimo_ano",
        "How much of your time would you have preferred to work remotely last year?": "preferencia_remoto_ultimo_ano",
        "Thinking about your current job, how much of your time did you spend remote working in the last 3 months?": "tempo_remoto_3meses",
        "How much of your time would you have preferred to work remotely in the last 3 months?": "preferencia_remoto_3meses",
        "Imagine that COVID-19 is cured or eradicated. Going forward, how much of your time would you prefer to work remotely?": "preferencia_remoto_futuro",
        "This question is about your productivity. Productivity means what you produce for each hour that you work. It includes the amount of work you achieve each hour, and the quality of your work each hour.  \nPlease compare your productivity when you work remotely to when you work at your employer's workplace.  \nRoughly how productive are you, each hour, when you work remotely?": "produtividade_percebida",
    }
    
    df_clean = df.rename(columns=rename_map)
    return df_clean

def main():
    """Função principal"""
    # Carregar
    df = load_data()
    
    # Explorar
    explore_data(df)
    
    # Limpar nomes
    df_clean = clean_column_names(df)
    
    print("\n" + "=" * 80)
    print(" ETL CONCLUÍDO")
    print("=" * 80)
    
    return df_clean

if __name__ == "__main__":
    df = main()
