import tkinter
import tkinter as tk

# Frame détaillé du menu principal
class Frame_Accueil(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent

        # Fond D'écran dans le menu
        background = tk.Label(self)
        img = tk.PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/elden ring projet bg.png")
        background.config(image=img)
        background.image = img  # Nécessaire pour conserver la référence de l'image
        background.place(x=0, y=0, relwidth=1, relheight=1)
        bg = background

        #Button du Menu Princiaple
        tk.Label(self, text="PYTHONLAND QUEST", fg="red4", bg="white",font=("arial", 100), relief=tkinter.RIDGE).pack(pady=100)
        tk.Button(self, text="Commencer votre aventure", fg="black", bg="seashell3", font=("arial", 70),
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

        # Fond D'écran dans le menu
        background = tk.Label(self)
        img = tk.PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/beginnerlogo.png")
        background.config(image=img)
        background.image = img  # Nécessaire pour conserver la référence de l'image
        background.place(x=0, y=0, relwidth=1, relheight=1)
        bg = background

        #Zone de texte pour le But du Jeu
        self.label = tk.Label(self, text="Le but du jeu est de vous en sortir de vivant de votre péripétie dans PythonLand Quest selon vox choix !\nQuand un choix vous sera demandé, vous devez entrer le numéro correspondant pour continuer et aussi appuyé sur Enter pour continuer l'intrigue\Vous commencez la partie avec comme base de 50 PV,\nsi cela tombe à 0, vous avez perdu...\nMais Attention ! Certains de vos choix vous seront bénéfiques comme un gain de points de vie tandis que d'autres vous nuieront comme une perte de vos points de vie ou la défaite directement! "
                              , bg="white", font=("arial", 15))

        #Bouton Retour
        self.label.place(x=50, y=400)
        tk.Button(self, text="Retour", fg="black", bg="seashell3", font=("arial", 50), command=self.show_main).place(x=840, y=900)

    def show_main(self):
        self.pack_forget()
        main_window = Frame_Accueil(self.master)
        main_window.pack(fill='both', expand=True)

# Commencement du Jeu
class Start_Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Fond d'écran pour l'introduction
        background = tk.Label(self)
        img = tk.PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/donjonstart.png")
        background.config(image=img)
        background.image = img  # Nécessaire pour conserver la référence de l'image
        background.place(x=0, y=-75, relwidth=1, relheight=1)

        # Message Box en blanc tout simplement
        tk.Label(self,
                 text="Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te",
                 fg="white", bg="white", font=("arial", 30), relief=tkinter.RIDGE).place(x=50, y=750)

        # Endroit où le texte apparait
        tk.Label(self, text="Bievenu(e) dans le monde de PythoLand Quest!\nVous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!\nVotre quête commence ici dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies"
                 , fg="black", bg="white", font=("arial", 25)).place(x=100,y=800)

        # Bouton pour continuer
        self.continue_button = tk.Button(self, text="Continuer", fg="black", bg="seashell3", font=("arial", 20),command=self.name_choice)
        self.continue_button.place(x=1700, y=685)

    def name_choice(self):
        self.pack_forget()
        name_choice_frame = Name_Choice(self.master)
        name_choice_frame.pack(fill='both', expand=True)

# Entrée pour le nom du joueur
class Name_Choice(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        # Fond d'écran
        background = tk.Label(self)
        img = tk.PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/beginnerlogo.png")
        background.config(image=img)
        background.image = img  # Nécessaire pour conserver la référence de l'image
        background.place(x=0, y=-75, relwidth=1, relheight=1)
        bg = background

        # Message Box en blanc tout simplement
        tk.Label(self,
                 text="Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te",
                 fg="white", bg="white", font=("arial", 30), relief=tkinter.RIDGE).place(x=50, y=750)

        #Entrez le nom du joueur
        self.name_label = tk.Label(self, text="Entrez votre nom:", fg="black", bg="white", font=("arial", 20))
        self.name_label.place(x=800, y=400)
        self.name_entry = tk.Entry(self, font=("arial", 20))
        self.name_entry.place(x=850, y=400)


# Choix d'Armes
class Weapon_Choice(tk.Frame):
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