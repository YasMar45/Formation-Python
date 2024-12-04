import tkinter as tk
import random


def show_explication(self):
    self.ecran_explication = tk.Toplevel(self.parent)
    self.explication = ButJeu(self.ecran_explication)


def game_frame(self):
    self.ecran_jeu = tk.Toplevel(self.parent)
    self.jeu = Game(self.ecran_jeu)

class Menu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.parent.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
        self.parent.geometry(f"1920x1080")
        self.parent.resizable(True, True)

        # Frame principale
        self.int = tk.Frame(self.parent, bg='black')
        self.int.pack(fill=tk.BOTH, expand=True)

        # Frame pour l'image
        self.frame_image = tk.Frame(self.int, bg='grey')
        self.frame_image.place(relwidth=2 / 3, relheight=3 / 4)

        # Image au-dessus de la boîte de message
        self.current_image = tk.PhotoImage(
            file="images/elden_ring_projet_bg.png")
        self.lbl_image = tk.Label(self.frame_image, image=self.current_image)
        self.lbl_image.pack(expand=True)

        #Titre dans l'image
        self.lbl_title = tk.Label(self.lbl_image, text="PYTHONLAND QUEST", fg="red4", font=("arial", 70), relief=tk.RIDGE).place(x = 120, y = 150)

        # Frame Button pour les choix
        self.btn_frame = tk.Frame(self.int, bg='black')
        self.btn_frame.place(relx=2 / 3, relwidth=1 / 3, relheight=3 / 4)

        # Boutons pour les choix
        self.btn_1 = tk.Button(self.btn_frame, text="But du Jeu", command=lambda: self.show_explication())
        self.btn_1.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.btn_2 = tk.Button(self.btn_frame, text="Quitter le jeu", command=lambda: self.quit())
        self.btn_2.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        # Boîte de message en bas
        self.frm_box = tk.Button(self.int, text="Commencer votre aventure", bg="white", font=("arial", 75), relief="groove", command=lambda: self.game_frame())
        self.frm_box.place(rely=3 / 4, relwidth=1, relheight=1 / 4)

    def game_frame(self):
        self.ecran_jeu= tk.Toplevel(self.parent)
        self.jeu = Game(self.ecran_jeu)

    def show_explication(self):
        self.ecran_explication = tk.Toplevel(self.parent)
        self.but = ButJeu(self.ecran_explication)

class ButJeu(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.parent.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
        self.parent.geometry(f"1920x1080")
        self.parent.resizable(True, True)

        #Frame principale
        self.int = tk.Frame(self.parent, bg='black')
        self.int.pack(fill=tk.BOTH, expand=True)

        #Image Tuto
        self.current_image = tk.PhotoImage(
            file="images/beginnerlogo.png")
        self.lbl_image = tk.Label(self.int, image=self.current_image)
        self.lbl_image.pack(expand=True)

        # Zone de texte pour le But du jeu
        self.label = tk.Label(self.int,
                              text=f"Le but du jeu est de vous en sortir de vivant de votre péripétie dans PythonLand Quest selon vox choix !"
                                   f"\nQuand un choix vous sera demandé, vous devez entrer le numéro correspondant pour continuer et aussi appuyé sur Enter pour continuer l'intrigue\Vous commencez la partie avec comme base de 50 PV,"
                                   f"\nsi cela tombe à 0, vous avez perdu...\nMais Attention ! "
                                   f"Certains de vos choix vous seront bénéfiques comme un gain de points de vie tandis que d'autres vous nuieront comme une perte de vos points de vie ou la défaite directement! "
                              , bg="white", font=("arial", 15))
        self.label.place(x=50, y=400)

        # Bouton Retour
        tk.Button(self.int, text="Retour", fg="black", bg="seashell3", font=("arial", 50), command=lambda:self.parent.destroy()).place(x=840, y=900)

class Game(tk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.player_name = ""
        # Point de vie
        self.health = 50
        # Attaque du joueur
        self.player_damage = 0
        # Arme
        self.weapon = ''
        # Stat Monstre
        self.monster = "monstre"
        self.monster_health = 20
        self.monster_damage = 5

        self.parent = parent
        self.parent.title("PYTHONLAND QUEST - Projet de Formation - Margoum Yassine - 2024")
        self.parent.geometry(f"1920x1080")
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
                                 text=f"Bienvenue dans le monde de PythoLand Quest!\n"
                                      f"Vous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!\n"
                                      f"Votre quête commence ici avec comme base {self.health} PV sans arme dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies.",
                                 fg="black", bg="white", font=("arial", 20))
        self.lbl_text.pack(expand=True, pady=20)

        # Affichage PV et ATT du joueur durant le jeu
        self.frm_box2 = tk.LabelFrame(self.int, text="Vos statistiques", bg="white", relief=tk.SUNKEN)
        self.frm_box2.place(relx=0, rely=0, relwidth=0.09, relheight=0.15)
        self.lbl_text2 = tk.Label(self.frm_box2, text=f"{self.health} PV\n{self.player_damage} ATT\nArme:{self.weapon}",
                                  fg="black", bg="white", font=("arial", 15, "bold"))
        self.lbl_text2.pack(expand=True, pady=20)

        # Ce widget sera affiché dans une fenêtre spécifique au cours de la partie
        self.name_choice = tk.Entry(self.frm_box, width=30)

    # Fonction pour modifier une frame + rapidement (moins de ligne dans le code)
    def modify_screen(self, photo_path, text_label, text_button_1, text_button_2, function_button_1, function_button_2):
        self.current_image = tk.PhotoImage(file=photo_path)
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text=text_label)
        self.modify_buttons(text_button_1, text_button_2, function_button_1, function_button_2)

    def modify_buttons(self, text_button_1, text_button_2, function_button_1, function_button_2):
        self.btn_1.config(text=text_button_1, command=lambda: function_button_1())
        self.btn_2.config(text=text_button_2, command=lambda: function_button_2())

    # Ecran de défaite quand PV = 0
    def death_screen(self):
        self.health = 50
        self.update()
        self.current_image = tk.PhotoImage(file="images/defeat.png")
        self.lbl_image.config(image=self.current_image)
        self.modify_buttons("Rejouer", "Quitter le jeu", self.restart_game, self.quit)

    # Commande pour revenir au début pour recommencer après une défaite
    def restart_game(self):
        self.health = 50
        self.update()
        self.current_image = tk.PhotoImage(file="images/donjonstart.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
                text=f"Bienvenue dans le monde de PythoLand Quest!\nVous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!\nVotre quête commence ici avec comme base {self.health} PV dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies.",
                fg="black", bg="white", font=("arial", 20))
        self.btn_1.config(text="Chemin de Gauche", command=lambda: self.make_choice_1('gauche'))
        self.btn_2.config(text="Chemin de Droite", command=lambda: self.make_choice_1('droite'))

    def make_choice_1(self, choice):
        if choice == 'gauche':
            self.health -= 10
            self.update_stats()
            self.modify_screen("images/trap.png", "Vous avez choisi le chemin de gauche."
                                                 "\nPerdu dans la pénombre, vous tombez dans un piège qui vous blesse sans savoir ce que c'était..."
                                                 "\nVous perdez 10PV\nVous trouvez la sortie", "Continuer", "Continuer", self.first_fight, self.first_fight)

        elif choice == 'droite':
            self.current_image = tk.PhotoImage(file="images/weaponchoice.png")
            self.lbl_image.config(image=self.current_image)
            self.lbl_text.config(
                text="Vous avez choisi le chemin de droite.\nVous sortez du donjon et voyez 2 armes au sol! Une Epée et une Massue\n Que faites-vous ?")
            self.btn_1.config(text="Epée (+10ATT et +10PV)", command=lambda: self.make_weapon_choice('Epée'))
            self.btn_2.config(text="Massue(+5ATT et +20PV)", command=lambda: self.make_weapon_choice('Massue'))

    def make_weapon_choice(self,choice):
        self.health = 50
        self.update()
        if choice == "Epée":
            self.weapon = "Epée"
            self.player_damage += 10
            self.health += 10
            self.lbl_text2.config(text=f"{self.health} PV\n{self.player_damage} ATT\nArme:{self.weapon}",
                                  fg="black", bg="white", font=("arial", 15, "bold"))
            self.current_image = tk.PhotoImage(file="images/sword.png")
            self.lbl_image.config(image=self.current_image)
            self.lbl_text.config(text= "Vous avez choisi l'épée ! Bon choix\nVous gagnez +10PV et +10 ATT")
            self.btn_1.config(text="Continuer", command=lambda: self.first_fight())
            self.btn_2.config(text="Continuer", command=lambda: self.first_fight())

        elif choice == "Massue":
            self.weapon = "Massue"
            self.player_damage += 5
            self.health += 30
            self.lbl_text2.config(text=f"{self.health} PV\n{self.player_damage} ATT\nArme:{self.weapon}",
                                  fg="black", bg="white", font=("arial", 15, "bold"))
            self.current_image = tk.PhotoImage(file="images/massue.png")
            self.lbl_image.config(image=self.current_image)
            self.lbl_text.config(text= "Vous avez choisi la massue ! Bon choix\nVous gagnez +20 PV et +5 ATT")
            self.btn_1.config(text="Continuer", command=lambda: self.first_fight())
            self.btn_2.config(text="Continuer", command=lambda: self.first_fight())

    def first_fight(self):
        self.modify_screen("images/first encounter.png",
                          "Vous rencontrez une silhouette hostile qui fonce vers vous, un combat commence !\n Que faites-vous?",
                          "Attaquer", "Fuir", self.fight_screen, self.road_choice_screen)

    def fight_screen(self):
        self.modify_screen("images/fight.png", f"Vous avez choisi d'attaquer !\nLe combat commence !\n Infos de l'adversaire: {self.monster_health} PV\nQue faites-vous ?",
                          "Attaquer", "Se Défendre", self.attack, self.defend)

    def attack(self):
        self.monster_health -= self.player_damage
        self.lbl_text.config(text=f"Vous attaquez !\nVous infligez {self.player_damage} de dégâts\nIl vous inflige en retour {self.monster_damage} points de dégâts\nPV du monstre restant: {self.monster_health}")
        self.update_stats()
        if self.monster_health <= 0:
            self.lbl_text.config(text="Vous avez vaincu le monstre !")
            if self.monster == "monstre":
                self.modify_buttons("Continuer", "Continuer", self.road_choice_screen, self.road_choice_screen)
            if self.monster == "minotaure":
                self.btn_1.config(text="Continuer", command=lambda: self.minotaur_win_screen())
                self.btn_2.config(text="Continuer", command=lambda: self.minotaur_win_screen())
            if self.monster == "thief":
                self.modify_buttons("Continuer", "Continuer", self.treasure_end_screen, self.treasure_end_screen)

        else:
            self.health -= self.monster_damage + random.randint(0, 5)
            self.update_stats()
        if self.health <= 0:
            self.lbl_text.config(text="Vous avez perdu !\n Défaite...")
            self.death_screen()

    def defend(self):
        self.health -= self.monster_damage + random.randint(0, 5) - 5
        self.update_stats()
        if self.health <= 0:
            self.death_screen()
        else:
            self.lbl_text.config(text=f"Vous vous défendez! Réduisez les dégâts reçus.\nVos PV: {self.health}")
            self.btn_1.config(text="Attaquer", command=lambda: self.attack())
            self.btn_2.config(text="Se Défendre", command=lambda: self.defend())

    def update_stats(self):
        self.lbl_text2.config(text=f"{self.health} PV\n{self.player_damage} ATT\nArme:{self.weapon}")

    def road_choice_screen(self):
        self.modify_screen("images/two_road.png", "Après cette confrontation, vous continuez votre chemin...\n vous remarquez deux chemins possibles:"
                                                                       "\nla première menant vers un donjon, la deuxième vers un chateau magnifique !"
                                                                       "\nQue faites-vous ?", "Direction le chateau", "Partir vers une autre direction", self.castle_area_screen, self.cave_area_screen)

    def castle_area_screen(self):
        self.modify_screen("images/castle.png", "Vous arrivez près de l'entrée du du chateau du chateau mais un garde du chateau vous interpelle..."
                                               "\n 'Quel est votre nom avant d'entrer ?'", "Continuer", "Continuer", self.name_entry, self.name_entry)
    def name_entry(self):
        self.current_image = tk.PhotoImage(file="images/demandenom.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
            text="Entrez votre nom ici !:")
        self.name_choice.pack(pady=30)
        self.btn_1.config(text="Continuer", command=lambda: self.name_select())
        self.btn_2.config(text="Continuer", command=lambda: self.name_select())

    def name_select(self):
        self.player_name = self.name_choice.get()
        self.village_zone_screen()

    def village_zone_screen(self):
        self.name_choice.forget()
        self.health += 20
        self.update_stats()
        self.modify_screen("images/village_entrance.png", f"Bievenu(e) {self.player_name} !\n Soldat: 'Vous pouvez rentrer à PythonCity !'"
                                                         f"\nVous vous reposez et récupérez 20 PV\nQue faites-vous ?", "Direction l'entrée du chateau", "Direction Taverne de la ville",
                           self.castle_fight_screen, self.tavern_area_screen)

    def castle_fight_screen(self):
        self.modify_screen("images/castle_fight.png", "Vers la salle du trône, un massacre...\n Un Minotaure de très grande taille est au milieu de la salle entouré de cadavre..."
                                                     "\n Si vous voulez sauver les personnes restantes il faudra se battre !"
                                                     "\nQue faites-vous ?", "SE BATTRE!", "S'enfuir", self.minotaur_fight_screen, self.minotaur_end_screen)

    def minotaur_fight_screen(self):
        self.monster = "minotaure"
        self.monster_health = 50
        self.monster_damage = 10
        self.update_stats()
        self.modify_screen("images/minotaur_fight.png", "Le combat commence !\nD'autres soldats du chateau vous viennent en aide !\nInfos de l'adversaire: 50 PV"
                                                       "\nQue faites-vous ?", "Attaquer", "Se Défendre", self.attack, self.defend)

    def minotaur_win_screen(self):
        self.modify_screen("images/minotaur_win.png", f"Vous prenez votre {self.weapon} et partez à l'assaut du Minotaure déjà un peu affaibli par le peu de soldats restants...\n"
                                                     f"Après un combat long et dur, vous avec vaincu le Minotaure !", "Continuer", "Continuer", self.victory_castle_screen, self.victory_castle_screen)

    def victory_castle_screen(self):
        self.modify_screen("images/king_win.png", "Malheureusement, le Roi étant mort, le peuple est d'accord pour faire de vous le Roi de PythoVillage!!\nVous avez les épaules pour protéger cette cité!!"
                                                 "\nFélicitations, vous avez réussi une fin!", "Relancer pour avoir une autre fin", "Quittez le jeu", self.quit, self.quit)

    def minotaur_end_screen(self):
        self.modify_screen("images/defeat.png", "Vous décidez de vous enfuir en laissant les autres dans la mort mais..."
                                               "\nLe Minotaure, vous voyant vous enfuir, lance sa Hache vers vous sans manquer et vous tue sur le coup en vous déchiquetant en deux..."
                                               "\n Défaite...", "Rejouer", "Quitter le jeu", self.restart_game, self.quit)

    def tavern_area_screen(self):
        self.modify_screen("images/tavern.png", "Vous allez à la taverne de PythonCity boire un coup mais avec l'ambiance, cela va bien plus loin...'",
                          "Continuer", "Continuer", self.drunk_lose_screen, self.drunk_lose_screen)
    def drunk_lose_screen(self):
        self.weapon = ''
        self.player_damage = 0
        self.health = 10
        self.update_stats()
        self.modify_screen("images/defeat.png", "Après une bonne fête rempli d'alcool, vous vous réveillez au milieu du village sans vos équipements...\n"
                                               "Totalement dépouiller...\nDéfaite...", "Rejouer", "Quitter le jeu", self.restart_game, self.quit)

    def cave_area_screen(self):
        self.modify_screen("images/cave_zone.png", "Vous ignorez le village et décidez de continuer votre route\nVous entendez de forts bruit venant du village mais cela ne doit pas être bien important..."
                                                  "\n Vous entrez dans une grotte magnifique, peut-être un trésor vous y attends!!", "Continuer", "Continuer",
                           self.thief_camp_screen, self.thief_camp_screen)

    def thief_camp_screen(self):
        self.modify_screen("images/thief_camp.png", "Vous vous aventurez dans cette grotte...\nVous remarquez un camp déjà mis en place"
                                                   "\nQui sont les personnes dedans ?", "Continuer", "Continuer", self.thief_attack_screen, self.thief_attack_screen)

    def thief_attack_screen(self):
        self.modify_screen("images/thief_attack.png", "Vous essayer de ne pas faire de bruit pour ne pas éveillez les soupçons...\nEn ayant presque traversé le camps en toute discrétions, vous sentez quelques chose derrière vous..."
                                                     "\nVous vous retournez et voyez un voleur vous bandit dessus"
                                                     "\nQue faites-vous ?", "Contrer son coup", "Esquiver son coup", self.thief_fight, self.thief_fight)
    def thief_fight(self):
        self.monster = "thief"
        self.monster_health = 30
        self.monster_damage = 20
        self.update_stats()
        self.modify_screen("images/thief_attack.png", "Le combat commence !\nD'autres soldats du chateau vous viennent en aide !\nInfos de l'adversaire: 50 PV\nQue faites-vous ?",
                           "Attaquer", "Se Défendre", self.attack, self.defend)

    def thief_win_screen(self):
        self.modify_screen("images/thief_win.png", f"Vous arrivez à abattre le voleur avec votre {self.weapon}!\nFélicitation !", "Continuer", "Continuer", self.treasure_end_screen, self.treasure_end_screen)

    def treasure_end_screen(self):
        self.modify_screen("images/treasure.png", "Après votre confrontation, vous arrivez dans leur salle aux trésors !\nFélicitation ! La richesse vous attends!",
                          "Relancer pour avoir une autre fin", "Quitter le jeu", self.quit, self.quit)

# Créer et exécuter l'application
root = tk.Tk()
game = Menu(root)
root.mainloop()