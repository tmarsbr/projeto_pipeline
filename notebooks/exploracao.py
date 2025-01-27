# %% [markdown]
# # Exploração de Dados - Fusão Clínicas Sanare e Reviver
# 
# Este notebook contém a análise exploratória dos dados das duas clínicas.

# %%

import json
import csv


# %% [markdown]
# # lendo dados 

# %%
# dados json impresa A
path_jason = '../dados_brutos/dados_empresaA.json'

# dados csv impresa B
path_csv = '../dados_brutos/dados_empresaB.csv'


# %% [markdown]
# # tratando json e csv para pipeline

# %%
# trabalhando dados json
with open(path_jason) as f:
    df_json = json.load(f)

df_json

# %%
dados_csv = []
with open(path_csv, 'r') as file:
    spamreader = csv.DictReader(file, delimiter=',')
    for row in spamreader:
        dados_csv.append(row)

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

# Atualizando os nomes das colunas no CSV
new_dados_csv = []

for old_dict in dados_csv:
    dict_temp = {}
    for old_key, value in old_dict.items():
        dict_temp[key_mapping.get(old_key, old_key)] = value
    new_dados_csv.append(dict_temp)

new_dados_csv[0]

# %% [markdown]
# # verificando quantidade de registros

# %%
# Verificando a quantidade de registros em cada conjunto de dados
len(df_json)

# %%
len(new_dados_csv)

# %% [markdown]
# # unindo os dados

# %%
# Combinando os dados das duas empresas
combined_list = []
combined_list.extend(df_json)
combined_list.extend(new_dados_csv)

# Verificando a quantidade total de registros
len(combined_list)

# %%
# Verificando o primeiro registro da lista combinada
combined_list[0]

# %%
# Verificando o último registro da lista combinada
combined_list[-1]

# %% [markdown]
# # criando uma lista de listas

# %%
# Confirmando o nome das colunas
nomes_colunas = list(combined_list[-1].keys())
nomes_colunas

# %%
# Criando a lista de listas
dados_combinados_tabela = [nomes_colunas]

for row in combined_list:
    linha = []
    for coluna in nomes_colunas:
        linha.append(row.get(coluna, 'Indisponivel'))
    dados_combinados_tabela.append(linha)

# Verificando o primeiro registro da lista de listas
dados_combinados_tabela[0]

# %%
# Verificando o primeiro registro de dados
dados_combinados_tabela[1]

# %%
# Verificando o último registro de dados
dados_combinados_tabela[-1]

# %%

print(dados_combinados_tbela)
pe

# %%
