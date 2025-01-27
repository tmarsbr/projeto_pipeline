# Projeto de Integração de Dados - Clínicas Sanare e Reviver

## Descrição
Este projeto visa integrar e uniformizar os dados das clínicas Sanare e Reviver durante seu processo de fusão.

## Estrutura do Projeto
```
projeto_clínicas/
├── dados_brutos/      # Dados originais das clínicas
├── dados_editados/    # Dados processados e uniformizados
├── notebooks/         # Jupyter notebooks para análise exploratória
├── scripts/          # Scripts de processamento
└── docs/             # Documentação adicional
```

## Configuração do Ambiente

1. Clone o repositório
2. Crie o ambiente virtual:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/Mac
```
3. Instale as dependências:
```bash
pip install -r requirements.txt
```

## Uso
1. Coloque os dados brutos na pasta `dados_brutos/`
2. Execute os notebooks na pasta `notebooks/` para análise exploratória
3. Execute os scripts de processamento:
```bash
python scripts/process_data.py
```
