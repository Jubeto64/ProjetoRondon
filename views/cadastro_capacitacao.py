import customtkinter as ctk


class CadastroCapacitacao(ctk.CTkFrame):
    def __init__(self, parent, app, controller):
        super().__init__(parent)
        self.controller = controller
        self.app = app

        ctk.CTkLabel(self, text="Cadastro de Capacitação", font=("Arial", 26)).pack(pady=20)

        self.identificador_instituicao = None

        self.identificador = ctk.CTkEntry(self, placeholder_text="Identificador")
        self.identificador.pack(pady=10)
        
        self.nome = ctk.CTkEntry(self, placeholder_text="Nome")
        self.nome.pack(pady=10)

        self.descricao = ctk.CTkEntry(self, placeholder_text="Descricao")
        self.descricao.pack(pady=10)

        ctk.CTkButton(self, text="Salvar", command=self.save_entity).pack(pady=20)

        ctk.CTkButton(self, text="Voltar", command=self.open_edit_screen).pack()

    def set_identificador_instituicao(self, identificador_instituicao):
        self.identificador_instituicao = identificador_instituicao

    def save_entity(self):
        identificador = self.identificador.get()
        nome = self.nome.get()
        descricao = self.descricao.get()
        identificador_instituicao = self.identificador_instituicao

        if identificador and nome:
            self.controller.create_entity(identificador, nome, descricao, identificador_instituicao)
            self.identificador.delete(0, "end")
            self.nome.delete(0, "end")
            self.descricao.delete(0, "end")

    def open_edit_screen(self):
        self.app.frames["EdicaoInstituicaoEnsino"].load_entity(self.identificador_instituicao)
        self.app.show_frame("EdicaoInstituicaoEnsino")