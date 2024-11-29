import tkinter
import tkinter as tk

import debian.changelog

# Taille de la fenêtre et de la grille
largeur_fenetre = 1920
hauteur_fenetre = 1080


class Game(tk.Frame):
    def __init__(self, parent):
        self.parent = parent

        self.parent.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")

        # Interface de base
        self.int = tk.Frame(self.parent, width=largeur_fenetre, height=hauteur_fenetre, bg='black')
        self.int.pack()

        # Rectangle pour le texte
        self.frm_box = tk.LabelFrame(self.parent, text= "Texte", bg='white', width=1920, height=400, relief= tk.SUNKEN)
        self.frm_box.pack(side = "bottom")

        # Endroit où le texte apparait
        self.lb_text = tk.Label(self.frm_box, text="Bievenu(e) dans le monde de PythoLand Quest!", fg="black", bg="white", font=("arial", 20))
        self.lb_text.pack()

# Lancement du jeu
root = tk.Tk()
jeu = Game(root)
root.mainloop()





