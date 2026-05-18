"""
Dashboard Streamlit - Análise de Trabalho Remoto na Pandemia
Versão 3: Dados totalmente traduzidos e visualizações enriquecidas
"""
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns
from pathlib import Path
from collections import Counter

# Configuração do matplotlib para suportar português
plt.rcParams['font.sans-serif'] = ['DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False

# Configurações Streamlit
st.set_page_config(
    page_title="Análise de Trabalho Remoto", 
    layout="wide",
    initial_sidebar_state="expanded"
)

# Estilo customizado
sns.set_theme(style="whitegrid", palette="husl")

# ============================================================================
# FUNÇÃO AUXILIAR 
# ============================================================================
def get_coluna(df, texto, excluir=None):
    if excluir is None:
        excluir = []

    for c in df.columns:
        if texto in c and not any(x in c for x in excluir):
            return c

    raise ValueError(f"Coluna não encontrada para: {texto}")

# ============================================================================
# CARREGAMENTO DE DADOS
# ============================================================================

BASE_PATH = Path(__file__).parent.parent
DATA_PATH = BASE_PATH / "data"

@st.cache_data
def load_data():
    """Carrega dataset traduzido"""
    df = pd.read_csv(DATA_PATH / "Dataset_PT.csv", encoding='utf-8')
    return df

# Carregar dados
df = load_data()

# Filtros Globais

st.sidebar.markdown("## 🎛️ Filtros Globais")

filtro_linhas = st.sidebar.slider(
    "Quantidade máxima de registros",
    min_value=500,
    max_value=len(df),
    value=len(df),
    step=500
)

df = df.head(filtro_linhas)

mostrar_graficos_interativos = st.sidebar.toggle(
    "Ativar gráficos interativos (Plotly)",
    value=True
)

# CSS customizado
st.markdown("""
<style>
h1 { text-align: center; color: #2c3e50; }
h2 { border-bottom: 2px solid #3498db; padding-bottom: 5px; }
.insight-box {
    background: #ecf0f1;
    padding: 15px;
    border-left: 4px solid #3498db;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)
# ============================================================================
# TITULO 
# ============================================================================
st.title("📊 Análise: Trabalho Remoto na Pandemia (2020-2021)")
st.markdown("Versão Traduzida com Contexto Completo | 3.019 Respondentes | 73 Variáveis")
st.markdown("---")

# ============================================================================
# SIDEBAR MENU
# ============================================================================
pagina = st.sidebar.radio(
    "Escolha uma seção:",
    [
        "📈 Resumo Executivo",
        "🧠 Insights Automáticos",
        "👥 Adoção do Trabalho Remoto",
        "💼 Produtividade Percebida",
        "🚧 Principais Barreiras",
        "✨ Benefícios Identificados",
        "🔮 Perspectiva Pós-Pandemia"
    ]
)

# ============================================================================
# PÁGINA 1: RESUMO EXECUTIVO
# ============================================================================
if pagina == "📈 Resumo Executivo":
    st.header("Resumo Executivo da Pesquisa")
    
    st.markdown("""
    ### Contexto da Pesquisa
    
    Durante a pandemia de COVID-19, o trabalho remoto tornou-se realidade para milhões de trabalhadores.
    Esta pesquisa explorou **como o trabalho remoto impactou a produtividade, preferências e bem-estar** 
    de 3.019 profissionais entre 2020 e 2021.
    """)
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("👥 Respondentes", "3.019")
    with col2:
        st.metric("📋 Variáveis", "73")
    with col3:
        st.metric("🌍 Regiões", "Metropolitana + Regional")
    with col4:
        st.metric("📅 Período", "2020-2021")
    
    st.markdown("---")
    
    st.subheader("🎯 Principais Descobertas")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        #### 1️⃣ Produtividade
        - **34%** percebem produtividade **positiva** trabalhando remotamente
        - **34%** relatam produtividade **igual** ao presencial
        - **32%** percebem produtividade **reduzida**
        
        #### 2️⃣ Principal Desafio
        - **Falta de motivação** é citada 2.211 vezes
        - Seguida por dificuldade em colaborar (1.763)
        - E sentimento de isolamento (1.561)
        """)
    
    with col2:
        st.markdown("""
        #### 3️⃣ Maior Benefício
        - **Equilíbrio vida-trabalho** é citado 1.829 vezes
        - Economia de tempo com deslocamento (1.485)
        - Melhor gestão de compromissos pessoais (1.082)
        
        #### 4️⃣ Futuro do Trabalho
        - **36%** querem continuar trabalhando remotamente
        - Indica mudança estrutural e duradoura
        - Demanda por modelos híbridos crescente
        """)
    
    st.markdown("---")
    
    st.subheader("📊 Lacuna Entre Realidade e Preferência")
    
    # Calcular essa métrica
    col_real = [c for c in df.columns if 'Thinking about your current job' in c and '2020' not in c][0]
    col_pref = [c for c in df.columns if 'How much of your time would you have preferred' in c and 'last 3' not in c][0]
    
    dados_real = df[col_real].value_counts()
    dados_pref = df[col_pref].value_counts()
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("🔵 **Tempo REAL Predominante**: 20% do tempo trabalhado remotamente")
    with col2:
        st.warning("🟢 **Tempo PREFERIDO Predominante**: 50% do tempo remoto")
    with col3:
        st.error("⚠️ **Lacuna**: 30% de diferença entre realidade e preferência")
    
    st.markdown("""
    <div class="insight-box">
    💡 **Insight Crítico**: Há uma demanda reprimida significativa - os trabalhadores gostariam de trabalhar 
    muito mais remotamente do que efetivamente trabalham. Isso sugere oportunidade para empresas adotarem 
    modelos mais flexíveis pós-pandemia.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PÁGINA 2: ADOÇÃO DO TRABALHO REMOTO
# ============================================================================
elif pagina == "👥 Adoção do Trabalho Remoto":
    st.header("Adoção do Trabalho Remoto na Prática")
    
    st.markdown("""
    ### Análise Descritiva
    
    Comparação entre o tempo que os trabalhadores **efetivamente trabalhavam remotamente** 
    durante a pandemia versus o tempo que **gostariam de trabalhar remotamente**.
    """)
    
    col_real = [c for c in df.columns if 'Thinking about your current job' in c and '2020' not in c][0]
    col_pref = [c for c in df.columns if 'How much of your time would you have preferred' in c and 'last 3' not in c][0]
    
    tempo_real = df[col_real].value_counts()
    tempo_pref = df[col_pref].value_counts()
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Respondentes com Dados Reais", f"{len(tempo_real.dropna()):,}")
    with col2:
        st.metric("Respondentes com Preferência Definida", f"{len(tempo_pref.dropna()):,}")
    
    st.markdown("---")
    
    # Gráfico 1: Tempo real
    st.subheader("⏱️ Tempo Real de Trabalho Remoto")
    st.markdown("_Percentual do tempo que os trabalhadores efetivamente trabalharam remotamente durante 2020-2021_")
    
    fig, ax = plt.subplots(figsize=(14, 8))
    cores_real = sns.color_palette("Blues_d", len(tempo_real.head(10)))
    tempo_real_plot = tempo_real.head(10).sort_values()
    tempo_real_plot.plot(kind='barh', ax=ax, color=cores_real)
    ax.set_xlabel('Número de Respondentes', fontweight='bold', fontsize=11)
    ax.set_ylabel('Percentual de Tempo Remoto', fontweight='bold', fontsize=11)
    ax.set_title('Top 10: Distribuição de Tempo Real Trabalhado Remotamente', 
                 fontweight='bold', fontsize=12, pad=20)
    
    # Adicionar valores nas barras
    for i, v in enumerate(tempo_real_plot):
        ax.text(v + 10, i, str(v), va='center', fontweight='bold')
    
    sns.despine(left=True)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Insight 1
    principal_real = tempo_real.index[0]
    st.markdown(f"""
    📌 **Resultado Principal**: A maioria dos trabalhadores (**{tempo_real.iloc[0]} respondentes**) 
    trabalhava **{principal_real}** remotamente, indicando adoção parcial durante a pandemia.
    """)
    
    st.markdown("---")
    
    # Gráfico 2: Tempo preferido
    st.subheader("💚 Tempo Preferido de Trabalho Remoto")
    st.markdown("_Quanto tempo os trabalhadores gostariam de trabalhar remotamente_")
    
    fig, ax = plt.subplots(figsize=(14, 8))
    cores_pref = sns.color_palette("Greens_d", len(tempo_pref.head(10)))
    tempo_pref_plot = tempo_pref.head(10).sort_values()
    tempo_pref_plot.plot(kind='barh', ax=ax, color=cores_pref)
    ax.set_xlabel('Número de Respondentes', fontweight='bold', fontsize=11)
    ax.set_ylabel('Tempo Preferido', fontweight='bold', fontsize=11)
    ax.set_title('Top 10: Preferência de Tempo de Trabalho Remoto', 
                 fontweight='bold', fontsize=12, pad=20)
    
    # Adicionar valores
    for i, v in enumerate(tempo_pref_plot):
        ax.text(v + 10, i, str(v), va='center', fontweight='bold')
    
    sns.despine(left=True)
    plt.tight_layout()
    st.pyplot(fig)
    
    principal_pref = tempo_pref.index[0]
    st.markdown(f"""
    📌 **Resultado Principal**: A preferência mais comum é **{principal_pref}** 
    (**{tempo_pref.iloc[0]} respondentes**), indicando forte demanda por trabalho mais flexível.
    """)

# ============================================================================
# PÁGINA 3: PRODUTIVIDADE
# ============================================================================
elif pagina == "💼 Produtividade Percebida":
    st.header("Percepção de Produtividade no Trabalho Remoto")
    
    st.markdown("""
    ### Autopercepção dos Trabalhadores
    
    Os trabalhadores foram perguntados: **"Quão produtivo você é ao trabalhar remotamente 
    em comparação com o trabalho presencial?"**
    """)
    
    col_prod = [c for c in df.columns if 'Roughly how productive are you' in c][0]
    produtividade = df[col_prod].value_counts()
    total_prod = produtividade.sum()
    
    # Categorizar
    positivos = produtividade[produtividade.index.str.contains('Positiva|mais produtivo', case=False, na=False)].sum()
    negativos = produtividade[produtividade.index.str.contains('Negativa|menos produtivo', case=False, na=False)].sum()
    neutros = total_prod - positivos - negativos
    
    # Cards com métricas
    col1, col2, col3 = st.columns(3)
    with col1:
        pct_pos = (positivos / total_prod * 100)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #27ae60 0%, #1e8449 100%); color: white; 
        padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3>✅ Produtividade Positiva</h3>
            <h2>{pct_pos:.1f}%</h2>
            <p><strong>{int(positivos):,}</strong> respondentes relataram maior produtividade</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        pct_neu = (neutros / total_prod * 100)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f39c12 0%, #d68910 100%); color: white; 
        padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3>➖ Produtividade Neutra</h3>
            <h2>{pct_neu:.1f}%</h2>
            <p><strong>{int(neutros):,}</strong> respondentes reportaram produtividade igual</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        pct_neg = (negativos / total_prod * 100)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #e74c3c 0%, #c0392b 100%); color: white; 
        padding: 20px; border-radius: 10px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.1);">
            <h3>❌ Produtividade Reduzida</h3>
            <h2>{pct_neg:.1f}%</h2>
            <p><strong>{int(negativos):,}</strong> respondentes sentiram menos produtivos</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    st.subheader("📊 Distribuição Detalhada de Respostas")
    
    fig, ax = plt.subplots(figsize=(15, 9))
    top_prod = produtividade.head(12)
    
    # Cores baseadas no tipo de resposta
    cores = []
    for cat in top_prod.index:
        if 'Positiva' in cat or 'mais produtivo' in cat.lower():
            cores.append('#27ae60')
        elif 'Negativa' in cat or 'menos produtivo' in cat.lower():
            cores.append('#e74c3c')
        else:
            cores.append('#f39c12')
    
    top_prod_sorted = top_prod.sort_values()
    top_prod_sorted.plot(kind='barh', ax=ax, color=cores)
    ax.set_xlabel('Número de Respondentes', fontweight='bold', fontsize=11)
    ax.set_ylabel('')
    ax.set_title('Percepção de Produtividade - Top 12 Respostas\n(Verde=Positiva, Laranja=Neutra, Vermelho=Reduzida)', 
                 fontweight='bold', fontsize=12, pad=20)
    
    # Adicionar valores
    for i, v in enumerate(top_prod_sorted):
        ax.text(v + 20, i, str(v), va='center', fontweight='bold', fontsize=10)
    
    sns.despine(left=True)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("""
    <div class="insight-box">
    💡 **Insight**: A resposta mais comum foi "Produtividade Positiva" (582 pessoas), seguida por 
    "Produtividade Neutra" (437 pessoas). Isso sugere que, no geral, o trabalho remoto **não prejudicou** 
    e em alguns casos **melhorou** a produtividade percebida.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PÁGINA 4: BARREIRAS
# ============================================================================
elif pagina == "🚧 Principais Barreiras":

    st.header("Principais Barreiras")

    cols = [c for c in df.columns if "barrier" in c]

    lista = []
    for c in cols:
        lista.extend(df[c].dropna().tolist())

    df_bar = pd.DataFrame(Counter(lista).items(), columns=["Barreira", "Frequência"])
    df_bar = df_bar.sort_values("Frequência", ascending=False)

    n = st.slider("Quantas barreiras?", 5, 15, 10)

    top = df_bar.head(n)

    # ================================
    # PLOTLY TOGGLE
    # ================================
    if mostrar_graficos_interativos:

        fig = px.bar(
            top,
            x="Frequência",
            y="Barreira",
            orientation="h",
            text="Frequência",
            color="Frequência",
            title="Principais Barreiras"
        )

        st.plotly_chart(fig, use_container_width=True)

    else:

        fig, ax = plt.subplots()
        top.sort_values("Frequência").plot(
            kind="barh",
            x="Barreira",
            y="Frequência",
            ax=ax
        )

        st.pyplot(fig)

# ============================================================================
# PÁGINA 5: BENEFÍCIOS
# ============================================================================
elif pagina == "✨ Benefícios Identificados":
    st.header("Benefícios do Trabalho Remoto")
    
    st.markdown("""
    ### Aspectos Positivos Percebidos
    
    Os respondentes foram perguntados: **"Qual é o melhor aspecto do trabalho remoto para você?"**
    """)
    
    cols_melhores = [col for col in df.columns if "best aspect of remote working" in col and "worst" not in col]
    
    aspectos_list = []
    for col in cols_melhores:
        aspectos_col = df[col].dropna()
        aspectos_list.extend(aspectos_col.tolist())
    
    aspectos_contador = Counter(aspectos_list)
    aspectos_df = pd.DataFrame(
        aspectos_contador.items(),
        columns=['Benefício', 'Frequência']
    ).sort_values('Frequência', ascending=False)
    
    st.metric("Total de Menções de Benefícios", f"{len(aspectos_list):,}")
    
    st.markdown("---")
    
    # Slider
    n_beneficios = st.slider("Quantos benefícios exibir?", 5, 15, 10, step=1)
    
    st.subheader(f"🟢 Top {n_beneficios} Benefícios Mais Mencionados")
    
    fig, ax = plt.subplots(figsize=(15, 10))
    aspectos_top = aspectos_df.head(n_beneficios).sort_values('Frequência')
    cores_ben = sns.color_palette("Greens_r", len(aspectos_top))
    aspectos_top.plot(
        kind='barh', 
        y='Frequência', 
        ax=ax, 
        color=cores_ben,
        legend=False
    )
    ax.set_xlabel('Número de Menções', fontweight='bold', fontsize=11)
    ax.set_ylabel('')
    ax.set_title(f'Principais Benefícios do Trabalho Remoto - Top {n_beneficios}\n(Quanto maior, mais valorizado o benefício)', 
                 fontweight='bold', fontsize=12, pad=20)
    
    # Adicionar valores
    for i, v in enumerate(aspectos_top['Frequência']):
        ax.text(v + 50, i, str(int(v)), va='center', fontweight='bold', fontsize=10)
    
    sns.despine(left=True)
    plt.tight_layout()
    st.pyplot(fig)
    
    # Top 5 com destaque
    st.markdown("---")
    st.subheader("⭐ Top 5 Benefícios Mais Valorados")
    
    for idx, row in aspectos_df.head(5).iterrows():
        pct = (row['Frequência'] / aspectos_df['Frequência'].max()) * 100
        col1, col2 = st.columns([3, 1])
        with col1:
            st.progress(pct / 100)
            st.write(f"**{idx + 1}. {row['Benefício']}**")
        with col2:
            st.write(f"**{int(row['Frequência'])}** menções")
    
    st.markdown("""
    <div class="insight-box">
    💡 **Insight**: "Equilíbrio Vida-Trabalho" é o benefício mais valorado (1.829 menções), 
    superando significativamente economia de tempo e dinheiro. Isso revela que os trabalhadores 
    priorizam qualidade de vida sobre ganhos materiais.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# PÁGINA 6: FUTURO
# ============================================================================
elif pagina == "🔮 Perspectiva Pós-Pandemia":
    st.header("Preferências para o Futuro (Após COVID-19)")
    
    st.markdown("""
    ### Visão dos Trabalhadores
    
    Pergunta: **"Se o COVID-19 for controlado, quanto tempo você gostaria de trabalhar remotamente?"**
    
    Esta resposta indica tendências estruturais no futuro do trabalho.
    """)
    
    col_futuro = "Imagine that COVID-19 is cured or eradicated. Going forward, how much of your time would you prefer to work remotely?"
    # Encontrar coluna exata
    col_futuro = [c for c in df.columns if 'Imagine that COVID-19' in c and 'Going forward' in c][0]
    
    preferencia = df[col_futuro].value_counts()
    total_futuro = preferencia.sum()
    
    st.metric("Respondentes com Preferência Definida", f"{int(total_futuro):,}")
    
    st.markdown("---")
    
    st.subheader("📊 Distribuição de Preferências para o Futuro")
    
    fig, ax = plt.subplots(figsize=(16, 9))
    pref_top = preferencia.head(12)
    
    cores_fut = sns.color_palette("RdYlGn", len(pref_top))
    pref_plot = pref_top.sort_values()
    pref_plot.plot(kind='barh', ax=ax, color=cores_fut)
    
    ax.set_xlabel('Número de Respondentes', fontweight='bold', fontsize=11)
    ax.set_ylabel('')
    ax.set_title('Preferência de Trabalho Remoto Pós-Pandemia - Top 12 Respostas\n(Verde=Mais remoto, Vermelho=Menos remoto)', 
                 fontweight='bold', fontsize=12, pad=20)
    
    # Adicionar valores
    for i, v in enumerate(pref_plot):
        ax.text(v + 30, i, str(int(v)), va='center', fontweight='bold', fontsize=10)
    
    sns.despine(left=True)
    plt.tight_layout()
    st.pyplot(fig)
    
    st.markdown("---")
    
    # Análise de preferência
    st.subheader("🎯 Análise de Preferências")
    
    # Classificar respostas
    remoto_alto = preferencia[preferencia.index.str.contains('100%|90%|80%|70%|60%|Muito|todo', case=False, na=False)].sum()
    remoto_medio = preferencia[preferencia.index.str.contains('50%|Metade|Cerca', case=False, na=False)].sum()
    presencial = preferencia[preferencia.index.str.contains('10%|20%|30%|40%|Raramente|Não', case=False, na=False)].sum()
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        pct_alto = (remoto_alto / total_futuro * 100)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #27ae60 0%, #1e8449 100%); color: white; 
        padding: 20px; border-radius: 10px; text-align: center;">
            <h3>🏠 Muito Remoto</h3>
            <h2>{pct_alto:.1f}%</h2>
            <p>Trabalhar mais de 50% remotamente</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        pct_medio = (remoto_medio / total_futuro * 100)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f39c12 0%, #d68910 100%); color: white; 
        padding: 20px; border-radius: 10px; text-align: center;">
            <h3>🔄 Híbrido</h3>
            <h2>{pct_medio:.1f}%</h2>
            <p>Cerca de 50% remoto e presencial</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        pct_pres = (presencial / total_futuro * 100)
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #3498db 0%, #2980b9 100%); color: white; 
        padding: 20px; border-radius: 10px; text-align: center;">
            <h3>🏢 Presencial</h3>
            <h2>{pct_pres:.1f}%</h2>
            <p>Menos de 50% remoto</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="insight-box">
    💡 **Insight Estratégico**: A maioria dos trabalhadores deseja continuar com trabalho remoto 
    ou híbrido após a pandemia. Isso indica que organizações que não adotarem modelos flexíveis 
    podem enfrentar desafios de retenção de talentos. A demanda por trabalho remoto é uma 
    **tendência estrutural**, não uma preferência temporária.
    </div>
    """, unsafe_allow_html=True)

# ============================================================================
# RODAPÉ
# ============================================================================
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #7f8c8d; padding: 20px; background: #f5f5f5; border-radius: 10px;'>
    <p style='font-size: 12px; margin: 5px;'>
        <strong>Dashboard Interativo de Análise</strong> | 
        Desenvolvido com Streamlit, Pandas, Matplotlib e Seaborn
    </p>
    <p style='font-size: 11px; margin: 5px;'>
        Dados Originais: Trabalho Remoto na Pandemia (2020-2021) | 
        Versão Traduzida e Contextualizada | 
        Projeto Acadêmico de Ciência de Dados
    </p>
    <p style='font-size': 11px;' margin: 5px;'>
        📊 3.019 Respondentes | 73 Variáveis | Dataset Totalmente Traduzido para Português
    </p>
</div>
""", unsafe_allow_html=True)
