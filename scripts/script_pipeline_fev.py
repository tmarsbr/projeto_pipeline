# %% [markdown]
# # Pipeline de Dados - Fusão Clínicas Sanare e Reviver
# 
# Este script contém o pipeline de dados para a fusão das duas clínicas.

# %%
# Importando bibliotecas necessárias
import json
import csv

# %% [markdown]
# # Funções de leitura de dados

# %%
def leitura_json(path_json):
    """
    Lê um arquivo JSON e retorna os dados como uma lista de dicionários.
    
    Args:
    path_json (str): Caminho para o arquivo JSON.
    
    Returns:
    list: Dados do arquivo JSON.
    """
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

def leitura_csv(path_csv):
    """
    Lê um arquivo CSV e retorna os dados como uma lista de dicionários.
    
    Args:
    path_csv (str): Caminho para o arquivo CSV.
    
    Returns:
    list: Dados do arquivo CSV.
    """
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    """
    Lê um arquivo de dados (JSON ou CSV) e retorna os dados como uma lista de dicionários.
    
    Args:
    path (str): Caminho para o arquivo de dados.
    tipo_arquivo (str): Tipo do arquivo ('json' ou 'csv').
    
    Returns:
    list: Dados do arquivo.
    """
    dados = []
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
    return dados

def get_columns(dados):
    """
    Retorna os nomes das colunas dos dados.
    
    Args:
    dados (list): Lista de dicionários contendo os dados.
    
    Returns:
    list: Lista com os nomes das colunas.
    """
    return list(dados[0].keys())

def rename_columns(dados, key_mapping):
    """
    Renomeia as colunas dos dados de acordo com o mapeamento fornecido.
    
    Args:
    dados (list): Lista de dicionários contendo os dados.
    key_mapping (dict): Dicionário de mapeamento das colunas.
    
    Returns:
    list: Lista de dicionários com as colunas renomeadas.
    """
    new_dados_csv = []
    for old_dict in dados:
        dict_temp = {}
        for old_key, value in old_dict.items():
            dict_temp[key_mapping.get(old_key, old_key)] = value
        new_dados_csv.append(dict_temp)
    return new_dados_csv

def size_data(dados):
    """
    Retorna o tamanho dos dados.
    
    Args:
    dados (list): Lista de dicionários contendo os dados.
    
    Returns:
    int: Tamanho dos dados.
    """
    return len(dados)

def join(dadosA, dadosB):
    """
    Junta dois conjuntos de dados em uma única lista.
    
    Args:
    dadosA (list): Primeiro conjunto de dados.
    dadosB (list): Segundo conjunto de dados.
    
    Returns:
    list: Lista combinada dos dois conjuntos de dados.
    """
    combined_list = []
    combined_list.extend(dadosA)
    combined_list.extend(dadosB)
    return combined_list

# %% [markdown]
# # Caminhos dos arquivos de dados

# %%
path_json = '../dados_brutos/dados_empresaA.json'
path_csv = '../dados_brutos/dados_empresaB.csv'

# %% [markdown]
# # Leitura dos dados

# %%
dados_json = leitura_dados(path_json, 'json')
nome_colunas_json = get_columns(dados_json)
tamanho_dados_json = size_data(dados_json)

print(f"Nome colunas dados JSON: {nome_colunas_json}")
print(f"Tamanho dos dados JSON: {tamanho_dados_json}")

dados_csv = leitura_dados(path_csv, 'csv')
nome_colunas_csv = get_columns(dados_csv)
tamanho_dados_csv = size_data(dados_csv)

print(f"Nome colunas dados CSV: {nome_colunas_csv}")
print(f"Tamanho dos dados CSV: {tamanho_dados_csv}")

# %% [markdown]
# # Transformação dos dados

# %%
# Mapeamento das chaves do CSV para os nomes desejados
key_mapping = {
    'Nome do Item': 'Nome do Produto',
    'Classificação do Produto': 'Categoria do Produto',
    'Valor em Reais (R$)': 'Preço do Produto (R$)',
    'Quantidade em Estoque': 'Quantidade de Estoque',
    'Nome da Loja': 'Filial',
    'Data da Venda': 'Data da Venda'
}

# Renomeando as colunas do CSV
dados_csv = rename_columns(dados_csv, key_mapping)
nome_colunas_csv = get_columns(dados_csv)
print(f"Nome colunas dados CSV após renomeação: {nome_colunas_csv}")

# %% [markdown]
# # Unindo os dados

# %%
dados_fusao = join(dados_json, dados_csv)
nomes_colunas_fusao = get_columns(dados_fusao)
tamanho_dados_fusao = size_data(dados_fusao)

print(f"Nome colunas dados fusão: {nomes_colunas_fusao}")
print(f"Tamanho dos dados fusão: {tamanho_dados_fusao}")

# %%
