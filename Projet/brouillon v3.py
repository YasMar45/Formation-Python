import tkinter as tk

# Taille de la fenêtre
largeur_fenetre = 1920
hauteur_fenetre = 1080


class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
        self.parent.geometry("1920x1080")
        self.parent.resizable(True, True)

        # Interface en noir
        self.int = tk.Frame(self.parent, width=largeur_fenetre, height=hauteur_fenetre, bg='black')
        self.int.grid(row=0, column=0, sticky="nsew")

        self.parent.grid_rowconfigure(0, weight=1)
        self.parent.grid_columnconfigure(0, weight=1)

        self.frm_box = tk.LabelFrame(self.int, text="Narration", bg="white", width=1900, height=300, relief=tk.SUNKEN)
        self.frm_box.grid(row=1, column=0, sticky="ew", pady=(0, 10))

        self.int.grid_rowconfigure(0, weight=1)
        self.int.grid_rowconfigure(1, weight=0)
        self.int.grid_columnconfigure(0, weight=1)

        # Endroit où le texte apparait
        self.lb_text = tk.Label(self.frm_box, text="Bienvenue dans le monde de PythoLand Quest!", fg="black",
                                bg="white", font=("arial", 20))
        self.lb_text.grid(pady=70)


# Fenetre de jeu
root = tk.Tk()
jeu = Game(root)
root.mainloop()
