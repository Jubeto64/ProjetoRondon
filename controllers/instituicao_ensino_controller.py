from helpers.csv_helper import save_to_csv

class InstituicaoEnsinoController:
    def __init__(self):
        self.csv_path = "data/instituicao_ensino.csv"

    def create_entity(self, identificador, nome, descricao):        
        data = {
            "identificador": identificador,
            "nome": nome,
            "descricao": descricao
        }
        save_to_csv(data, self.csv_path)
