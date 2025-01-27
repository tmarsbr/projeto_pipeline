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
def leitura_json(path_json):
    dados_json = []
    with open(path_json, 'r') as file:
        dados_json = json.load(file)
    return dados_json

def leitura_csv(path_csv):
    dados_csv = []
    with open(path_csv, 'r') as file:
        spamreader = csv.DictReader(file, delimiter=',')
        for row in spamreader:
            dados_csv.append(row)
    return dados_csv

def leitura_dados(path, tipo_arquivo):
    dados = []
    if tipo_arquivo == 'csv':
        dados = leitura_csv(path)
    elif tipo_arquivo == 'json':
        dados = leitura_json(path)
    return dados

path_json = '../dados_brutos/dados_empresaA.json'
path_csv = '../dados_brutos/dados_empresaB.csv'

dados_json = leitura_dados(path_json, 'json')
print(dados_json[0])

dados_csv = leitura_dados(path_csv, 'csv')
print(dados_csv[0])

# %%
