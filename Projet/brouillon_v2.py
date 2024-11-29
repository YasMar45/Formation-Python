import tkinter
import tkinter as tk

# Taille de la fenêtre et de la grille
largeur_fenetre = 1920
hauteur_fenetre = 1080

class Game(tk.Frame):
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")

        # Interface de base
        self.int = tk.Canvas(self.parent, width=largeur_fenetre, height=hauteur_fenetre, bg='black')
        self.int.pack()


# Lancement du jeu
root = tk.Tk()
jeu = Game(root)
root.mainloop()





