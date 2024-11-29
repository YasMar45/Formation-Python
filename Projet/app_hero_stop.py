import tkinter
import tkinter as tk

# Variable des points de vie
player_health = 50
max_player_health = 100
player_name = ''
weapon_choice = ''
player_weapon = ''


# Mécanique de Points de vie
def health_meca():
    global player_health
    global max_player_health
    if player_health > max_player_health:
        player_health = max_player_health
        print("Vous êtes au maximum de PV possible!")


# Si PV arrive à 0, Défaite
def check_health():
    global player_health
    if player_health <= 0:
        print("Mais...")
        print("Vous succombez de vos blessures,Défaite...")
        print("Retour au menu principal")
        Frame_Accueil(root)

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

        # Button du Menu Princiaple
        tk.Label(self, text="PYTHONLAND QUEST", fg="red4", bg="white", font=("arial", 100), relief=tkinter.RIDGE).pack(
            pady=100)
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
        self.main_window = None
        # Fond D'écran dans le menu
        self.lbl_background = tk.Label(self)
        self.img = tk.PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/beginnerlogo.png")
        self.lbl_background.config(image=self.img)
        self.lbl_background.image = self.img  # Nécessaire pour conserver la référence de l'image
        self.lbl_background.place(x=0, y=0, relwidth=1, relheight=1)

        # Zone de texte pour le But du Jeu
        self.lbl_description = tk.Label(self,
                                        text=f"Le but du jeu est de vous en sortir de vivant de votre péripétie dans PythonLand Quest selon vox choix !\nQuand un choix vous sera demandé, vous devez entrer le numéro correspondant pour continuer et aussi appuyé sur Enter pour continuer l'intrigue\Vous commencez la partie avec comme base de {player_health} PV,\nsi cela tombe à 0, vous avez perdu...\nMais Attention ! Certains de vos choix vous seront bénéfiques comme un gain de points de vie tandis que d'autres vous nuieront comme une perte de vos points de vie ou la défaite directement! "
                                        , bg="white", font=("arial", 15))

        # Bouton Retour
        self.lbl_description.place(x=50, y=400)
        tk.Button(self, text="Retour", fg="black", bg="seashell3", font=("arial", 50), command=self.show_main).place(
            x=840, y=900)

    def show_main(self):
        self.pack_forget()
        self.main_window = Frame_Accueil(self.master)
        self.main_window.pack(fill='both', expand=True)


# Commencement du Jeu
class Start_Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.lbl_background = None
        self.lbl_description = None
        self.btn_continue = None
        self.init_ui()

    def init_ui(self):
        # Fond d'écran pour l'introduction
        self.lbl_background = tk.Label(self)
        self.img = tk.PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/donjonstart.png")
        self.lbl_background.config(image=img)
        self.lbl_background.image = img  # Nécessaire pour conserver la référence de l'image
        self.lbl_background.place(x=0, y=-75, relwidth=1, relheight=1)

        # Message Box en blanc tout simplement
        self.lbl_msg = tk.Label(self,
                                text="Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te",
                                fg="white", bg="white", font=("arial", 30), relief=tk.RIDGE)
        self.lbl_msg.place(x=50, y=750)

        # Endroit où le texte apparait
        self.lbl_description = tk.Label(self,
                                        text="Bievenu(e) dans le monde de PythoLand Quest!\nVous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!\nVotre quête commence ici dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies",
                                        fg="black", bg="white", font=("arial", 25))
        self.lbl_description.place(x=100, y=800)

        # Bouton pour continuer
        self.btn_continue = tk.Button(self, text="Continuer", fg="black", bg="seashell3", font=("arial", 20),
                                      command=self.name_choice)
        self.btn_continue.place(x=1700, y=685)

        self.update()

    # Entrer son nom
    def name_choice(self):
        # Fond d'écran
        lbl_background = tk.Label(self)
        img = tk.PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/demandenom.png")
        lbl_background.config(image=img)
        lbl_background.image = img  # Nécessaire pour conserver la référence de l'image
        lbl_background.place(x=0, y=-75, relwidth=1, relheight=1)
        bg = lbl_background
        # Message box
        self.lbl_msg = tk.Label(self,
                                text="Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te",
                                fg="white", bg="white", font=("arial", 30), relief=tk.RIDGE)
        self.lbl_msg.place(x=50, y=750)

        # Endroit où le texte apparait
        tk.Label(self,
                 text="Faites attention ! Il faudra vous remplir de courage et y aller pour vous en sortir vivant,cela ne va pas être facile!\nVos choix vous meneront vers la victoire mais aussi très souvent vers la défaite, Bonne chance...\nMais avant tout quel est ton nom qui va 'peut-être rentrer dans la légende...'"
                 , fg="black", bg="white", font=("arial", 25)).place(x=100, y=800)

        # Ajouter des composants de choix de nom ici, par exemple
        tk.Label(self, text="Entrer votre nom:", fg="black", font=("arial", 20, "bold")).place(x=650, y=600)
        self.ent_name = tk.Entry(self, font=("arial", 20))
        self.ent_name.place(x=1000, y=600)

        self.btn_continue = tk.Button(self, text="Continuer", fg="black", bg="seashell3", font=("arial", 20),
                                      command=self.on_continue)
        self.btn_continue.place(x=1700, y=685)

        self.update()

    def on_continue(self):
        global player_name
        player_name = self.ent_name.get()
        self.weapon_choice()

    def clear_frame_contents(self):
        for widget in self.winfo_children():
            widget.place_forget()

    # Choix Arme
    def weapon_choice(self):
        # Fond d'écran
        background = tk.Label(self)
        img = tk.PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/weaponchoice.png")
        background.config(image=img)
        background.image = img  # Nécessaire pour conserver la référence de l'image
        background.place(x=100, y=-75, relwidth=1, relheight=1)
        bg = background

        # Message Box en blanc tout simplement
        tk.Label(self,
                 text="Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te",
                 fg="white", bg="white", font=("arial", 30), relief=tkinter.RIDGE).place(x=50, y=750)

        # Endroit où le texte apparait
        tk.Label(self,
                 text=f"Très bien {player_name}, votre aventure commence dès maintenant,bonne chance....\nVous vous revéillez dans cette cellule humide et immonde, juste quelques bougies vous éclaire...'\nVous vous levez et apercevez le couloir qui découle de votre cellule...'\nAu sol, 3 armes sont devant vous mais une seule pourra être portée,laquelle choissisez vous ?"
                 , fg="black", bg="white", font=("arial", 25)).place(x=270, y=800)

        #Bouton pour le choix d'armes
        self.btn_weapon_1 = tk.Button(self, text ='"Epee et Bouclier"', fg="black", font=("arial", 30, "bold"),
                                      command=self.player_weapon_choice)
        self.btn_weapon_1.place(x=80, y=200)

        self.btn_weapon_2 = tk.Button(self, text='"Double Dagues"', fg="black", font=("arial", 30, "bold"),
                                      command=self.player_weapon_choice)
        self.btn_weapon_2.place(x=80, y=400)

        self.btn_weapon_3 = tk.Button(self, text='"Massue"', fg="black", font=("arial", 30, "bold"),
                                      command=self.player_weapon_choice)
        self.btn_weapon_3.place(x=80, y=600)

        self.update()

    def player_weapon_choice(self):
        global player_weapon
        player_weapon = self.btn_weapon_1.cget("text")
        self.first_encounter()

    def first_encounter(self):
        global player_weapon
        # Fond d'écran
        background = tk.Label(self)
        img = tk.PhotoImage(
            file="/home/student213-06/PycharmProjects/Formation-Python/Projet/image projet/first encounter.png")
        background.config(image=img)
        background.image = img  # Nécessaire pour conserver la référence de l'image
        background.place(x=0, y=-75, relwidth=1, relheight=1)
        bg = background

        # Message Box en blanc tout simplement
        tk.Label(self,
                 text="Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te\nTest Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Test Te",
                 fg="white", bg="white", font=("arial", 30), relief=tkinter.RIDGE).place(x=50, y=750)

        # Endroit où le texte apparait
        tk.Label(self,
                 text=f"Vous avez ramassé {player_weapon}!\n Vous vous aventuré dans le donjon pour chercher la sortie...\nVous voyez une lumière au loin, surement la sortie!\nMais une silhouette garde la sortie! Que faites-vous !?"
                 , fg="black", bg="white", font=("arial", 25)).place(x=500, y=770)

        #Bouton Continuer
        self.btn_continue = tk.Button(self, text="Continuer", fg="black", bg="seashell3", font=("arial", 20),
                                      command=self.on_continue)
        self.btn_continue.place(x=1700, y=685)


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


# Fonction pour les textes qui defilent lentemenet
"""def slow_print(text, delay=0.1):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()
"""