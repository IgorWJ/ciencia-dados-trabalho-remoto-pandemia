"""
Geração de visualizações para o dashboard
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Configurar estilo
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 10

BASE_PATH = Path(__file__).parent.parent
DATA_PATH = BASE_PATH / "data"
VIZ_PATH = BASE_PATH / "visualizations"
VIZ_PATH.mkdir(exist_ok=True)

def load_data():
    """Carrega os dados"""
    df = pd.read_csv(DATA_PATH / "Dataset.csv", encoding='latin-1')
    return df

def plot_produtividade(df):
    """Visualiza distribuição de produtividade"""
    col_prod = [c for c in df.columns if 'Roughly how productive are you' in c][0]
    
    # Criar categorias simplificadas
    produtividade = df[col_prod].value_counts()
    
    # Plotar
    fig, ax = plt.subplots(figsize=(12, 8))
    produtividade.head(10).plot(kind='barh', ax=ax, color='steelblue')
    ax.set_xlabel('Número de Respondentes', fontsize=12)
    ax.set_title('Top 10: Percepção de Produtividade no Trabalho Remoto', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(VIZ_PATH / 'produtividade.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico de produtividade salvo")
    plt.close()

def plot_barreiras(df):
    """Visualiza principais barreiras"""
    cols_barreiras = [col for col in df.columns if "most significant barrier" in col]
    
    barreiras_list = []
    for col in cols_barreiras:
        barreiras_col = df[col].dropna()
        barreiras_list.extend(barreiras_col.tolist())
    
    from collections import Counter
    barreiras_contador = Counter(barreiras_list)
    barreiras_df = pd.DataFrame(
        barreiras_contador.items(),
        columns=['Barreira', 'Frequência']
    ).sort_values('Frequência', ascending=False).head(10)
    
    # Filtrar valores nulos e inválidos
    barreiras_df = barreiras_df[~barreiras_df['Barreira'].isin(['NA', '8', 'No', ''])]
    
    fig, ax = plt.subplots(figsize=(12, 8))
    barreiras_df.sort_values('Frequência').plot(
        kind='barh', 
        y='Frequência', 
        ax=ax, 
        color='coral',
        legend=False
    )
    ax.set_xlabel('Número de Menções', fontsize=12)
    ax.set_ylabel('Barreira', fontsize=12)
    ax.set_title('Top 10: Principais Barreiras ao Trabalho Remoto', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(VIZ_PATH / 'barreiras.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico de barreiras salvo")
    plt.close()

def plot_aspectos_positivos(df):
    """Visualiza melhores aspectos do trabalho remoto"""
    cols_melhores = [col for col in df.columns if "best aspect of remote working" in col and "worst" not in col]
    
    aspectos_list = []
    for col in cols_melhores:
        aspectos_col = df[col].dropna()
        aspectos_list.extend(aspectos_col.tolist())
    
    from collections import Counter
    aspectos_contador = Counter(aspectos_list)
    aspectos_df = pd.DataFrame(
        aspectos_contador.items(),
        columns=['Aspecto', 'Frequência']
    ).sort_values('Frequência', ascending=False).head(10)
    
    fig, ax = plt.subplots(figsize=(12, 8))
    aspectos_df.sort_values('Frequência').plot(
        kind='barh', 
        y='Frequência', 
        ax=ax, 
        color='lightgreen',
        legend=False
    )
    ax.set_xlabel('Número de Menções', fontsize=12)
    ax.set_ylabel('Aspecto', fontsize=12)
    ax.set_title('Top 10: Melhores Aspectos do Trabalho Remoto', fontsize=14, fontweight='bold')
    plt.tight_layout()
    plt.savefig(VIZ_PATH / 'aspectos_positivos.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico de aspectos positivos salvo")
    plt.close()

def plot_tempo_remoto(df):
    """Compara tempo real vs preferido de trabalho remoto"""
    col_real = "Thinking about your current job, how much of your time did you spend remote working last year?"
    col_pref = "How much of your time would you have preferred to work remotely last year?"
    
    tempo_real = df[col_real].value_counts().head(8)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    tempo_real.plot(kind='bar', ax=ax, color='skyblue')
    ax.set_xlabel('Tempo de Trabalho Remoto', fontsize=12)
    ax.set_ylabel('Número de Respondentes', fontsize=12)
    ax.set_title('Distribuição: Tempo Real de Trabalho Remoto (Último Ano)', fontsize=14, fontweight='bold')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(VIZ_PATH / 'tempo_remoto.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico de tempo remoto salvo")
    plt.close()

def plot_preferencia_futura(df):
    """Visualiza preferência de trabalho remoto no futuro"""
    col_futuro = "Imagine that COVID-19 is cured or eradicated. Going forward, how much of your time would you prefer to work remotely?"
    
    preferencia = df[col_futuro].value_counts().head(10)
    
    fig, ax = plt.subplots(figsize=(12, 6))
    preferencia.plot(kind='bar', ax=ax, color='mediumpurple')
    ax.set_xlabel('Preferência de Trabalho Remoto', fontsize=12)
    ax.set_ylabel('Número de Respondentes', fontsize=12)
    ax.set_title('Preferência de Trabalho Remoto no Futuro (Pós-Pandemia)', fontsize=14, fontweight='bold')
    ax.tick_params(axis='x', rotation=45)
    plt.tight_layout()
    plt.savefig(VIZ_PATH / 'preferencia_futura.png', dpi=150, bbox_inches='tight')
    print("✓ Gráfico de preferência futura salvo")
    plt.close()

def main():
    """Função principal"""
    print("="*80)
    print("GERANDO VISUALIZAÇÕES")
    print("="*80)
    
    df = load_data()
    
    plot_produtividade(df)
    plot_barreiras(df)
    plot_aspectos_positivos(df)
    plot_tempo_remoto(df)
    plot_preferencia_futura(df)
    
    print("\n" + "="*80)
    print("TODAS AS VISUALIZAÇÕES GERADAS COM SUCESSO")
    print(f"Salvas em: {VIZ_PATH}")
    print("="*80)

if __name__ == "__main__":
    main()
