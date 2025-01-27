import json
import csv

class Dados:
    def __init__(self, path, tipo_dados):
        self.path = path
        self.tipo_dados = tipo_dados
        self.dados = self.leitura_dados()
        self.nome_colunas = self.get_columns()

    def leitura_json(self):
        """
        Lê um arquivo JSON e retorna os dados como uma lista de dicionários.
        
        Returns:
        list: Dados do arquivo JSON.
        """
        with open(self.path, 'r') as file:
            dados_json = json.load(file)
        return dados_json

    def leitura_csv(self):
        """
        Lê um arquivo CSV e retorna os dados como uma lista de dicionários.
        
        Returns:
        list: Dados do arquivo CSV.
        """
        dados_csv = []
        with open(self.path, 'r') as file:
            spamreader = csv.DictReader(file, delimiter=',')
            for row in spamreader:
                dados_csv.append(row)
        return dados_csv

    def leitura_dados(self):
        """
        Lê um arquivo de dados (JSON ou CSV) e retorna os dados como uma lista de dicionários.
        
        Returns:
        list: Dados do arquivo.
        """
        if self.tipo_dados == 'csv':
            return self.leitura_csv()
        elif self.tipo_dados == 'json':
            return self.leitura_json()
        else:
            raise ValueError("Tipo de arquivo não suportado: {}".format(self.tipo_dados))

    def get_columns(self):
        """
        Retorna os nomes das colunas dos dados.
        
        Returns:
        list: Lista com os nomes das colunas.
        """
        return list(self.dados[-1].keys())

    def rename_columns(self, key_mapping):
        """
        Renomeia as colunas dos dados de acordo com o mapeamento fornecido.
        
        Args:
        key_mapping (dict): Dicionário de mapeamento das colunas.
        """
        new_dados = []
        for old_dict in self.dados:
            dict_temp = {}
            for old_key, value in old_dict.items():
                dict_temp[key_mapping.get(old_key, old_key)] = value
            new_dados.append(dict_temp)
        self.dados = new_dados
        self.nome_colunas = self.get_columns()
