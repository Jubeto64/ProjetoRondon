import customtkinter as ctk

from views.app_view import AppView
from controllers.instituicao_ensino_controller import InstituicaoEnsinoController

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")

    instituicao_ensino_controller = InstituicaoEnsinoController()

    app = AppView(instituicao_ensino_controller=instituicao_ensino_controller)
    app.mainloop()