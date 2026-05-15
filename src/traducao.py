"""
Script de tradução do dataset de Inglês para Português
Cria um dataset traduzido para melhor compreensão
"""
import pandas as pd
from pathlib import Path

BASE_PATH = Path(__file__).parent.parent
DATA_PATH = BASE_PATH / "data"

def traduzir_dataset():
    """Carrega dataset e traduz todos os valores para português"""
    
    # Dicionário de traduções de valores comuns
    traducoes = {
        # Gênero
        'Male': 'Masculino',
        'Female': 'Feminino',
        'Non-binary': 'Não-binário',
        'Prefer to self-describe': 'Prefiro descrever-me',
        
        # Tempo de trabalho remoto
        '100% - All of my time': '100% - Todo o meu tempo',
        '90%': '90%',
        '80%': '80%',
        '70%': '70%',
        '60%': '60%',
        '50% - About half of my time': '50% - Cerca de metade do meu tempo',
        '50% - I spent about half of my time remote working': '50% - Passei cerca de metade do meu tempo trabalhando remotamente',
        '40%': '40%',
        '30%': '30%',
        '20%': '20%',
        '10%': '10%',
        'Less than 10% of my time': 'Menos de 10% do meu tempo',
        'Rarely or never': 'Raramente ou nunca',
        'I would not have preferred to work remotely': 'Eu não teria preferido trabalhar remotamente',
        'I would prefer not to work remotely': 'Eu preferiria não trabalhar remotamente',
        
        # Acordos e discordâncias
        'Strongly agree': 'Concordo totalmente',
        'Somewhat agree': 'Concordo em parte',
        'Neither agree nor disagree': 'Nem concordo nem discordo',
        'Somewhat disagree': 'Discordo em parte',
        'Strongly disagree': 'Discordo totalmente',
        'NA': 'Não aplicável',
        
        # Produtividade
        'Strongly Positive': 'Muito Positiva',
        'Somewhat Positive': 'Positiva',
        'Neither positive nor negative': 'Neutra',
        'Somewhat Negative': 'Negativa',
        'Strongly Negative': 'Muito Negativa',
        'My productivity is about same when I work remotely': 'Minha produtividade é aproximadamente a mesma quando trabalho remotamente',
        'Im 50% more productive when working remotely (or more)': 'Sou 50% mais produtivo quando trabalho remotamente (ou mais)',
        'Im 40% more productive when working remotely': 'Sou 40% mais produtivo quando trabalho remotamente',
        'Im 30% more productive when working remotely': 'Sou 30% mais produtivo quando trabalho remotamente',
        'Im 20% more productive when working remotely': 'Sou 20% mais produtivo quando trabalho remotamente',
        'Im 10% more productive when working remotely': 'Sou 10% mais produtivo quando trabalho remotamente',
        'Im 10% less productive when working remotely': 'Sou 10% menos produtivo quando trabalho remotamente',
        'Im 20% less productive when working remotely': 'Sou 20% menos produtivo quando trabalho remotamente',
        'Im 30% less productive when working remotely': 'Sou 30% menos produtivo quando trabalho remotamente',
        'Im 40% less productive when working remotely': 'Sou 40% menos produtivo quando trabalho remotamente',
        'Im 50% less productive when working remotely (or less)': 'Sou 50% menos produtivo quando trabalho remotamente (ou menos)',
        
        # Barreiras
        'Connectivity (internet connection)': 'Conectividade (conexão à internet)',
        'Feeling left out and/or isolated': 'Sentimento de exclusão e/ou isolamento',
        'Poor management': 'Gestão inadequada',
        'IT equipment (computer, printer, etc.)': 'Equipamento de TI (computador, impressora, etc.)',
        'Difficulty collaborating remotely': 'Dificuldade em colaborar remotamente',
        'Caring responsibilities': 'Responsabilidades de cuidado',
        'Cyber security': 'Segurança cibernética',
        'Lack of motivation': 'Falta de motivação',
        'My organisation\'s software and systems': 'Software e sistemas da minha organização',
        'My workspace (e.g. suitable chair, lighting, noise levels, facilities)': 'Meu espaço de trabalho (ex. cadeira adequada, iluminação, níveis de ruído, instalações)',
        'I have tasks that can\'t be done remotely': 'Tenho tarefas que não podem ser feitas remotamente',
        'Lack of remote working skills': 'Falta de habilidades de trabalho remoto',
        'My living situation (e.g. location, home size, who I live with)': 'Minha situação de vida (ex. localização, tamanho da casa, com quem vivo)',
        'Management discourages remote working': 'A gestão desencoraja o trabalho remoto',
        
        # Aspectos positivos
        'My work-life balance': 'Meu equilíbrio vida-trabalho',
        'Preparing for work and commuting': 'Preparação para o trabalho e deslocamento',
        'Managing my family responsibilities': 'Gestão de minhas responsabilidades familiares',
        'Managing my personal commitments': 'Gestão de meus compromissos pessoais',
        'My opportunities to socialise': 'Minhas oportunidades de socializar',
        'My mental wellbeing': 'Meu bem-estar mental',
        'My on-the-job learning opportunities': 'Minhas oportunidades de aprendizado no trabalho',
        'My daily expenses': 'Minhas despesas diárias',
        'My personal relationships': 'Meus relacionamentos pessoais',
        'My working relationships': 'Meus relacionamentos de trabalho',
        'My job satisfaction': 'Minha satisfação no trabalho',
        'The number of hours  I work': 'O número de horas que trabalho',
        
        # Tamanho da empresa
        'Between 1 and 4': 'Entre 1 e 4',
        'Between 5 and 19': 'Entre 5 e 19',
        'Between 20 and 199': 'Entre 20 e 199',
        'Between 200 and 999': 'Entre 200 e 999',
        'Between 1000 and 4999': 'Entre 1.000 e 4.999',
        'More than 5000': 'Mais de 5.000',
        
        # Localização
        'Metro': 'Metropolitana',
        'Regional': 'Regional',
        
        # Tipo de moradia
        'Couple with no dependent children': 'Casal sem filhos dependentes',
        'Couple with dependent children': 'Casal com filhos dependentes',
        'Single with dependent children': 'Solteiro com filhos dependentes',
        'Single with no dependent children': 'Solteiro sem filhos dependentes',
        'Extended family': 'Família extensa',
        'Shared living': 'Moradia compartilhada',
        
        # Gestão de pessoas
        'Yes': 'Sim',
        'No': 'Não',
    }
    
    # Carregar dataset
    df = pd.read_csv(DATA_PATH / "Dataset.csv", encoding='latin-1')
    
    print("=" * 80)
    print("🌐 TRADUZINDO DATASET PARA PORTUGUÊS")
    print("=" * 80)
    print(f"\n📊 Dimensões originais: {df.shape[0]} linhas e {df.shape[1]} colunas")
    
    # Aplicar traduções
    df_traduzido = df.copy()
    
    total_substituicoes = 0
    for coluna in df_traduzido.columns:
        for valor_en, valor_pt in traducoes.items():
            mask = df_traduzido[coluna] == valor_en
            if mask.any():
                quantidade = mask.sum()
                df_traduzido.loc[mask, coluna] = valor_pt
                total_substituicoes += quantidade
    
    print(f"\n✅ Total de valores traduzidos: {total_substituicoes:,}")
    
    # Salvar dataset traduzido
    caminho_traduzido = DATA_PATH / "Dataset_PT.csv"
    df_traduzido.to_csv(caminho_traduzido, encoding='utf-8', index=False)
    print(f"\n💾 Dataset traduzido salvo em: {caminho_traduzido}")
    
    print("\n" + "=" * 80)
    print("✅ TRADUÇÃO CONCLUÍDA COM SUCESSO")
    print("=" * 80)
    
    return df_traduzido

if __name__ == "__main__":
    df = traduzir_dataset()
    print(f"\n🎯 Dataset pronto para uso em português!")
