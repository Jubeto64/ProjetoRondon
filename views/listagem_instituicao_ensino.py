import customtkinter as ctk
import pandas as pd


class ListagemInstituicaoEnsino(ctk.CTkFrame):
    def __init__(self, parent, app, csv_path):
        super().__init__(parent)
        self.app = app
        self.csv_path = csv_path

        ctk.CTkLabel(self, text="Listagem de Instituições de Ensino", font=("Arial", 26)).pack(pady=20)

        self.table_frame = ctk.CTkScrollableFrame(self, width=600, height=300)
        self.table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Atualizar", command=self.load_table).grid(row=0, column=0, padx=10)
        ctk.CTkButton(button_frame, text="Voltar", command=lambda: app.show_frame("Menu")).grid(row=0, column=1, padx=10)

        self.load_table()

    def clear_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

    def load_table(self):
        self.clear_table()

        try:
            df = pd.read_csv(self.csv_path)
        except FileNotFoundError:
            ctk.CTkLabel(self.table_frame, text="Arquivo CSV não encontrado").pack()
            return
        except pd.errors.EmptyDataError:
            ctk.CTkLabel(self.table_frame, text="Arquivo CSV vazio").pack()
            return

        for col_index, col_name in enumerate(df.columns):
            header = ctk.CTkLabel(self.table_frame, text=col_name, font=("Arial", 14, "bold"))
            header.grid(row=0, column=col_index, padx=10, pady=5)

        for row_index, row in df.iterrows():
            for col_index, value in enumerate(row):
                cell = ctk.CTkLabel(self.table_frame, text=str(value), font=("Arial", 13))
                cell.grid(row=row_index + 1, column=col_index, padx=10, pady=3)