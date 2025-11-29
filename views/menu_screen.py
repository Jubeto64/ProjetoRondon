import customtkinter as ctk


class MenuScreen(ctk.CTkFrame):
    def __init__(self, parent, app):
        super().__init__(parent)

        ctk.CTkLabel(self, text="Menu", font=("Arial", 30)).pack(pady=40)

        ctk.CTkButton(
            self, text="Cadastro de Instituicao de Ensino",
            command=lambda: app.show_frame("CadastroInstituicaoEnsino")
        ).pack(pady=15)

        ctk.CTkButton(
            self, text="Listagem de Instituições de Ensino",
            command=lambda: app.show_frame("ListagemInstituicaoEnsino")
        ).pack(pady=15)