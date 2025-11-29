import customtkinter as ctk

from views.menu_screen import MenuScreen
from views.cadastro_instituicao_ensino import CadastroInstituicaoEnsino

class AppView(ctk.CTk):
    def __init__(self, instituicao_ensino_controller):
        super().__init__()

        self.title("Projeto Rondon")
        self.geometry("700x450")

        self.instituicao_ensino_controller = instituicao_ensino_controller

        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True)

        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {
            "Menu": MenuScreen(self.container, self),
            "CadastroInstituicaoEnsino": CadastroInstituicaoEnsino(self.container, self, instituicao_ensino_controller)
        }

        for frame in self.frames.values():
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("Menu")

    def show_frame(self, name):
        frame = self.frames[name]
        frame.tkraise()