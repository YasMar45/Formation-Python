import tkinter as tk
from tkinter import PhotoImage

# Taille de la fenêtre
largeur_fenetre = 1920
hauteur_fenetre = 1080


class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
        self.parent.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")
        self.parent.resizable(True, True)

        # Frame principale
        self.int = tk.Frame(self.parent, bg='black')
        self.int.pack(fill=tk.BOTH, expand=True)

        # Frame pour l'image (2/3 de la largeur)
        self.frame_image = tk.Frame(self.int, bg='grey')
        self.frame_image.place(relwidth=2 / 3, relheight=3 / 4)

        # Image au-dessus de la boîte de message
        self.image = PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/elden ring projet bg.png")
        self.img_label = tk.Label(self.frame_image, image=self.image)
        self.img_label.pack(expand=True)

        # Frame Button pour les choix
        self.btn_frame = tk.Frame(self.int, bg='black')
        self.btn_frame.place(relx=2 / 3, relwidth=1 / 3, relheight=3 / 4)

        # Boutons pour les choix
        self.btn_1 = tk.Button(self.btn_frame, text="Chemin de Gauche")
        self.btn_1.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.btn_2 = tk.Button(self.btn_frame, text="Chemin de Droite")
        self.btn_2.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Boîte de message en bas
        self.frm_box = tk.LabelFrame(self.int, text="NARRATION", bg="white", relief=tk.SUNKEN)
        self.frm_box.place(rely=3 / 4, relwidth=1, relheight=1 / 4)

        # Texte dans la boîte de message
        self.lb_text = tk.Label(self.frm_box, text="Bienvenue dans le monde de PythoLand Quest!", fg="black", bg="white",
                                font=("arial", 20))
        self.lb_text.pack(expand=True, pady=20)


# Créer et exécuter l'application
root = tk.Tk()
game = Game(root)
root.mainloop()


