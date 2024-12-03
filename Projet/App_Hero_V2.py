import tkinter as tk
import random

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

        # Stat Monstre
        self.monster_health = 20
        self.monster_damage = random.randint(5, 10)

        # Stat Minotaure
        self.minotaure_health = 50
        self.minotaure_damage = random.randint(10, 15)

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
        self.lbl_text2 = tk.Label(self.frm_box2,text=f"{self.health} PV\n{self.player_damage} ATT\nArme:{self.weapon}",fg="black", bg="white", font=("arial", 15, "bold"))
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

    def death_screen(self):
        self.health = 50
        self.current_image = tk.PhotoImage(file="images/defeat.png")
        self.lbl_image.config(image=self.current_image)
        self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
        self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

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
                                  fg="black", bg="white", font=("arial", 15, "bold"))
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
                                  fg="black", bg="white", font=("arial", 15, "bold"))
            self.current_image = tk.PhotoImage(file="images/massue.png")
            self.lbl_image.config(image=self.current_image)
            self.lbl_text.config(text= "Vous avez choisi la massue ! Bon choix\nVous gagnez +20 PV et +5 ATT")
            self.btn_1.config(text="Continuer", command=lambda: self.first_fight())
            self.btn_2.config(text="Continuer", command=lambda: self.first_fight())

    def first_fight(self):
        self.current_image = tk.PhotoImage(file="images/first encounter.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Vous rencontrez une silhouette hostile vers vous, un combat commence !\n Que faites-vous?")
        self.btn_1.config(text="Attaquer", command=lambda: self.fight_screen())
        self.btn_2.config(text="Fuir", command=lambda: self.road_choice())

    def fight_screen(self):
        self.current_image = tk.PhotoImage(file="images/fight.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text=f"Vous avez choisi d'attaquer !\nLe combat commence !\n Infos de l'adversaire: {self.monster_health} PV\nQue faites-vous ?")
        #Bouton durant le combat pour Attaquer ou Se Défendre
        self.btn_1.config(text="Attaquer", command=lambda: self.attack())
        self.btn_2.config(text="Se Défendre", command=lambda: self.defend())

    def attack(self):
        self.monster_health -= self.player_damage
        self.lbl_text.config(text=f"Vous attaquez !\nVous infligez {self.player_damage} de dégats\nIl vous inflige en retour {self.monster_damage} points de dégats\nPV du monstre restant: {self.monster_health}")
        if self.monster_health <= 0:
            self.lbl_text.config(text="Vous avez vaincu le monstre !")
            self.btn_1.config(text="Continuer", command=lambda: self.road_choice())
            self.btn_2.config(text="Continuer", command=lambda: self.road_choice())
        elif self.health <= 0:
            self.death_screen()
        else:
            self.monster_attack()

    def defend(self):
        self.health -= self.monster_damage - 5
        self.update_stats()
        if self.health <= 0:
            self.death_screen()
        else:
            self.lbl_text.config(text=f"Vous vous défendez! Réduisez les dégâts reçus.\nVos PV: {self.health}")
            self.btn_1.config(text="Attaquer", command=lambda: self.attack())
            self.btn_2.config(text="Se Défendre", command=lambda: self.defend())

    def monster_attack(self):
        self.health -= self.monster_damage
        self.update_stats()
        if self.health <= 0:
            self.restart_game()

    def update_stats(self):
        self.lbl_text2.config(text=f"{self.health} PV\n{self.player_damage} ATT\nArme:{self.weapon}")

    def road_choice(self):
        self.current_image = tk.PhotoImage(file="images/two_road.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Après cette confrontation, vous continuez votre chemin...\n vous remarquez deux chemins possibles:\nla première menant vers un donjon, la deuxième vers un chateau magnifique !\nQue faites-vous ?")
        self.btn_1.config(text="Direction le chateau", command=lambda: self.castle_area())
        self.btn_2.config(text="Partir vers une autre direction", command=lambda: self.cave_area())

    def castle_area(self):
        self.current_image = tk.PhotoImage(file="images/castle.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Vous arrivez près de l'entrée du du chateau du chateau mais un garde du chateau vous interpelle...\n 'Quel est votre nom avant d'entrer ?'")
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
        self.btn_2.config(text="Continuer", command=lambda: self.name_select())
    def name_select(self):
        global player_name
        player_name = self.name_choice.get()
        self.village_zone()

    def village_zone(self):
        global player_name
        self.name_choice.forget()
        self.health += 20
        self.update_stats()
        self.current_image = tk.PhotoImage(file="images/village_entrance.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text= f"Bievenu(e) {player_name} !\n Soldat: 'Vous pouvez rentrer à PythonCity !'\nVous vous reposez et récupérez 20 PV\nQue faites-vous ?")
        self.btn_1.config(text="Direction l'entrée du chateau", command=lambda: self.castle_fight())
        self.btn_2.config(text="Aller au bar", command=lambda: self.tavern_area())

    def castle_fight(self):
        self.current_image = tk.PhotoImage(file="images/castle_fight.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(
            text="Vers la salle du trône, un massacre...\n Un Minotaure de très grande taille est au milieu de la salle entouré de cadave...\n Si vous voulez sauver les personnes restantes il faudra se battre !\nQue faites-vous ?")
        self.btn_1.config(text="SE BATTRE!", command=lambda: self.minotaur_fight())
        self.btn_2.config(text="S'enfuir", command=lambda: self.minotaur_end())

    def minotaur_fight(self):
        self.current_image = tk.PhotoImage(file="images/minotaur_fight.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="X")

    def minotaur_end(self):
        self.current_image = tk.PhotoImage(file="images/defeat.png")
        self.lbl_image.config(image=self.current_image)
        self.lbl_text.config(text="Vous décidez de vous enfuir en laissant les autres dans la mort mais...\nLe Minotaure, vous voyant vous enfuir, lance sa Hache vers vous sans manquer et vous tue sur le coup en vous déchiquetant en deux...\n Défaite...")
        self.btn_1.config(text="Rejouer", command=lambda: self.restart_game())
        self.btn_2.config(text="Quitter le jeu", command=lambda: self.quit_game())

    def tavern_area(self):
        pass

    def cave_area(self):
        pass

# Créer et exécuter l'application
root = tk.Tk()
game = Game(root)
root.mainloop()