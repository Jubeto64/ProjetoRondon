from helpers.csv_helper import save_to_csv
from CTkMessagebox import CTkMessagebox

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

        CTkMessagebox(
            title="Sucesso",
            message="Instituição de Ensino Cadastrada",
            icon="check"
        )
