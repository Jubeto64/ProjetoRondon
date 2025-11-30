import customtkinter as ctk


class CadastroInstituicaoEnsino(ctk.CTkFrame):
    def __init__(self, parent, app, controller):
        super().__init__(parent)
        self.controller = controller
        self.app = app

        ctk.CTkLabel(self, text="Cadastro de Instituição de Ensino", font=("Arial", 26)).pack(pady=20)

        self.identificador = ctk.CTkEntry(self, placeholder_text="Identificador")
        self.identificador.pack(pady=10)
        
        self.nome = ctk.CTkEntry(self, placeholder_text="Nome")
        self.nome.pack(pady=10)

        self.descricao = ctk.CTkEntry(self, placeholder_text="Descrição")
        self.descricao.pack(pady=10)

        self.senha = ctk.CTkEntry(self, placeholder_text="Senha")
        self.senha.pack(pady=10)

        ctk.CTkButton(self, text="Salvar", command=self.save_entity).pack(pady=20)

        ctk.CTkButton(self, text="Voltar", command=lambda: app.show_frame("Menu")).pack()

    def save_entity(self):
        identificador = self.identificador.get()
        nome = self.nome.get()
        descricao = self.descricao.get()
        senha = self.senha.get()

        if identificador and nome:
            self.controller.create_entity(identificador, nome, descricao, senha)
            self.identificador.delete(0, "end")
            self.nome.delete(0, "end")
            self.descricao.delete(0, "end")
            self.senha.delete(0, "end")