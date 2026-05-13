"""
Cálculo de métricas para análise de trabalho remoto na pandemia
"""
import pandas as pd
import numpy as np
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent
DATA_PATH = BASE_PATH / "data"

def load_data():
    """Carrega e limpa os dados"""
    df = pd.read_csv(DATA_PATH / "Dataset.csv", encoding='latin-1')
    return df

def calcular_adocao_remoto(df):
    """
    Métrica 1: Adoção do trabalho remoto
    Compara o tempo real de trabalho remoto com o tempo preferido
    """
    col_tempo_real = "Thinking about your current job, how much of your time did you spend remote working last year?"
    col_tempo_pref = "How much of your time would you have preferred to work remotely last year?"
    
    # Criar cópias para análise
    df_adopcao = df[[col_tempo_real, col_tempo_pref]].copy()
    
    # Contar respostas válidas
    total_respostas = len(df_adopcao.dropna(subset=[col_tempo_real]))
    
    # Análise simples - contar frequências
    tempo_real_dist = df[col_tempo_real].value_counts()
    tempo_pref_dist = df[col_tempo_pref].value_counts()
    
    print("\n" + "="*80)
    print("MÉTRICA 1: ADOÇÃO DO TRABALHO REMOTO")
    print("="*80)
    print(f"\n✓ Total de respondentes com dados: {total_respostas}")
    
    print("\n Tempo REAL de trabalho remoto (último ano):")
    print(tempo_real_dist.head(10))
    
    print("\ Tempo PREFERIDO de trabalho remoto (último ano):")
    print(tempo_pref_dist.head(10))
    
    return {
        'tempo_real': tempo_real_dist,
        'tempo_preferido': tempo_pref_dist,
        'total': total_respostas
    }

def calcular_produtividade(df):
    """
    Métrica 2: Percepção de produtividade
    Analisa como os trabalhadores se percebem em termos de produtividade remota
    """
    col_prod = """This question is about your productivity. Productivity means what you produce for each hour that you work. It includes the amount of work you achieve each hour, and the quality of your work each hour.  
Please compare your productivity when you work remotely to when you work at your employer's workplace.  
Roughly how productive are you, each hour, when you work remotely?"""
    
    produtividade = df[col_prod].value_counts()
    total_com_resposta = produtividade.sum()
    
    print("\n" + "="*80)
    print("MÉTRICA 2: PERCEPÇÃO DE PRODUTIVIDADE")
    print("="*80)
    print(f"\n✓ Total de respondentes: {total_com_resposta}")
    print("\nDistribuição de respostas:")
    print(produtividade)
    
    # Calcular percentuais
    print("\nPercentual de cada categoria:")
    percentuais = (produtividade / total_com_resposta * 100).round(2)
    for categoria, perc in percentuais.items():
        print(f"  {categoria}: {perc}%")
    
    return produtividade

def analisar_barreiras(df):
    """
    Métrica 3: Principais barreiras ao trabalho remoto
    Identifica as barreiras mais significativas mencionadas pelos respondentes
    """
    # Colunas que contêm "most significant barrier"
    cols_barreiras_mais = [col for col in df.columns if "most significant barrier" in col]
    
    print("\n" + "="*80)
    print(" MÉTRICA 3: PRINCIPAIS BARREIRAS AO TRABALHO REMOTO")
    print("="*80)
    
    # Consolidar todas as respostas sobre barreiras
    barreiras_list = []
    for col in cols_barreiras_mais:
        barreiras_col = df[col].dropna()
        barreiras_list.extend(barreiras_col.tolist())
    
    # Contar frequência de cada barreira
    from collections import Counter
    barreiras_contador = Counter(barreiras_list)
    barreiras_df = pd.DataFrame(
        barreiras_contador.items(),
        columns=['Barreira', 'Frequência']
    ).sort_values('Frequência', ascending=False)
    
    print(f"\nTotal de menções de barreiras: {len(barreiras_list)}")
    print("\nTop 10 barreiras mais mencionadas:")
    print(barreiras_df.head(10).to_string(index=False))
    
    return barreiras_df

def analisar_aspectos_positivos(df):
    """
    Métrica 4: Melhores aspectos do trabalho remoto
    """
    # Colunas que contêm "best aspect"
    cols_melhores = [col for col in df.columns if "best aspect of remote working" in col and "worst" not in col]
    
    print("\n" + "="*80)
    print("MÉTRICA 4: MELHORES ASPECTOS DO TRABALHO REMOTO")
    print("="*80)
    
    # Consolidar respostas
    aspectos_list = []
    for col in cols_melhores:
        aspectos_col = df[col].dropna()
        aspectos_list.extend(aspectos_col.tolist())
    
    from collections import Counter
    aspectos_contador = Counter(aspectos_list)
    aspectos_df = pd.DataFrame(
        aspectos_contador.items(),
        columns=['Aspecto', 'Frequência']
    ).sort_values('Frequência', ascending=False)
    
    print(f"\n✓ Total de menções: {len(aspectos_list)}")
    print("\nTop 10 melhores aspectos mencionados:")
    print(aspectos_df.head(10).to_string(index=False))
    
    return aspectos_df

def analisar_preferencia_futura(df):
    """
    Métrica 5: Preferência de trabalho remoto no futuro (pós-pandemia)
    """
    col_futuro = "Imagine that COVID-19 is cured or eradicated. Going forward, how much of your time would you prefer to work remotely?"
    
    preferencia_futura = df[col_futuro].value_counts()
    total = preferencia_futura.sum()
    
    print("\n" + "="*80)
    print("MÉTRICA 5: PREFERÊNCIA DE TRABALHO REMOTO NO FUTURO (PÓS-PANDEMIA)")
    print("="*80)
    print(f"\nTotal de respondentes: {total}")
    print("\nDistribuição de preferências:")
    print(preferencia_futura)
    
    print("\nPercentual:")
    for pref, freq in preferencia_futura.items():
        perc = (freq / total * 100)
        print(f"  {pref}: {perc:.1f}%")
    
    return preferencia_futura

def main():
    """Função principal"""
    df = load_data()
    
    # Calcular todas as métricas
    adocao = calcular_adocao_remoto(df)
    produtividade = calcular_produtividade(df)
    barreiras = analisar_barreiras(df)
    aspectos = analisar_aspectos_positivos(df)
    preferencia = analisar_preferencia_futura(df)
    
    print("\n" + "="*80)
    print("MÉTRICAS CALCULADAS COM SUCESSO")
    print("="*80)
    
    return {
        'adocao': adocao,
        'produtividade': produtividade,
        'barreiras': barreiras,
        'aspectos': aspectos,
        'preferencia': preferencia
    }

if __name__ == "__main__":
    metricas = main()
