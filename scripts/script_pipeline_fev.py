# %% [markdown]
# # Pipeline de Dados - Fusão Clínicas Sanare e Reviver
# 
# Este script contém o pipeline de dados para a fusão das duas clínicas.

# %%
# Importando bibliotecas necessárias
import json
import csv
from processamento_dados import Dados

# %% [markdown]
# # Caminhos dos arquivos de dados

# %%
path_json = '../dados_brutos/dados_empresaA.json'
path_csv = '../dados_brutos/dados_empresaB.csv'

# %% [markdown]
# # Instanciando a classe Dados

# %%
dados_empresaA = Dados(path_json, 'json')
dados_empresaB = Dados(path_csv, 'csv')

print(dados_empresaA.nome_colunas)
print(dados_empresaB.nome_colunas)
print(dados_empresaA.qtd_linhas)
print(dados_empresaB.qtd_linhas)

# %% [markdown]
# # Funções de transformação e salvamento de dados

# %%
def size_data(dados):
    """
    Retorna o tamanho dos dados.
    
    Args:
    dados (list): Lista de dicionários contendo os dados.
    
    Returns:
    int: Tamanho dos dados.
    """
    return len(dados)

def transformando_dados_tabela(dados, nomes_colunas):
    """
    Transforma os dados em uma lista de listas no formato de tabela.
    
    Args:
    dados (list): Lista de dicionários contendo os dados.
    nomes_colunas (list): Lista com os nomes das colunas.
    
    Returns:
    list: Lista de listas no formato de tabela.
    """
    dados_combinados_tabela = [nomes_colunas]
    for row in dados:
        linha = []
        for coluna in nomes_colunas:
            linha.append(row.get(coluna, 'Indisponivel'))
        dados_combinados_tabela.append(linha)
    return dados_combinados_tabela

def salvando_dados(dados, path):
    """
    Salva os dados em um arquivo CSV.
    
    Args:
    dados (list): Lista de listas no formato de tabela.
    path (str): Caminho para salvar o arquivo CSV.
    """
    with open(path, 'w') as file:
        writer = csv.writer(file)
        writer.writerows(dados)

# %% [markdown]
# # Transformação dos dados

# %%
# Mapeamento das chaves do CSV para os nomes desejados
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade em Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

# Renomeando as colunas do CSV
dados_empresaB.rename_columns(key_mapping)
print(dados_empresaB.nome_colunas)

# %% [markdown]
# # Unindo os dados

# %%
dados_fusao = Dados.join(dados_empresaA, dados_empresaB)
print(dados_fusao.nome_colunas)
print(dados_fusao.qtd_linhas)

# %% [markdown]
# # Salvando os dados

# %%
dados_fusao_tabela = transformando_dados_tabela(dados_fusao.dados, dados_fusao.nome_colunas)

path_dados_combinados = '../dados_processados/dados_combinados.csv'

salvando_dados(dados_fusao_tabela, path_dados_combinados)

print(f"Dados salvos em: {path_dados_combinados}")

# %%

