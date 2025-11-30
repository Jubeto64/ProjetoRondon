import customtkinter as ctk
import pandas as pd
from CTkMessagebox import CTkMessagebox

class AutenticacaoInstituicaoEnsino(ctk.CTkFrame):
    def __init__(self, parent, app, csv_path):
        super().__init__(parent)
        self.app = app
        self.csv_path = csv_path

        ctk.CTkLabel(self, text="Autenticacao de Instituição de Ensino", font=("Arial", 26)).pack(pady=20)

        self.identificador = ctk.CTkEntry(self, placeholder_text="Identificador")
        self.identificador.pack(pady=10)

        self.senha = ctk.CTkEntry(self, placeholder_text="Senha", show='*')
        self.senha.pack(pady=10)

        ctk.CTkButton(self, text="Autenticar", command=self.authenticate).pack(pady=20)

        ctk.CTkButton(self, text="Voltar", command=lambda: app.show_frame("Menu")).pack()

    def authenticate(self):
        identificador = self.identificador.get()
        senha = self.senha.get()

        df = pd.read_csv(self.csv_path, dtype={"identificador": str, "senha": str})

        entity = df[(df["identificador"] == str(identificador)) & (df["senha"] == str(senha))]

        if entity.empty:
            CTkMessagebox(
                title="Acesso negado",
                message="Credenciais inválidas",
                icon="cancel"
            )
        else:
            self.app.set_instituicao_ensino_autenticada(entity.iloc[0]["identificador"])
            CTkMessagebox(
                title="Sucesso",
                message="Autenticado realizada",
                icon="check"
            )
            self.app.show_frame("Menu")