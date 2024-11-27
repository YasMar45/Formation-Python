import tkinter as tk


# Frame détaillé du menu principal
class Frame_Accueil(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller  # Référence au contrôleur

        tk.Label(self, text="PYTHONLAND QUEST", fg="red4", bg="gray65", font=("arial", 100)).pack(pady=100)
        tk.Button(self, text="Commencer", fg="black", bg="seashell3", font=("arial", 70)).pack(pady=20)
        tk.Button(self, text="Explication/But du jeu", fg="black", bg="seashell3", font=("arial", 70),
                  command=lambda: controller.show_frame("But_Jeu")).pack(pady=20)
        tk.Button(self, text="Quitter le jeu", fg="black", bg="seashell3", font=("arial", 70),
                  command=parent.destroy).pack(pady=20)


# Frame pour les explications
class But_Jeu(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller

        tk.Label(self, text="Explications du Jeu", fg="black", bg="white", font=("arial", 80)).pack(pady=100)
        tk.Button(self, text="Retour", fg="black", bg="seashell3", font=("arial", 50),
                  command=lambda: controller.show_frame("Frame_Accueil")).pack(pady=50)


# Fenêtre principale du jeu
class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
        self.geometry("1920x1080")

        # Stocke les frames
        self.frames = {}
        for F in (Frame_Accueil, But_Jeu):
            frame = F(self, self)  # Passe l'instance actuelle comme contrôleur
            self.frames[F.__name__] = frame
            frame.pack(fill='both', expand=True)

        self.show_frame("Frame_Accueil")  # Affiche la frame d'accueil par défaut

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()  # Met la frame au premier plan


# Lancement de l'application
if __name__ == "__main__":
    app = MainApp()
    app.mainloop()