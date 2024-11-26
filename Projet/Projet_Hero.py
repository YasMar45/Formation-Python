import time
import sys
import json

#Fonction pour les textes qui defilent lentemenet
def slow_print(text, delay=0):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

#Variable des points de vie
player_health = 100
player_name = ''
weapon_choice = ''
player_weapon = ''

#fonction pour voir les points de vie du joueur
def check_health():
    global player_health
    if player_health <= 0:
        slow_print ("Défaite...")
        slow_print("Retour au menu principal")
        game_menu()

#Menu du jeu
def game_menu():
    print("PYTHONLAND QUEST")
    print('1.Commencez votre aventure !\n2.Explication du Jeu\n3.Quittez le jeu')
    option = input('Entrer votre choix:')

    if option == '1':
        start_game()
    elif option == '2':
        help_menu()
    elif option == '3':
        print('Fermeture du Jeu!')
        sys.exit()
    while option not in ['1', '2', '3']:
        print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        game_menu()

#Help_menu Explication
def help_menu():
    slow_print('Le but du jeu est de vous en sortir de vivant de votre péripétie dans PythonLand Quest selon vox choix !')
    slow_print(f'Vous commencez la partie avec comme base {player_health} PV,si cela tombe à 0, vous avez perdu...')
    slow_print(f"Mais Attention ! Certains de vos choix vous seront bénéfiques tandis que d'autres vous nuieront comme une perte de vos points de vie ou la défaite directement! ")
    game_menu()

#Introduction + Nom
def start_game():
    global player_name
    slow_print('Bievenu(e) dans le monde de PythoLand Quest!')
    slow_print('Vous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!')
    slow_print('Votre quête commence ici dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies')
    slow_print('Faites attention ! Il faudra vous remplir de courage et y aller pour vous en sortir vivant,cela ne va pas être facile!')
    slow_print('Vos choix vous meneront vers la victoire mais aussi très souvent vers la défaite, Bonne chance...')
    slow_print('Mais avant tout quel est ton nom qui va "peut-être rentrer dans la légende...')
    player_name = input('Entrez votre nom:')
    slow_print(f'Très bien {player_name}, votre aventure commence dès maintenant,bonne chance...')
    dungeon_start()

#Commencement réel du jeu avec le début dans la cellule
def dungeon_start():
    global weapon_choice
    global player_weapon
    slow_print(f'{player_name}, vous vous revéillez dans cette cellule humide et immonde, juste quelques bougies vous éclaire...')
    slow_print(f'Vous avez un mal de crâne comme si on vous avez frappé auparavant très fort dessus')
    slow_print(f'Vous vous levez et appercevez le couloir qui découle de votre cellule...')
    slow_print(f'Vous voyez plein de cadavres au sol, il y a eu un combat très violent ici il y a peu de temps...')
    slow_print(f"Au sol. 3 armes sont devant vous mais une seule pourra être portée,laquelle choissisez vous ?")
    print(f"1.L'épee et Bouclier\n2.Les doubles Dagues'\n3.La Massue")
    weapon_choice = input(f"Veuillez choisir le chiffre pour votre arme de prédilection:")
    if weapon_choice == "1":
        player_weapon = "L'épee et Bouclier"
        slow_print(f'Vous avez ramassé {player_weapon}')
        first_encounter()
    elif weapon_choice == "2":
        player_weapon = 'Les doubles Dagues'
        slow_print(f'Vous avez ramassé {player_weapon}')
        first_encounter()
    elif weapon_choice == "3":
        player_weapon = 'La Massue'
        slow_print(f'Vous avez ramassé {player_weapon}')
        first_encounter()

#Première rencontre et choix !
def first_encounter():
    global player_weapon
    global player_health
    slow_print(f'Après avoir ramassé {player_weapon}, vous vous aventuré dans le donjon en ayant pour but de chercher une sortie...')
    slow_print(f"Vous remarquez une faisceau lumineux au loin, on dirait bien que c'est la sortie!")
    slow_print(f"Mais... On dirait qu'une silhouette de dos garde cette sortie... Vous pouvez aussi apercevoir une crevasse sur le coté mais où cela va vous amenez ?")
    slow_print(f"Que faites-vous, la solution de la force ou de la sûreté ?!")
    choice = input(f"1.Attaquez la silhouette par surprise tant qu'elle est dos à vous !!\n2.Vous faufilez dans dans la crevasse pour éviter le combat\nVotre choix:")
    if choice == '1':
        slow_print(f"À l'approche de la silhouette avec {player_weapon}, vous être prêt à lui asséner un coup mortel par surprise !")
        if player_weapon == "L'épee et Bouclier":
            player_health -= 10
            slow_print(f"Vous prenez fermement votre épée pour lui trancher la gorge par derrière! Mais il a le temps de se retourner pour vous asséner un grand coup de poing dans votre bouclier qui a été levé juste avant ! Il succombe peu de temps après fait son coup de poing")
            slow_print(f"Vous avez été projeté avec la force brute de l'adversaire vers le mur,vous perdez 10 PV, il vous reste {player_health} PV")
            slow_print(f"Après vous êtes remis de cette confrontation, il est tant de sortir de ce donjon, l'extèrieur vous attend!")
            out_dungeon()
        elif player_weapon == 'Les doubles Dagues':
            player_health -= 30
            slow_print("Vous sautez sur la silhouette avec vos deux dagues prêt à lui asséner plusieurs coups partout dans le corps!\nAccrochez à son dos en lui mettant plein de coup de dague, vous sentez qu'il s'affaiblit mais il a le temps de vous faire tomber de son dos et vous infligez un grand coup de poing dans le ventre qui vous projette")
            slow_print(f"Vous avez été projeté avec la force brute de l'adversaire vers le mur,vous perdez 30 PV, il vous reste {player_health} PV, heureusement qu'il était affaibli grâce aux différent coup que vous lui avez asséné...")
            slow_print(f"Après vous êtes remis de cette confrontation, il est tant de sortir de ce donjon, l'extèrieur vous attend!")
            out_dungeon()
        elif player_weapon == "La Massue":
            slow_print(f"Avec votre Massue chargée et prêt à lui mettre un coup mortel ! Il n'a pas eu le temps de réagir que vous avec pu l'écraser au sol sans broncher !")
            slow_print(f"Après vous êtes remis de cette confrontation, il est tant de sortir de ce donjon, l'extèrieur vous attend!")
            out_dungeon()

    elif choice == '2':
        slow_print(f"Vous décidez de prendre la crevasse pour éviter la silhouette, risque zéro, après quelques complications, vous ressentez de l'air frais et une source de lumières au bout!")
        out_dungeon()

#Sortie du donjon, petit blabla
def out_dungeon():
    slow_print(f"Vous vous en sortez de ce donjon par vos moyens ou votre courage! Après avoir enfin respiré le bon air frais ! Il est tant d'avancer pour votre survie !")
    slow_print(f"Après quelques minutes de marche à votre aise, vous vous retrouvez devant deux sentier avec entre les deux une géante fissure béante...")
    slow_print(f"Il va falloir faire un choix qui sera conséquent dans votre aventure!")
    choice = input(f"1.À GAUCHE où on peut entendre divers bruit mais surtout une forêt assez dense de ce coté-ci?\n2.À DROITE cela donne vers quelques collines rocheuses avec comme repère de la fumée qui peut annoncer un feu de camp donc peut-être des personnes!\nEntrez votre choix ici:")
    if choice == '1':
        slow_print('Vous décidez de prendre le chemin de gauche...')
        left_path()
    elif choice == '2':
        slow_print('Vous décidez de prendre le chemin de droite...')
        right_path()

#Chemin de Gauche !
def left_path():
    slow_print(f"x")
    strange_sound()

#Bruit étrange choix ignorer ou aller vers le bruit
def strange_sound():
    pass

#Chemin de Droite !
def right_path():
    pass

#Lancement du jeu
game_menu()