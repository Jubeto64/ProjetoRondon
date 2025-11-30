import customtkinter as ctk

from views.menu_screen import MenuScreen
from views.cadastro_instituicao_ensino import CadastroInstituicaoEnsino
from views.edicao_instituicao_ensino import EdicaoInstituicaoEnsino
from views.cadastro_capacitacao import CadastroCapacitacao
from views.listagem_capacitacao import ListagemCapacitacao
from views.edicao_capacitacao import EdicaoCapacitacao
from views.autenticacao_instituicao_ensino import AutenticacaoInstituicaoEnsino

class AppView(ctk.CTk):
    def __init__(self, instituicao_ensino_controller, capacitacao_controller):
        super().__init__()

        self.instituicao_ensino_autenticada = None

        self.title("Projeto Rondon")
        self.geometry("700x450")

        self.instituicao_ensino_controller = instituicao_ensino_controller
        self.capacitacao_controller = capacitacao_controller

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {
            "Menu": MenuScreen(self.container, self, instituicao_ensino_controller.csv_path),
            "CadastroInstituicaoEnsino": CadastroInstituicaoEnsino(self.container, self, instituicao_ensino_controller),
            "EdicaoInstituicaoEnsino": EdicaoInstituicaoEnsino(self.container, self, instituicao_ensino_controller.csv_path),
            "CadastroCapacitacao": CadastroCapacitacao(self.container, self, capacitacao_controller),
            "ListagemCapacitacao": ListagemCapacitacao(self.container, self, csv_path=capacitacao_controller.csv_path),
            "EdicaoCapacitacao": EdicaoCapacitacao(self.container, self, capacitacao_controller.csv_path),
            "AutenticacaoInstituicaoEnsino": AutenticacaoInstituicaoEnsino(self.container, self, instituicao_ensino_controller.csv_path)
        }

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()

    def set_instituicao_ensino_autenticada(self, identificador_instituicao):
        self.instituicao_ensino_autenticada = identificador_instituicao