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
        self.int = tk.Frame(self.parent, width=largeur_fenetre, height=hauteur_fenetre, bg='black')
        self.int.pack()

        # Rectangle pour le texte
        self.frm_box = tk.Frame(self.parent, bg='white', width= largeur_fenetre, height= hauteur_fenetre, relief= tk.SUNKEN)
        self.frm_box.place(x=0, y=700)

        # Endroit où le texte apparait
        self.lb_text = tk.Label(text="Test", fg="black", bg="white", font=("arial", 20))
        self.lb_text.place(x=100, y=750)

        # Button "Continuer"
        self.btn_continue = tk.Button(self.parent, text="Continuer", fg="black",bg="seashell3", font=("arial", 30))
        self.btn_continue.place(x=1650, y=620)


# Lancement du jeu
root = tk.Tk()
jeu = Game(root)
root.mainloop()





