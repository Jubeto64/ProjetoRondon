import customtkinter as ctk
import pandas as pd


class ListagemCapacitacao(ctk.CTkFrame):
    def __init__(self, parent, app, csv_path):
        super().__init__(parent)
        self.app = app
        self.csv_path = csv_path

        ctk.CTkLabel(self, text="Listagem de Capacitações", font=("Arial", 26)).pack(pady=20)

        self.table_frame = ctk.CTkScrollableFrame(self, width=600, height=300)
        self.table_frame.pack(pady=10, padx=20, fill="both", expand=True)

        button_frame = ctk.CTkFrame(self)
        button_frame.pack(pady=10)

        ctk.CTkButton(button_frame, text="Atualizar", command=self.load_table).grid(row=0, column=0, padx=10)
        ctk.CTkButton(button_frame, text="Voltar", command=lambda: app.show_frame("Menu")).grid(row=0, column=1, padx=10)

    def clear_table(self):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

    def load_table(self, identificador_instituicao):
        self.clear_table()

        try:
            df = pd.read_csv(self.csv_path, dtype={"identificador": str, "identificador_instituicao": str})
        except FileNotFoundError:
            ctk.CTkLabel(self.table_frame, text="Arquivo CSV não encontrado").pack()
            return
        except pd.errors.EmptyDataError:
            ctk.CTkLabel(self.table_frame, text="Arquivo CSV vazio").pack()
            return
        
        df_filtered = df[df["identificador_instituicao"] == str(identificador_instituicao)]

        if df_filtered.empty:
            ctk.CTkLabel(self.table_frame, text="Capacitações não encontradas").pack()
            return

        columns = list(df_filtered.columns) + ["Editar"]

        for col_index, col_name in enumerate(columns):
            header = ctk.CTkLabel(self.table_frame, text=col_name, font=("Arial", 14, "bold"))
            header.grid(row=0, column=col_index, padx=10, pady=5)

        for row_index, row in df_filtered.iterrows():
            for col_index, value in enumerate(row):
                cell = ctk.CTkLabel(self.table_frame, text=str(value), font=("Arial", 13))
                cell.grid(row=row_index + 1, column=col_index, padx=10, pady=4)

            edit_btn = ctk.CTkButton(
                self.table_frame,
                text="Editar",
                width=80,
                command=lambda entity_id=row["identificador"]: self.open_edit_screen(entity_id)
            )
            edit_btn.grid(row=row_index + 1, column=len(columns) - 1, padx=10)

    def open_edit_screen(self, entity_id):
        self.app.frames["EdicaoCapacitacao"].load_entity(entity_id)
        self.app.show_frame("EdicaoCapacitacao")