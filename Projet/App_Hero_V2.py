import tkinter as tk

# Taille de la fenêtre
largeur_fenetre = 1920
hauteur_fenetre = 1080

player_name = ""

class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
        self.parent.geometry(f"{largeur_fenetre}x{hauteur_fenetre}")
        self.parent.resizable(True, True)

        #Point de vie
        self.health = 50
        if self.health <= 0:
            self.health = 0
            pass

        #Attaque du joueur
        self.player_damage = 0

        #Arme
        self.weapon = ''


        # Frame principale
        self.int = tk.Frame(self.parent, bg='black')
        self.int.pack(fill=tk.BOTH, expand=True)

        # Frame pour l'image
        self.frame_image = tk.Frame(self.int, bg='grey')
        self.frame_image.place(relwidth=2 / 3, relheight=3 / 4)

        # Image au-dessus de la boîte de message
        self.current_image = tk.PhotoImage(
            file="images/donjonstart.png")
        self.lbl_image = tk.Label(self.frame_image, image=self.current_image)
        self.lbl_image.pack(expand=True)

        # Frame Button pour les choix
        self.btn_frame = tk.Frame(self.int, bg='black')
        self.btn_frame.place(relx=2 / 3, relwidth=1 / 3, relheight=3 / 4)

        # Boutons pour les choix
        self.btn_1 = tk.Button(self.btn_frame, text="Chemin de Gauche", command=lambda: self.make_choice_1('gauche'))
        self.btn_1.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.btn_2 = tk.Button(self.btn_frame, text="Chemin de Droite", command=lambda: self.make_choice_1('droite'))
        self.btn_2.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Boîte de message en bas
        self.frm_box = tk.LabelFrame(self.int, text="NARRATION", bg="white", relief=tk.SUNKEN)
        self.frm_box.place(rely=3 / 4, relwidth=1, relheight=1 / 4)

        # Texte dans la boîte de message
        self.lbl_text = tk.Label(self.frm_box,
                                 text=f"Bienvenue dans le monde de PythoLand Quest!\nVous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!\nVotre quête commence ici avec comme base {self.health} PV dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies.",
                                 fg="black", bg="white", font=("arial", 20))
        self.lbl_text.pack(expand=True, pady=20)

        #Affichage PV et ATT du joueur durant le jeu
        self.frm_box2 = tk.LabelFrame(self.int, text="Vos statistiques", bg="white", relief=tk.SUNKEN)
        self.frm_box2.place(relx=0, rely=0, relwidth=0.09, relheight=0.15)
        self.lbl_text2 = tk.Label(self.frm_box2,text=f"{self.health} PV\n{self.player_damage} ATT\nArme:{self.weapon}",fg="black", bg="white", font=("arial", 10))
        self.lbl_text2.pack(expand=True, pady=20)

    # Ecran de défaite quand PV = 0
    def death_screen(self):
        self.current_image = tk.PhotoImage(file="images/defeat.png")
        self.lbl_image.config(image=self.current_image)
        self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
        self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

    # Commande pour revenir au début pour recommencer après une défaite
    def restart_game(self):
        self.current_image = tk.PhotoImage(file="images/donjonstart.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
                text=f"Bienvenue dans le monde de PythoLand Quest!\nVous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!\nVotre quête commence ici avec comme base {self.health} PV dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies.",
                fg="black", bg="white", font=("arial", 20))
        self.btn_1.config(text="Chemin de Gauche", command=lambda: self.make_choice_1('gauche'))
        self.btn_2.config(text="Chemin de Droite", command=lambda: self.make_choice_1('droite'))

    # Commande pour quitter le jeu sur un bouton
    def quit_game(self):
        self.quit()

    def make_choice_1(self, choice):
        if choice == 'gauche':
            self.lbl_text.config(
                text="Vous avez choisi le chemin de gauche.\nPerdu dans la pénombre, vous tombez dans un piège qui vous tue instanément sans savoir ce que c'était...\nDéfaite...")
            self.current_image = tk.PhotoImage(file="images/defeat.png")
            self.lbl_image.config(image=self.current_image)

            #Bouton pour Rejouer du début ou pour quitter le jeu
            self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
            self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

        elif choice == 'droite':
            self.current_image = tk.PhotoImage(file="images/weaponchoice.png")
            self.lbl_image.config(image=self.current_image)
            self.lbl_text.config(
                text="Vous avez choisi le chemin de droite.\nVous sortez du donjon et voyez 2 armes au sol! Une Epée et une Massue\n Que faites-vous ?")
            self.btn_1.config(text="Epée (+10ATT et +10PV)", command=lambda: self.make_weapon_choice('Epée'))
            self.btn_2.config(text="Massue(+5ATT et +20PV)", command=lambda: self.make_weapon_choice('Massue'))

    def make_weapon_choice(self,choice):
        if choice == "Epée":
            self.weapon = "Epée"
            self.player_damage += 10
            self.health += 10
            self.lbl_text2.config(text=f"{self.health} PV\n{self.player_damage} ATT\nArme:{self.weapon}",
                                  fg="black", bg="white", font=("arial", 10))
            self.current_image = tk.PhotoImage(file="images/sword.png")
            self.lbl_image.config(image=self.current_image)
            self.lbl_text.config(text= "Vous avez choisi l'épée ! Bon choix\nVous gagnez +10PV et +10 ATT")
            self.btn_1.config(text="Continuer", command=lambda: self.first_fight())
            self.btn_2.config(text="Continuer", command=lambda: self.first_fight())

        elif choice == "Massue":
            self.weapon = "Massue"
            self.player_damage += 5
            self.health += 20
            self.lbl_text2.config(text=f"{self.health} PV\n{self.player_damage} ATT\nArme:{self.weapon}",
                                  fg="black", bg="white", font=("arial", 10))
            self.current_image = tk.PhotoImage(file="images/massue.png")
            self.lbl_image.config(image=self.current_image)
            self.lbl_text.config(text= "Vous avez choisi la massue ! Bon choix\nVous gagnez +20 PV et +5 ATT")
            self.btn_1.config(text="Continuer", command=lambda: self.first_fight())
            self.btn_2.config(text="Continuer", command=lambda: self.first_fight())

    def first_fight(self):
        self.current_image = tk.PhotoImage(file="images/first encounter.png")
        self.lbl_image.config(image=self.current_image)



# Créer et exécuter l'application
root = tk.Tk()
game = Game(root)
root.mainloop()