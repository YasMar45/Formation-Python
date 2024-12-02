import tkinter as tk

import click
import orca.braille

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
                                 text="Bienvenue dans le monde de PythoLand Quest!\nVous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!\nVotre quête commence ici dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies.",
                                 fg="black", bg="white", font=("arial", 20))
        self.lbl_text.pack(expand=True, pady=20)

    # Commande pour quitter le jeu sur un bouton
    def quit_game(self):
        self.quit()

    #Commande pour revenir au début pour recommencer après une défaite
    def restart_game(self):
        self.current_image = tk.PhotoImage(file="images/donjonstart.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
                            text="Bienvenue dans le monde de PythoLand Quest!\nVous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!\nVotre quête commence ici dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies.",
                            fg="black", bg="white", font=("arial", 20))
        self.btn_1.config(text="Chemin de Gauche", command=lambda: self.make_choice_1('gauche'))
        self.btn_2.config(text="Chemin de Droite", command=lambda: self.make_choice_1('droite'))

    def make_choice_1(self, choice):
        if choice == 'gauche':
            self.lbl_text.config(
                text="Vous avez choisi le chemin de gauche.\nPerdu dans la pénombre, vous tombez dans un piège qui vous tue\nDéfaite")
            self.current_image = tk.PhotoImage(file="images/defeat.png")
            self.lbl_image.config(image=self.current_image)

            #Bouton pour Rejouer du début ou pour quitter le jeu
            self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
            self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())


        elif choice == 'droite':
            self.lbl_text.config(
                text="Vous avez choisi le chemin de droite.\nVous sortez du donjon et voyez une silhouette vous foncer dessus\n Que faites-vous ?")
            self.btn_1.config(text="Attaquer", command=lambda: self.make_choice_right('Attaquer'))
            self.btn_2.config(text="Fuir", command=lambda: self.make_choice_right('Fuir'))
            self.current_image = tk.PhotoImage(file="images/first encounter.png")
            self.lbl_image.config(image=self.current_image)

    def make_choice_right(self, choice):
        if choice == 'Attaquer':
            self.lbl_text.config(
                text="Vous avez choisi d'affronter le monstre.\nDéfaite")
            self.current_image = tk.PhotoImage(file="images/defeat.png")
            self.lbl_image.config(image=self.current_image)
            self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
            self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())
        elif choice == 'Fuir':
            self.lbl_text.config(
                text="Vous avez arrivé à semer la silhouette qui vous pourchassez.\nVous arrivez dans une auberge vide mais au moins vous pouvez prendre une pause durant la nuit\n Que faites-vous ?")
            self.current_image = tk.PhotoImage(file="images/auberge.png")
            self.lbl_image.config(image=self.current_image)
            self.btn_1.config(text="Se reposer", command=lambda: self.make_choice_inn('Se reposer'))
            self.btn_2.config(text="Continuer votre périple", command=lambda: self.make_choice_inn('Continuer votre périple'))

    def make_choice_inn(self, choice):
        if choice == 'Se reposer':
            self.lbl_text.config(
                text="Après quelques heures de repose, vous vous réveillez en forme\nVous voyez sur la table près de vous, deux armes: Une épée ou une Massue\nLaquelle prenez-vous ?")
            self.btn_1.config(text="Epée", command=lambda: self.make_choice_weapon('Epée'))
            self.btn_2.config(text="Massue", command=lambda: self.make_choice_weapon('Massue'))
            self.current_image = tk.PhotoImage(file="images/weaponchoice.png")
            self.lbl_image.config(image=self.current_image)

        elif choice == 'Continuer votre périple':
            self.lbl_text.config(
                text="Vous sortez à peine que quelques minutes dans la nuit.\n Que vous vous faites attaquer par une meute de loup enragée...\nDéfaite")
            self.current_image = tk.PhotoImage(file="images/defeat.png")
            self.lbl_image.config(image=self.current_image)
            self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
            self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

    def make_choice_weapon(self, choice):
        if choice == "Epée":
            self.lbl_text.config(text="Vous avez choisi l'épéé !\n Très bon choix !")
            self.btn_1.config(text="Continuer", command=lambda: self.castle_zone())
            self.btn_2.config(text="Continuer", command=lambda: self.castle_zone())
            self.current_image = tk.PhotoImage(file="images/sword.png")
            self.lbl_image.config(image=self.current_image)
        elif choice == "Massue":
            self.lbl_text.config(text="Vous avez choisi la Massue !\n Très bon choix !")
            self.btn_1.config(text="Continuer", command=lambda: self.castle_zone())
            self.btn_2.config(text="Continuer", command=lambda: self.castle_zone())
            self.current_image = tk.PhotoImage(file="images/massue.png")
            self.lbl_image.config(image=self.current_image)

    def castle_zone(self):
        self.current_image = tk.PhotoImage(file="images/castle.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
            text="Vous arrivez après quelques heures de marche devant un village mais sans manquer son énorme chateau au centre!\nQue faites-vous ?")
        self.btn_1.config(text="Entrer dans le village", command=lambda: self.village_zone())
        self.btn_2.config(text="Passer votre chemin", command=lambda: self.cave_zone())

    def village_zone(self):
        self.current_image = tk.PhotoImage(file="images/castle.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
            text="Vous arrivez proche des portes du village proche du chateau mais un soldat gardant la porte vous interpelle...\n 'Quel est votre nom avant d'entrer ?'")
        self.btn_1.config(text="Continuer", command=lambda: self.name_entry())
        self.btn_2.config(text="Continuer", command=lambda: self.name_entry())

    def name_entry(self):
        self.current_image = tk.PhotoImage(file="images/demandenom.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
            text="Entrez votre nom ici !:")
        self.name_choice = tk.Entry(self.frm_box, width=30)
        self.name_choice.pack(pady=30)
        self.btn_1.config(text="Continuer", command=lambda: self.name_select())
        self.btn_2.config(text="Continuer", command=lambda : self.name_select())

    def name_select(self):
        global player_name
        player_name = self.name_choice.get()
        self.village_zone_2()

    def village_zone_2(self):
        global player_name
        self.name_choice.forget()
        self.current_image = tk.PhotoImage(file="images/village_entrance.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text= f"Bievenu(e) {player_name} !\n Vous pouvez rentrer à PythonVillage !\n Que faites-vous ?")
        self.btn_1.config(text="Direction le chateau", command=lambda: self.castle_area())
        self.btn_2.config(text="Aller au bar", command=lambda: self.tavern_area())

    def castle_area(self):
        pass

    def tavern_area(self):
        self.current_image = tk.PhotoImage(file="images/tavern.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Vous allez au bar boire un coup mais avec l'ambiance, cela va bien plus loin...")
        self.btn_1.config(text="Continuer", command=lambda: self.drunk_lose())
        self.btn_2.config(text="Continuer", command=lambda: self.drunk_lose())

    def drunk_lose(self):
        self.current_image = tk.PhotoImage(file="images/defeat.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Après une bonne fête rempli d'alcool, vous vous réveillez au milieu du village sans vos équipement...\nDéfaite...")
        self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
        self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

    def cave_zone(self):
        pass

# Créer et exécuter l'application
root = tk.Tk()
game = Game(root)
root.mainloop()





