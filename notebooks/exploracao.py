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
dados_csv


# %%



