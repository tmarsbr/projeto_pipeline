# Projeto de Integração de Dados - Clínicas Sanare e Reviver

## Descrição
Este projeto visa integrar e uniformizar os dados das clínicas Sanare e Reviver durante seu processo de fusão. Utilizamos um pipeline de dados orientado a objetos para garantir a consistência e a qualidade dos dados ao longo do processo. Este projeto faz parte da formação inicial em Engenharia de Dados da Alura.

## Estrutura do Projeto
```
projeto_clínicas/
├── dados_brutos/      # Dados originais das clínicas
├── dados_processados/ # Dados processados e uniformizados
├── notebooks/         # Jupyter notebooks para análise exploratória
├── scripts/           # Scripts de processamento
└── docs/              # Documentação adicional
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
python scripts/script_pipeline_fev.py
```

## Scripts
- `script_pipeline_fev.py`: Script principal para processar e unir os dados das duas clínicas.
- `processamento_dados.py`: Contém a classe `Dados` e métodos auxiliares para leitura, transformação e união dos dados.

## Notebooks
- `notebooks/`: Contém notebooks Jupyter para análise exploratória dos dados.

## Contribuição
1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/nova-feature`)
3. Commit suas mudanças (`git commit -am 'Adiciona nova feature'`)
4. Faça push para a branch (`git push origin feature/nova-feature`)
5. Abra um Pull Request

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.
