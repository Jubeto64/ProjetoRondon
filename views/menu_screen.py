import customtkinter as ctk
import pandas as pd
from CTkMessagebox import CTkMessagebox

class MenuScreen(ctk.CTkFrame):
    def __init__(self, parent, app, csv_path):
        super().__init__(parent)
        self.app = app
        self.csv_path = csv_path

        ctk.CTkLabel(self, text="Projeto Rondon", font=("Arial", 30)).pack(pady=15)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=15)

        ctk.CTkButton(
            button_frame,
            text="Cadastro",
            command=lambda: app.show_frame("CadastroInstituicaoEnsino")
        ).grid(row=0, column=0, padx=10)

        ctk.CTkButton(
            button_frame,
            text="Autenticação",
            command=lambda: app.show_frame("AutenticacaoInstituicaoEnsino")
        ).grid(row=0, column=1, padx=10)

        ctk.CTkLabel(self, text="Instituições de Ensino", font=("Arial", 26)).pack(pady=15)
        ctk.CTkButton(self, text="Atualizar Listagem", command=self.load_table).pack(pady=5)

        self.table_frame = ctk.CTkScrollableFrame(self, width=600, height=300)
        self.table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        self.load_table()

    def clear_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

    def load_table(self):
        self.clear_table()

        try:
            df = pd.read_csv(self.csv_path, dtype={"identificador": str})
        except FileNotFoundError:
            ctk.CTkLabel(self.table_frame, text="Arquivo CSV não encontrado").pack()
            return
        except pd.errors.EmptyDataError:
            ctk.CTkLabel(self.table_frame, text="Arquivo CSV vazio").pack()
            return
        
        df_filtered = df.drop("senha", axis=1)
        
        columns = list(df_filtered.columns)

        if self.app.instituicao_ensino_autenticada is not None:
            columns = columns + ["Editar"] + ["Excluir"]

        for col_index, col_name in enumerate(columns):
            header = ctk.CTkLabel(self.table_frame, text=col_name, font=("Arial", 14, "bold"))
            header.grid(row=0, column=col_index, padx=10, pady=5)

        for row_index, row in df_filtered.iterrows():
            for col_index, value in enumerate(row):
                cell = ctk.CTkLabel(self.table_frame, text=str(value), font=("Arial", 13))
                cell.grid(row=row_index + 1, column=col_index, padx=10, pady=4)

            if self.app.instituicao_ensino_autenticada == row["identificador"]:
                edit_btn = ctk.CTkButton(
                    self.table_frame,
                    text="Editar",
                    width=80,
                    command=lambda entity_id=row["identificador"]: self.open_edit_screen(entity_id)
                )
                edit_btn.grid(row=row_index + 1, column=len(columns) - 2, padx=10)

                del_btn = ctk.CTkButton(
                    self.table_frame,
                    text="Deletar",
                    width=80,
                    command=lambda entity_id=row["identificador"]: self.delete_entity(entity_id)
                )
                del_btn.grid(row=row_index + 1, column=len(columns) - 1, padx=10)

    def open_edit_screen(self, entity_id):
        self.app.frames["EdicaoInstituicaoEnsino"].load_entity(entity_id)
        self.app.show_frame("EdicaoInstituicaoEnsino")

    def delete_entity(self, entity_id):
        answer = CTkMessagebox(
            title="Confirmar Exclusão",
            message="Realmente deseja Excluir?",
            icon="warning",
            option_1="Sim",
            option_2="Não"
        ).get()
                
        if answer == "Sim":
            df = pd.read_csv(self.csv_path, dtype={"identificador": str})
            df = df[df["identificador"] != entity_id]
            df.to_csv(self.csv_path, index=False)

            CTkMessagebox(title="Excluído", message="Instituição de Ensino Exluída com sucesso!", icon="check")

            self.load_table()