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

    # Ecran de défaite quand PV = 0
    def death_screen(self):
        self.current_image = tk.PhotoImage(file="images/defeat.png")
        self.lbl_image.config(image=self.current_image)
        self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
        self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

    # Commande pour quitter le jeu sur un bouton
    def quit_game(self):
        self.quit()

    #Commande pour revenir au début pour recommencer après une défaite
    def restart_game(self):
        self.current_image = tk.PhotoImage(file="images/donjonstart.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
                            text=f"Bienvenue dans le monde de PythoLand Quest!\nVous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!\nVotre quête commence ici avec comme base {self.health} PV dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies.",
                            fg="black", bg="white", font=("arial", 20))
        self.btn_1.config(text="Chemin de Gauche", command=lambda: self.make_choice_1('gauche'))
        self.btn_2.config(text="Chemin de Droite", command=lambda: self.make_choice_1('droite'))

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
            self.health += 20
            self.lbl_text.config(
                text=f"Après quelques heures de repose, vous vous réveillez en forme\nVous regagnez +20PV, Vous êtes à {self.health} PV !\nVous voyez sur la table près de vous, deux armes: Une épée ou une Massue\nLaquelle prenez-vous ?")
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
            self.weapon = "Epée"
            self.lbl_text.config(text=f"Vous avez choisi {self.weapon} !\n Très bon choix !")
            self.btn_1.config(text="Continuer", command=lambda: self.castle_zone())
            self.btn_2.config(text="Continuer", command=lambda: self.castle_zone())
            self.current_image = tk.PhotoImage(file="images/sword.png")
            self.lbl_image.config(image=self.current_image)
        elif choice == "Massue":
            self.weapon = "Massue"
            self.lbl_text.config(text=f"Vous avez choisi la {self.weapon}!\n Très bon choix !")
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
            text="Vous arrivez près de l'entrée du village proche du chateau mais un soldat gardant la porte vous interpelle...\n 'Quel est votre nom avant d'entrer ?'")
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
        self.lbl_text.config(text= f"Bievenu(e) {player_name} !\n Soldat: 'Vous pouvez rentrer à PythonVillage !'\n Que faites-vous ?")
        self.btn_1.config(text="Direction le chateau", command=lambda: self.castle_area())
        self.btn_2.config(text="Aller au bar", command=lambda: self.tavern_area())

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

    def castle_area(self):
        self.current_image = tk.PhotoImage(file="images/castle_entrance.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Vous entrez dans ce gigantesque chateau ! Mais...\n vous sentez des tremblements assez fort\n Vous décidez d'aller voir!")
        self.btn_1.config(text="Continuer", command=lambda: self.castle_fight())
        self.btn_2.config(text="Continuer", command=lambda: self.castle_fight())

    def castle_fight(self):
        self.current_image = tk.PhotoImage(file="images/castle_fight.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
            text="Vers la salle du trône, un massacre...\n Un Minotaure de très grande taille est au milieu de la salle entouré de cadave...\n Si vous voulez sauver les personnes restantes il faudra se battre !\nQue faites-vous ?")
        self.btn_1.config(text="SE BATTRE!", command=lambda: self.minotaur_fight())
        self.btn_2.config(text="S'enfuir", command=lambda: self.minotaur_end())

    def minotaur_fight(self):
        self.health -= 50
        self.current_image = tk.PhotoImage(file="images/minotaur_win.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text=f"Vous prenez votre {self.weapon} et partez à l'assaut du Minotaure déjà un peu affaibli par le peu de soldats restants...\n Après un combat long et dur, vous avec vaincu le Minotaure !\n Vous avez perdu 50PV, il vous reste {self.health} PV")
        self.btn_1.config(text="Continuer", command=lambda: self.victory_castle())
        self.btn_2.config(text="Continuer", command=lambda: self.victory_castle())

    def minotaur_end(self):
        self.current_image = tk.PhotoImage(file="images/defeat.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Vous décidez de vous enfuir en laissant les autres dans la mort mais...\nLe Minotaure, vous voyant vous enfuir, lance sa Hache vers vous sans manquer et vous tue sur le coup en vous déchiquetant en deux...\n Défaite...")
        self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
        self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

    def victory_castle(self):
        self.current_image = tk.PhotoImage(file="images/king_win.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Malheureusement, le Roi étant mort, le peuple est d'accord pour faire de vous le Roi de PythoVillage!!\nVous avez les épaules pour protéger cette cité!!\nFélicitations, vous avez réussi une fin!")
        self.btn_1.config(text="Rejouer pour avoir une autre fin ?", command=lambda: self.restart_game())
        self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

    def cave_zone(self):
        self.current_image = tk.PhotoImage(file="images/cave_zone.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Vous ignorez le village et décidez de continuer votre route\nVous entendez de forts bruit venant du village mais cela ne doit pas être bien important...\n Vous entrez dans une grotte magnifique, peut-être un trésor vous y attends!!")
        self.btn_1.config(text="Continuer", command=lambda: self.cave_area())
        self.btn_2.config(text="Continuer", command=lambda: self.cave_area())

    def cave_area(self):
        self.current_image = tk.PhotoImage(file="images/thief_camp.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Vous vous aventurez dans cette grotte...\nVous remarquez un camp déjà mis en place\nQui sont les personnes dedans ?")
        self.btn_1.config(text="Continuer", command=lambda: self.thief_camp())
        self.btn_2.config(text="Continuer", command=lambda: self.thief_camp())

    def thief_camp(self):
        self.current_image = tk.PhotoImage(file="images/thief attack.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Vous essayer de ne pas faire de bruit pour ne pas éveillez les soupçons...\nEn ayant presque traversé le camps en toute discrétions, vous sentez quelques chose derrière vous...\nVous vous retournez et voyez un voleur vous bandir dessus\nQue faites-vous ?")
        self.btn_1.config(text="Contrer son coup !", command=lambda: self.thief_attack())
        self.btn_2.config(text="Esquiver son coup !", command=lambda: self.thief_attack())

    def thief_attack(self):
        self.health -= 20
        self.current_image = tk.PhotoImage(file="images/thief_win.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text=f"Vous arrivez à abattre le voleur avec votre {self.weapon}\nVous avez perdu 20PV, il vous reste {self.health} PV")
        self.btn_1.config(text="Continuer", command=lambda: self.treasure_end())
        self.btn_2.config(text="Continuer", command=lambda: self.treasure_end())

    def treasure_end(self):
        self.current_image = tk.PhotoImage(file="images/treasure.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Après votre confrontation, vous arrivez dans leur salle aux trésors !\nFélicitation ! La richesse vous attends!")
        self.btn_1.config(text="Rejouer pour avoir une autre fin ?", command=lambda: self.restart_game())
        self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

# Créer et exécuter l'application
root = tk.Tk()
game = Game(root)
root.mainloop()
