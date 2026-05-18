"""
Dashboard Streamlit - Análise de Trabalho Remoto na Pandemia
Versão 3: Dados totalmente traduzidos e visualizações enriquecidas
"""
import streamlit as st
import pandas as pd
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

# FUNÇÃO AUXILIAR 

def get_coluna(df, texto, excluir=None):
    if excluir is None:
        excluir = []

    for c in df.columns:
        if texto in c and not any(x in c for x in excluir):
            return c

    st.error(f"Coluna não encontrada: {texto}")
    st.stop()

# CARREGAMENTO DE DADOS

BASE_PATH = Path(__file__).parent.parent
DATA_PATH = BASE_PATH / "data"

@st.cache_data
def load_data():
    """Carrega dataset traduzido"""
    df = pd.read_csv(
        DATA_PATH / "Dataset_PT.csv",
        encoding="utf-8"
    )
    return df


# Carregar dados
df = load_data()

st.toast("Dados carregados com sucesso 📊")

# SIDEBAR

st.sidebar.markdown("""
# 📊 Dashboard Analítico
### Trabalho Remoto na Pandemia
""")

st.sidebar.title("Navegação")

st.sidebar.markdown("## Configurações")

amostra = st.sidebar.slider(
    "Quantidade de registros exibidos",
    min_value=500,
    max_value=len(df),
    value=len(df),
    step=500
)

df = df.head(amostra)

mostrar_graficos_interativos = st.sidebar.toggle(
    "Ativar gráficos interativos (Plotly)",
    value=True
)

st.sidebar.markdown("---")

st.sidebar.info(
    """
### Sobre este Projeto

Dashboard analítico desenvolvido em Streamlit para análise dos impactos do trabalho remoto durante a pandemia de COVID-19.

### Tecnologias
- Python
- Streamlit
- Pandas
- Plotly
- Seaborn

### Dataset
- 3.019 respondentes
- 73 variáveis
- Dados coletados entre 2020–2021
"""
)

st.sidebar.markdown("---")

st.sidebar.caption(
    "Projeto acadêmico de Ciência de Dados com foco em análise exploratória, visualização de dados e storytelling analítico."
)

# CSS CUSTOMIZADO

st.markdown("""
<style>

/* Fundo geral */
.main {
    background-color: #0f172a;
}

/* Texto padrão */
html, body, [class*="css"]  {
    color: #f1f5f9;
    font-family: 'Segoe UI', sans-serif;
}

/* HERO */
.hero {
    padding: 2rem;
    border-radius: 20px;
    background: linear-gradient(135deg, #1e293b, #0f172a);
    border: 1px solid #334155;
    margin-bottom: 2rem;
    box-shadow: 0 0 20px rgba(0,0,0,0.3);
}

.hero h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
    color: white;
}

.hero p {
    font-size: 1.1rem;
    color: #cbd5e1;
}

/* Headers */
h2, h3 {
    color: #f8fafc;
    border-bottom: 1px solid #334155;
    padding-bottom: 0.3rem;
}

/* Métricas */
[data-testid="metric-container"] {
    background-color: #1e293b;
    border: 1px solid #334155;
    padding: 1rem;
    border-radius: 16px;
    box-shadow: 0 4px 10px rgba(0,0,0,0.2);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

/* Insight box */
.insight-box {
    background: linear-gradient(135deg, #1e293b, #111827);
    color: #f8fafc;
    padding: 1.5rem;
    border-left: 5px solid #38bdf8;
    border-radius: 14px;
    margin-top: 1rem;
    box-shadow: 0 0 15px rgba(0,0,0,0.25);
}

/* Dataframe */
[data-testid="stDataFrame"] {
    border-radius: 14px;
    overflow: hidden;
}

/* Botões */
.stButton>button {
    border-radius: 12px;
    border: none;
    background-color: #2563eb;
    color: white;
    padding: 0.5rem 1rem;
}

/* Tabs */
.stTabs [data-baseweb="tab"] {
    font-size: 16px;
}

/* Espaçamento */
.block-container {
    padding-top: 2rem;
}

/* Linha horizontal */
hr {
    border-color: #334155;
}

</style>
""", unsafe_allow_html=True)

# TITULO 

st.markdown("""
<div class="hero">

<h1>Trabalho Remoto na Pandemia</h1>

<p>
Análise interativa sobre produtividade, barreiras, benefícios
e perspectivas do home office durante a COVID-19.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown(
    "Versão traduzida com contexto completo | 3.019 Respondentes | 73 Variáveis"
)

st.markdown("---")

# SIDEBAR MENU

pagina = st.sidebar.radio(
    "Escolha uma seção:",
    [
        "Resumo Executivo",
        "Insights Automáticos",
        "Adoção do Trabalho Remoto",
        "Produtividade Percebida",
        "Principais Barreiras",
        "Benefícios Identificados",
        "Perspectiva Pós-Pandemia"
    ]
)

# ============================================================================
# PÁGINA 1: RESUMO EXECUTIVO
# ============================================================================

if pagina == "Resumo Executivo":

    st.header("Resumo Executivo da Pesquisa")

    st.markdown("""
Durante a pandemia de COVID-19, milhões de trabalhadores migraram para o trabalho remoto.
Esta pesquisa analisou como essa mudança impactou produtividade, motivação, bem-estar e preferências futuras.
""")

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("👥 Respondentes", f"{len(df):,}")
    col2.metric("📊 Variáveis", len(df.columns))
    col3.metric("🌎 Escopo", "Global")
    col4.metric("📅 Período", "2020–2021")

    st.markdown("---")

    st.subheader("Principais Descobertas")

    col1, col2 = st.columns(2)

    with col1:

        st.markdown("""
### Produtividade

- Grande parte dos participantes relatou produtividade igual ou superior ao trabalho presencial.
- Muitos profissionais relataram maior foco durante o home office.
- Não houve percepção generalizada de queda de desempenho.

### Barreiras

- Falta de motivação apareceu como principal obstáculo.
- Isolamento social foi recorrente.
- Comunicação e colaboração remota foram desafios relevantes.
""")

    with col2:

        st.markdown("""
### Benefícios

- Equilíbrio entre vida pessoal e profissional foi o benefício mais citado.
- Economia de tempo com deslocamento teve forte destaque.
- Flexibilidade tornou-se prioridade para muitos profissionais.

### Futuro

- Muitos trabalhadores desejam continuar em modelos híbridos.
- O trabalho remoto passou a ser visto como tendência estrutural.
""")

    st.markdown("---")

    st.subheader("Visualização do Dataset")

    st.dataframe(
    df.head(),
    use_container_width=True
)

    st.markdown("""
<div class="insight-box">

<strong>Insight Estratégico:</strong>

Os dados sugerem que empresas que mantiverem modelos flexíveis de trabalho
podem ter vantagens em retenção de talentos, satisfação profissional
e adaptação às novas expectativas do mercado.

</div>
""", unsafe_allow_html=True)

# ============================================================================
# PÁGINA 2 - INSIGHTS AUTOMÁTICOS
# ============================================================================

elif pagina == "Insights Automáticos":

    st.header("Insights Automáticos")

    st.markdown("""
Esta seção reúne descobertas automáticas identificadas a partir da análise dos dados.
""")

    col1, col2 = st.columns(2)

    with col1:
        st.success(
            "Equilíbrio entre vida pessoal e profissional foi o benefício mais citado."
        )

        st.info(
            "Existe forte preferência por modelos híbridos de trabalho."
        )

    with col2:
        st.warning(
            "Falta de motivação apareceu como principal obstáculo ao home office."
        )

        st.success(
            "A produtividade foi percebida como neutra ou positiva pela maioria."
        )

    st.info(
        "Muitos profissionais desejam continuar trabalhando remotamente após a pandemia."
    )

# ============================================================================
# PÁGINA 3: ADOÇÃO DO TRABALHO REMOTO
# ============================================================================

elif pagina == "Adoção do Trabalho Remoto":

    st.header("Adoção do Trabalho Remoto")

    col_real = get_coluna(
        df,
        "Thinking about your current job",
        ["2020"]
    )

    col_pref = get_coluna(
        df,
        "How much of your time would you have preferred",
        ["last 3"]
    )

    real = df[col_real].value_counts().head(10)
    pref = df[col_pref].value_counts().head(10)

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Tempo Real")

        real_df = real.reset_index()
        real_df.columns = ["Categoria", "Quantidade"]

        if mostrar_graficos_interativos:

            fig = px.bar(
                real_df,
                x="Quantidade",
                y="Categoria",
                orientation="h",
                text="Quantidade",
                color="Quantidade",
                title="Tempo Real Trabalhado Remotamente",
                template="plotly_dark"
            )

            fig.update_layout(
                height=600,
                paper_bgcolor="#0f172a",
                plot_bgcolor="#0f172a",
                font_color="white",
                title_font_size=22,
                title_x=0.05,
                coloraxis_showscale=False
            )

            st.plotly_chart(fig, use_container_width=True)

        else:

            st.bar_chart(real)

    with col2:

        st.subheader("Tempo Preferido")

        pref_df = pref.reset_index()
        pref_df.columns = ["Categoria", "Quantidade"]

        if mostrar_graficos_interativos:

            fig = px.bar(
                pref_df,
                x="Quantidade",
                y="Categoria",
                orientation="h",
                text="Quantidade",
                color="Quantidade",
                title="Tempo Preferido de Trabalho Remoto",
                template="plotly_dark"
            )

            fig.update_layout(
                height=600,
                paper_bgcolor="#0f172a",
                plot_bgcolor="#0f172a",
                font_color="white",
                title_font_size=22,
                title_x=0.05,
                coloraxis_showscale=False
            )

            st.plotly_chart(fig, use_container_width=True)

        else:

            st.bar_chart(pref)

    st.markdown("""
<div class="insight-box">

<strong>Insight:</strong>

Os trabalhadores demonstraram preferência por níveis mais altos de trabalho remoto
do que os efetivamente praticados durante a pandemia.

</div>
""", unsafe_allow_html=True)

# ============================================================================
# PÁGINA 4: PRODUTIVIDADE
# ============================================================================

elif pagina == "Produtividade Percebida":

    st.header("Produtividade Percebida")

    col_prod = get_coluna(
        df,
        "Roughly how productive are you"
    )

    prod = df[col_prod].value_counts().head(10)

    prod_df = prod.reset_index()
    prod_df.columns = ["Categoria", "Quantidade"]

    if mostrar_graficos_interativos:

        fig = px.bar(
            prod_df,
            x="Quantidade",
            y="Categoria",
            orientation="h",
            text="Quantidade",
            color="Quantidade",
            title="Percepção de Produtividade",
            template="plotly_dark"
        )

        fig.update_layout(
            height=600,
            paper_bgcolor="#0f172a",
            plot_bgcolor="#0f172a",
            font_color="white",
            title_font_size=22,
            title_x=0.05,
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True)

    else:

        st.bar_chart(prod)

    st.markdown("""
<div class="insight-box">

<strong>Insight:</strong>

A percepção predominante foi de produtividade igual ou superior ao trabalho presencial,
indicando boa adaptação ao modelo remoto.

</div>
""", unsafe_allow_html=True)

# ============================================================================
# PÁGINA 5: BARREIRAS
# ============================================================================

elif pagina == "Principais Barreiras":

    st.header("Principais Barreiras")

    st.markdown("""
Principais obstáculos enfrentados pelos trabalhadores durante o trabalho remoto.
""")

    cols = [c for c in df.columns if "barrier" in c]

    lista = []

    for c in cols:
        lista.extend(df[c].dropna().tolist())

    df_bar = pd.DataFrame(
        Counter(lista).items(),
        columns=["Barreira", "Frequência"]
    )

    df_bar = df_bar.sort_values("Frequência", ascending=False)

    n = st.slider("Quantas barreiras exibir?", 5, 15, 10)

    top = df_bar.head(n)

    if mostrar_graficos_interativos:

        fig = px.bar(
            top,
            x="Frequência",
            y="Barreira",
            orientation="h",
            text="Frequência",
            color="Frequência",
            title="Principais Barreiras ao Trabalho Remoto",
            template="plotly_dark"
        )

        fig.update_layout(
            height=700,
            paper_bgcolor="#0f172a",
            plot_bgcolor="#0f172a",
            font_color="white",
            title_font_size=22,
            title_x=0.05,
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True)

    else:

        fig, ax = plt.subplots(figsize=(12, 8))

        top.sort_values("Frequência").plot(
            kind="barh",
            x="Barreira",
            y="Frequência",
            ax=ax
        )

        st.pyplot(fig)

    st.markdown("""
<div class="insight-box">

<strong>Insight:</strong>

A falta de motivação e o isolamento social apareceram entre os obstáculos mais recorrentes,
mostrando que os desafios do trabalho remoto não são apenas tecnológicos,
mas também emocionais e comportamentais.

</div>
""", unsafe_allow_html=True)
    
# ============================================================================
# PÁGINA 6: BENEFÍCIOS
# ============================================================================

elif pagina == "Benefícios Identificados":

    st.header("Benefícios do Trabalho Remoto")

    st.markdown("""
Aspectos positivos mais valorizados pelos trabalhadores durante a pandemia.
""")

    cols = [c for c in df.columns if "best aspect" in c]

    lista = []

    for c in cols:

        lista.extend(df[c].dropna().tolist())

    df_ben = pd.DataFrame(
        Counter(lista).items(),
        columns=["Benefício", "Frequência"]
    )

    df_ben = df_ben.sort_values(
        "Frequência",
        ascending=False
    )

    top = df_ben.head(10)

    if mostrar_graficos_interativos:

        fig = px.bar(
            top,
            x="Frequência",
            y="Benefício",
            orientation="h",
            text="Frequência",
            color="Frequência",
            title="Benefícios Mais Valorizados",
            template="plotly_dark"
        )

        fig.update_layout(
            height=600,
            paper_bgcolor="#0f172a",
            plot_bgcolor="#0f172a",
            font_color="white",
            title_font_size=22,
            title_x=0.05,
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True)

    else:

        st.bar_chart(top.set_index("Benefício"))

    st.markdown("""
<div class="insight-box">

<strong>Insight:</strong>

O equilíbrio entre vida pessoal e profissional foi o benefício mais valorizado,
superando inclusive fatores financeiros e operacionais.

</div>
""", unsafe_allow_html=True)


# ============================================================================
# PÁGINA 7: FUTURO
# ============================================================================

elif pagina == "Perspectiva Pós-Pandemia":

    st.header("Perspectiva Pós-Pandemia")

    st.markdown("""
Preferências futuras dos trabalhadores após o período crítico da pandemia.
""")

    col = get_coluna(df, "Imagine that COVID")

    pref = df[col].value_counts().head(10)

    pref_df = pref.reset_index()
    pref_df.columns = ["Categoria", "Quantidade"]

    if mostrar_graficos_interativos:

        fig = px.bar(
            pref_df,
            x="Quantidade",
            y="Categoria",
            orientation="h",
            text="Quantidade",
            color="Quantidade",
            title="Preferências Futuras de Trabalho Remoto",
            template="plotly_dark"
        )

        fig.update_layout(
            height=600,
            paper_bgcolor="#0f172a",
            plot_bgcolor="#0f172a",
            font_color="white",
            title_font_size=22,
            title_x=0.05,
            coloraxis_showscale=False
        )

        st.plotly_chart(fig, use_container_width=True)

    else:

        st.bar_chart(pref)

    st.markdown("""
<div class="insight-box">

<strong>Insight Estratégico:</strong>

Os dados indicam forte tendência de continuidade do trabalho remoto e híbrido,
mesmo após o período pandêmico.

Isso sugere mudanças estruturais permanentes no mercado de trabalho.

</div>
""", unsafe_allow_html=True)

# ============================================================================
# RODAPÉ
# ============================================================================

st.markdown("---")

st.markdown("""
<div style='text-align: center; color: gray;'>

Dashboard Interativo de Ciência de Dados<br>
Análise do Trabalho Remoto na Pandemia (2020–2021)<br><br>

Desenvolvido com Streamlit, Pandas, Plotly e Seaborn

</div>
""", unsafe_allow_html=True)
