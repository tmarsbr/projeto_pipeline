# %% [markdown]
# ## Análise Detalhada dos Dados json
# 
# Baseado nos metadados, observamos:
# - 10 produtos diferentes
# - 4 categorias de produtos
# - 2687 valores distintos de preços
# - Estoque variando de 0 a 100 unidades
# - 10 filiais diferentes

# %% [markdown]
# Distribuição por Categoria:
# Categoria do Produto
# Eletrônicos         807
# Distribuição por Categoria:
# 
# | Categoria do Produto | Quantidade |
# |----------------------|------------|
# | Eletrônicos          | 807        |
# | Alimentos            | 788        |
# | Eletrodomésticos     | 781        |
# | Roupas               | 747        |
# 
# Name: count, dtype: int64
# Eletrodomésticos    781
# Roupas              747
# Name: count, dtype: int64

# %% [markdown]
# Estatísticas de Preços:
# 
# 
# | Estatística | Valor      |
# |-------------|------------|
# | count       | 3123.000000|
# | mean        | 50.608194  |
# | std         | 28.281982  |
# | min         | 1.030000   |
# | 25%         | 26.385000  |
# | 50%         | 50.670000  |
# | 75%         | 75.220000  |
# | max         | 99.980000  |
# 
# Name: Preço do Produto (R$)
# 50%        50.670000
# 75%        75.220000
# max        99.980000
# Name: Preço do Produto (R$)

# %% [markdown]
# 
#             ### Estoque por Filial:
# 
#             | Filial   | Total de Estoque | Média de Estoque | Mediana de Estoque |
#             |----------|------------------|------------------|--------------------|
#             | Filial 1 | 16723            | 51.93            | 53.0               |
#             | Filial 10| 15166            | 49.89            | 48.5               |
#             | Filial 2 | 14632            | 46.75            | 43.0               |
#             | Filial 3 | 14652            | 47.88            | 46.0               |
#             | Filial 4 | 15173            | 52.32            | 52.0               |
#             | Filial 5 | 14985            | 47.42            | 48.0               |
#             | Filial 6 | 15921            | 48.25            | 46.0               |
#             | Filial 7 | 15069            | 51.78            | 53.0               |
#             | Filial 8 | 17066            | 51.72            | 53.0               |
#             | Filial 9 | 16061            | 50.03            | 48.0               |

# %% [markdown]
# # Análises Detalhadas dos Dados CSV
# 
# dtype | percentual_nulos | valores_distintos
# ----- | ---------------- | ------------------
# Nome do Item (object) | 0.0 | 10
# Classificação do Produto (object) | 0.0 | 4
# Valor em Reais (R$) (float64) | 0.0 | 1234
# Quantidade em Estoque (int64) | 0.0 | 100
# Nome da Loja (object) | 0.0 | 10
# Data da Venda (object) | 0.0 | 354
# 
# ### 1. **Nome do Item**
# - Nulos: 0% (dados completos)
# - Valores distintos: 10
# - Análise:
#   - Existem apenas 10 itens únicos no catálogo.
#   - Pode indicar um negócio com foco em poucos produtos ou uma amostra limitada.
#   - **Sugestão**: Analisar a relação entre esses itens e outras colunas (ex.: lojas que vendem cada item).
# 
# ### 2. **Classificação do Produto**
# - Nulos: 0%
# - Valores distintos: 4
# - Análise:
#   - Sistema simples de categorização (ex.: "Eletrônico", "Vestuário", "Alimento", "Casa").
#   - Permite análises de desempenho por categoria.
#   - **Sugestão**: Cruzar com valores monetários para identificar categorias mais lucrativas.
# 
# ### 3. **Valor em Reais (R$)**
# - Nulos: 0%
# - Valores distintos: 1.234
# - Análise:
#   - Alta variedade de preços (provavelmente valores únicos por transação).
#   - Possível presença de descontos, variações de preço ou itens personalizados.
#   - **Sugestão**: Criar faixas de preço para simplificar análises (ex.: "0-50", "50-100").
# 
# ### 4. **Quantidade em Estoque**
# - Nulos: 0%
# - Valores distintos: 100
# - Análise:
#   - Estoque varia entre 0 e 100 unidades (ou outro intervalo contendo 100 valores).
#   - **Atenção**: Verificar se há registros com estoque zero (risco de perda de vendas).
#   - **Sugestão**: Relacionar estoque com vendas para identificar itens sub/sobre-estocados.
# 
# ### 5. **Nome da Loja**
# - Nulos: 0%
# - Valores distintos: 10
# - Análise:
#   - Rede com 10 lojas físicas ou virtuais.
#   - **Curiosidade**: Número igual ao de itens únicos (10) - investigar se há especialização por loja.
#   - **Sugestão**: Comparar desempenho entre lojas (ex.: vendas médias por unidade).
# 
# ### 6. **Data da Venda**
# - Nulos: 0%
# - Valores distintos: 354
# - Análise:
#   - Dados cobrem aproximadamente 1 ano (354 dias únicos de venda).
#   - **Problema**: Tipo `object` indica datas não formatadas como datetime.
#   - **Sugestão**: Converter para `datetime64` e extrair informações temporais (mês, trimestre, dia da semana).
# 
# ### **Cross-Analysis Recomendada**
# 1. **Sazonalidade**:
#    - Relacionar `Data da Venda` com `Valor em Reais` para identificar picos sazonais.
# 
# 2. **Desempenho por Loja**:
#    - Cruzar `Nome da Loja` com `Classificação do Produto` para mapear preferências regionais.
# 
# 3. **Gestão de Estoque**:
#    - Comparar `Quantidade em Estoque` com frequência de vendas por item.
# 
# 4. **Precificação**:
#    - Analisar a distribuição de `Valor em Reais` por categoria (`Classificação do Produto`).
# 
# ### **Possíveis Problemas a Investigar**
# 1. Por que há exatamente 10 itens e 10 lojas? Há uma relação 1:1?
# 2. Valores únicos em `Data da Venda` (354) sugerem dados diários - confirmar se não há horários registrados.
# 3. Checar duplicidades (ex.: mesma venda registrada múltiplas vezes).
# 


