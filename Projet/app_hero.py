import tkinter as tk

import click


# Frame détaillé du menu principal
class Frame_Accueil(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        tk.Label(self, text="PYTHONLAND QUEST", fg="red4", bg="gray65", font=("arial", 100)).pack(pady=100)
        tk.Button(self, text="Commencer", fg="black", bg="seashell3", font=("arial", 70),
                  command=self.starting_game).pack(pady=20)
        tk.Button(self, text="Explication/But du jeu", fg="black", bg="seashell3", font=("arial", 50),
                  command=self.show_explication).pack(pady=20)
        tk.Button(self, text="Quitter le jeu", fg="black", bg="seashell3", font=("arial", 50),
                  command=parent.destroy).pack(pady=20)

    def show_explication(self):
        self.pack_forget()
        explication_frame = But_Jeu(self.parent)
        explication_frame.pack(fill='both', expand=True)

    def starting_game(self):
        self.pack_forget()
        game_frame = Start_Game(self.parent)
        game_frame.pack(fill='both', expand=True)

# Menu Explication
class But_Jeu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.label = tk.Label(self, text="Le but du jeu est de vous en sortir de vivant de votre péripétie dans PythonLand Quest selon vox choix !\nQuand un choix vous sera demandé, vous devez entrer le numéro correspondant pour continuer et aussi appuyé sur Enter pour continuer l'intrigue\Vous commencez la partie avec comme base de 50 PV,\nsi cela tombe à 0, vous avez perdu...\nMais Attention ! Certains de vos choix vous seront bénéfiques comme un gain de points de vie tandis que d'autres vous nuieront comme une perte de vos points de vie ou la défaite directement! "
                              , bg="white", font=("arial", 15))
        self.label.place(x=50, y=400)
        tk.Button(self, text="Retour", fg="black", bg="seashell3", font=("arial", 50), command=self.show_main).pack(
            pady=300)

    def show_main(self):
        self.pack_forget()
        main_window = Frame_Accueil(self.master)
        main_window.pack(fill='both', expand=True)


# Commencement du Jeu
class Start_Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        pass

# Fenetre de jeu
root = tk.Tk()
root.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
root.geometry("1920x1080")
root.resizable(True, True)  # non-resizable width, height

# Menu principal
main_window = Frame_Accueil(root)
main_window.pack(fill='both', expand=True)

# Main loop (blocage ici tant qu'on n'a pas quittée)
root.mainloop()
