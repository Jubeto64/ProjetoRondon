from helpers.csv_helper import save_to_csv
from CTkMessagebox import CTkMessagebox

class CapacitacaoController:
    def __init__(self):
        self.csv_path = "data/capacitacao.csv"

    def create_entity(self, identificador, nome, descricao, identificador_instituicao):        
        data = {
            "identificador": identificador,
            "nome": nome,
            "descricao": descricao,
            "identificador_instituicao": identificador_instituicao
        }

        save_to_csv(data, self.csv_path)

        CTkMessagebox(
            title="Sucesso",
            message="Capacitação Cadastrada",
            icon="check"
        )
