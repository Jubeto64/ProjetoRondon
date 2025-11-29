import customtkinter as ctk
import pandas as pd
from CTkMessagebox import CTkMessagebox

class EdicaoInstituicaoEnsino(ctk.CTkFrame):
    def __init__(self, parent, app, csv_path):
        super().__init__(parent)
        self.app = app
        self.csv_path = csv_path
        self.entity_id = None

        ctk.CTkLabel(self, text="Edição de Instituição de Ensino", font=("Arial", 26)).pack(pady=20)

        self.identificador = ctk.CTkEntry(self, placeholder_text="Identificador")
        self.identificador.pack(pady=10)
        
        self.nome = ctk.CTkEntry(self, placeholder_text="Nome")
        self.nome.pack(pady=10)

        self.descricao = ctk.CTkEntry(self, placeholder_text="Descricao")
        self.descricao.pack(pady=10)

        ctk.CTkButton(self, text="Atualizar", command=self.save_changes).pack(pady=10)

        ctk.CTkButton(self, text="Excluir", fg_color="red", hover_color="#ff4d4d", command=self.delete_entity).pack(pady=10)

        ctk.CTkButton(self, text="Voltar", command=lambda: app.show_frame("ListagemInstituicaoEnsino")).pack(pady=10)

    def load_entity(self, entity_id):
        self.entity_id = entity_id
        df = pd.read_csv(self.csv_path, dtype={"identificador": str})

        entity = df[df["identificador"] == str(entity_id)].iloc[0]

        self.identificador.delete(0, "end")
        self.nome.delete(0, "end")
        self.descricao.delete(0, "end")

        self.identificador.insert(0, entity["identificador"])
        self.nome.insert(0, entity["nome"])
        self.descricao.insert(0, entity["descricao"])

    def save_changes(self):
        df = pd.read_csv(self.csv_path, dtype={"identificador": str})

        df.loc[df["identificador"] == str(self.entity_id), "nome"] = self.nome.get()
        df.loc[df["identificador"] == str(self.entity_id), "descricao"] = self.descricao.get()
        df.loc[df["identificador"] == str(self.entity_id), "identificador"] = self.identificador.get()

        df.to_csv(self.csv_path, index=False)

        CTkMessagebox(
            title="Sucesso",
            message="Instituição de Ensino Atualizada",
            icon="check"
        )

        self.app.frames["ListagemInstituicaoEnsino"].load_table()
        self.app.show_frame("ListagemInstituicaoEnsino")

    def delete_entity(self):
        answer = CTkMessagebox(
            title="Confirm Delete",
            message="Are you sure?",
            icon="warning",
            option_1="Yes",
            option_2="No"
        ).get()
                
        if answer == "Yes":
            df = pd.read_csv(self.csv_path, dtype={"identificador": str})
            df = df[df["identificador"] != self.entity_id]
            df.to_csv(self.csv_path, index=False)

            CTkMessagebox(title="Excluído", message="Instituição de Ensino Exluída com sucesso!", icon="check")

            self.app.frames["ListagemInstituicaoEnsino"].load_table()
            self.app.show_frame("ListagemInstituicaoEnsino")