import time
import sys
from tkinter import *

#Fonction pour les textes qui defilent lentemenet
def slow_print(text, delay=0.1):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

#Variable des points de vie
player_health = 50
max_player_health = 100
player_name = ''
weapon_choice = ''
player_weapon = ''

#Mécanique de Points de vie
def health_meca():
    global player_health
    global max_player_health
    if player_health > max_player_health:
        player_health = max_player_health
        print("Vous êtes au maximum de PV possible!")

#Si PV arrive à 0, Défaite
def check_health():
    global player_health
    if player_health <= 0:
        slow_print ("Mais...")
        slow_print("Vous succombez de vos blessures,Défaite...")
        slow_print("Retour au menu principal")
        game_menu()

#Menu du jeu
def game_menu():
    print("PYTHONLAND QUEST")
    print('1.Commencez votre aventure !\n2.Explication et But du Jeu\n3.Quittez le jeu')
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

#help_menu Explication
def help_menu():
    slow_print('Le but du jeu est de vous en sortir de vivant de votre péripétie dans PythonLand Quest selon vox choix !')
    slow_print("Quand un choix vous sera demandé, vous devez entrer le numéro correspondant pour continuer et aussi appuyé sur Enter pour continuer l'intrigue")
    slow_print(f'Vous commencez la partie avec comme base de {player_health} PV,si cela tombe à 0, vous avez perdu...')
    slow_print(f"Mais Attention ! Certains de vos choix vous seront bénéfiques comme un gain de points de vie tandis que d'autres vous nuieront comme une perte de vos points de vie ou la défaite directement! ")
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
    global player_health
    player_health = 50
    slow_print(f'{player_name}, Vous vous revéillez dans cette cellule humide et immonde, juste quelques bougies vous éclaire....')
    slow_print(f'Vous avez un mal de crâne comme si on vous avez frappé auparavant très fort dessus')
    slow_print(f'Vous commencez avec {player_health} PV!')
    input(f"Appuyez sur Enter pour continuer")
    slow_print(f'Vous vous levez et apercevez le couloir qui découle de votre cellule...')
    slow_print(f'Vous voyez plein de cadavres au sol, il y a eu un combat très violent ici il y a peu de temps...')
    input(f"Appuyer sur Enter pour continuer")
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
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        dungeon_start()

#Première rencontre et choix !
def first_encounter():
    global player_weapon
    global player_health
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f'Après avoir ramassé {player_weapon}, vous vous aventuré dans le donjon en ayant pour but de chercher une sortie en premier temps...')
    input(f"Appuyer sur Enter pour continer")
    slow_print(f"Vous remarquez une faisceau lumineux au loin, on dirait bien que c'est la sortie!")
    slow_print(f"Mais... On dirait qu'une silhouette de dos garde cette sortie... Vous pouvez aussi apercevoir une crevasse sur le coté mais où cela va vous amenez ?")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Que faites-vous, la solution de la force ou de la sûreté ?!")
    choice = input(f"1.Attaquez la silhouette par surprise tant qu'elle est dos à vous !!\n2.Vous faufilez dans dans la crevasse pour éviter le combat\nVotre choix:")
    if choice == '1':
        slow_print(f"À l'approche de la silhouette avec {player_weapon}, vous être prêt à lui asséner un coup mortel par surprise !")
        if player_weapon == "L'épee et Bouclier":
            player_health -= 10
            slow_print(f"Vous prenez fermement votre épée pour lui trancher la gorge par derrière! Mais il a le temps de se retourner pour vous asséner un grand coup de poing dans votre bouclier qui a été levé juste avant ! Il succombe peu de temps après fait son coup de poing")
            input(f"Appuyer sur Enter pour continuer")
            slow_print(f"Vous avez été projeté avec la force brute de l'adversaire vers le mur,vous perdez 10 PV")
            check_health()
            slow_print(f"il vous reste {player_health} PV")
            slow_print(f"Après vous êtes remis de cette confrontation, il est tant de sortir de ce donjon, l'extèrieur vous attend!")
            out_dungeon()
        elif player_weapon == 'Les doubles Dagues':
            player_health -= 30
            slow_print("Vous sautez sur la silhouette avec vos deux dagues prêt à lui asséner plusieurs coups partout dans le corps!\nAccrochez à son dos en lui mettant plein de coup de dague, vous sentez qu'il s'affaiblit mais il a le temps de vous faire tomber de son dos et vous infligez un grand coup de poing dans le ventre qui vous projette")
            input(f"Appuyer sur Enter pour continuer")
            slow_print(f"Vous avez été projeté avec la force brute de l'adversaire vers le mur,vous perdez 30 PV'")
            check_health()
            slow_print(f"il vous reste {player_health} PV, heureusement qu'il était affaibli grâce aux différent coup que vous lui avez asséné...")
            input(f"Appuyer sur Enter pour continuer")
            slow_print(f"Après vous êtes remis de cette confrontation, il est tant de sortir de ce donjon, l'extèrieur vous attend!")
            out_dungeon()
        elif player_weapon == "La Massue":
            slow_print(f"Avec votre Massue chargée et prêt à lui mettre un coup mortel ! Il n'a pas eu le temps de réagir que vous avec pu l'écraser au sol sans broncher !")
            input(f"Appuyer sur Enter pour continuer")
            slow_print(f"Après vous êtes remis de cette confrontation, il est tant de sortir de ce donjon, l'extèrieur vous attend!")
            out_dungeon()
        else:
            slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
            first_encounter()

    elif choice == '2':
        slow_print(f"Vous décidez de prendre la crevasse pour éviter la silhouette, risque zéro, après quelques complications, vous ressentez de l'air frais et une source de lumières au bout!")
        out_dungeon()
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        first_encounter()

#Sortie du donjon, petit blabla
def out_dungeon():
    slow_print(f"Vous vous en sortez de ce donjon par vos moyens ou votre courage! Après avoir enfin respiré le bon air frais ! Il est tant d'avancer pour votre survie !")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Après quelques minutes de marche à votre aise, vous vous retrouvez devant deux sentier avec entre les deux une géante fissure béante...")
    slow_print(f"Il va falloir faire un choix qui sera conséquent dans votre aventure!")
    choice = input(f"1.À GAUCHE où on peut entendre divers bruit mais surtout une forêt assez dense de ce coté-ci?\n2.À DROITE cela donne vers quelques collines rocheuses avec comme repère de la fumée qui peut annoncer un feu de camp donc peut-être des personnes!\nEntrez votre choix ici:")
    if choice == '1':
        slow_print('Vous décidez de prendre le chemin de gauche...')
        left_path()
    elif choice == '2':
        slow_print('Vous décidez de prendre le chemin de droite...')
        right_path()
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        out_dungeon()

#Chemin de Gauche !
def left_path():
    slow_print(f"Après quelques heures de marche dans ce sentier avec de quoi vous nourrir avec des fruits et boire de l'eau grâce à une jolie rivière qui se trouve pas trop loin!")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Soudainement, vous entendez et sentez des mouvements rapides près de vous!")
    input(f"Appuyer sur Enter pour continuer")
    strange_sound()

#Bruit étrange choix ignorer ou aller vers le bruit
def strange_sound():
    global player_health
    slow_print(f"Maintenant vous entendez des bruits venant d'un buisson près de vous, allez-vous ignorer cela ou aller voir par curiosité ce qu'il se trame?\n1.Check le buisson!\n2.Ignorer")
    choice = input(f"Entrez votre choix ici:")
    if choice == "1":
        player_health -= 1
        slow_print(f"Un écureuil vous saute au visage et vous griffe la joue, vous perdez 1 PV")
        check_health()
        slow_print(f"il vous reste {player_health} PV")
        input(f"Appuyer sur Enter pour continuer")
        in_village()
    elif choice == "2":
        slow_print(f"Vous décidez d'ignorer ce qu'il se passe dans le buisson, vous continuez votre chemin!")
        input(f"Appuyer sur Enter pour continuer")
        in_village()
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        strange_sound()

#Entrer au village!
def in_village():
    global player_health
    slow_print(f'Le soir,après des heures de marches, vous apercevez au loin des lumières, vous vous approchez et vous remarquez que vus êtes arrivé à un village du nom de "Json Village"')
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"C'est très animé comme c'était un jour de fête mais vous avez une rude journée, vous méritez du repos ou...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Vous pouvez participer à la fête avec les habitants pour boire un bon coup et vous amusez!")
    choice = input(f"1.Aller à l'auberge vous reposer de ce périple\n2.Aller participer à la fête !!\nQue faites-vous, entrez votre choix ici:")
    if choice == '1':
        player_health += 20
        slow_print(f"Vous décidez d'aller vous reposer à l'auberge,vous le méritez après un réveil brutal dans une cellule caché dans un donjon!")
        slow_print(f"Vous récupérez 20 PV")
        check_health()
        slow_print(f"il vous reste {player_health} PV")
        undead_attack()
    elif choice == '2':
        player_health -= 10
        slow_print(f"Vous passez la nuit à boire et faire la fête, ça vous fais un grand bien cependant...")
        slow_print(f"Une bagarre générale se lance sans que vous savez pourquoi ni comment,vous prenez des coups gratuits et tombez dans les pommes dû à l'ivresse et le choc...")
        slow_print(f"Vous avez perdu 10 PV")
        check_health()
        slow_print(f"il vous reste {player_health} PV")
        undead_attack()
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        in_village()

#Attaque de Zombie
def undead_attack():
    global player_health
    slow_print(f"De lourds cris vous réveille de votre profond sommeil,vous sentez des secousses de partout comme si le village allait se retourner d'un moment ou un autre!")
    slow_print(f"Vous ouvrez grand vos yeux et vous voyer une invasion de mort-vivant attaquer le village...")
    slow_print(f"Que faites-vous ?\n1.Aider le village contre l'invasion de zombie ?\n2.S'enfuir !")
    choice = input(f"Entrez votre choix ici:")
    if choice == '1':
        player_health -= 10
        slow_print(f"Vous prenez votre arme et partez à l'assaut de la horde de mort-vivant!")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Votre motivation se propage dans le village, la population prend ce qu'ils peuvent pour vous aider à repousser l'envahisseur!")
        slow_print(f"Vous perdez 10 PV seulement grâce au soutien du village à vos coté !")
        check_health()
        slow_print(f"Il vous reste {player_health} PV")
        win_village()
    elif choice == '2':
        player_health -= 100
        slow_print(f"Vous décidez de ne pas aider le village et de vous enfuir mais en courant de toute vos forces...")
        slow_print(f"Une horde de mort-vivant vous attrape et vous déchique sur place... Peut-être qu'avec l'aide du village, ça aurait pu mieux se passer...")
        check_health()
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        undead_attack()

#Fin dans le village
def win_village():
    slow_print(f"Vous avez triomphé de la horde de mort-vivant toute la nuit avec le village, il y a eu des pertes mais au moins le village a été sauvé!")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Après des journées à remettre le village dans l'ordre et soigner les blessés, vous sentez quelque chose de particulier...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Comme si ce village était fait pour vous,peut-être songé à y rester pour le chérir et le protéger de toutes les menaces possible ?")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Que voulez-vous faire ?\n1.Repartir à l'aventure vers l'inconnu\n2.Rester au village")
    choice = input("Entrer votre choix ici:")
    if choice == "1":
        slow_print('Vous décidez de partir du village après les efforts donnés, les habitants vous disent "au revoir" en pleur...')
        print('à suivre...')
        game_menu()
    elif choice == "2":
        slow_print(f"Vous décidez de faire votre vie dans ce village !")
        slow_print(f"Qu'elles seront les prochaines menaces à venir ? à suivre...")
        slow_print("Félicitations, vous avez atteins une des fins ! Réessayer pour découvrir les autres fin possible!")
        game_menu()
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        win_village()

#Chemin de Droite !
def right_path():
    global player_health
    slow_print(f"Après quelques minutes de marche sur le chemin de droite vers cette fumée que l'on avait vu au loin")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Vous apercevez une cabane avec une cheminée, ça venait donc de la fumée au loin, il y a écrit près de la porte")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"'Maison de repos pour les aventuriers',c'est bon signe pour marquer un repos pour la journée!")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Vous décidez donc de dormir après cette longue route...")
    input(f"Appuyer sur Enter pour continuer")
    player_health += 20
    slow_print("Vous regagnez 20 PV")
    check_health()
    slow_print(f"Vous êtes à {player_health} PV")
    thief_coming()


#Arrivé des bandits choix
def thief_coming():
    global player_health
    slow_print(f"Votre instinct vous réveille, vous entendez des pas vers l'extérieur qui se rapproche...")
    input(f"Appuyer sur Enter pour continer")
    slow_print(f"Vous apercevez que ce sont des bandis qui rôdent à la recherche de trésor ou de personne à piller")
    slow_print(f"Ils sont une dizaine,ça sera difficile de les battre à vous tout seul...\nQu'allez vous faire ?")
    input(f"Appuyer sur Enter pour continer")
    choice = input("1.Se cacher et rester silencieux\n2.Les attaquer!\nEntrer votre choix ici:")
    if choice == "1":
        slow_print(f"Vous restez silencieux caché sous le lit de la cabane...")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Vous entendez les bandits rentrer dans la foyer, les pas sont nombreux, si vous aviez tenté de les attaquer, c'était du suicide...")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Après quelques minutes caché sous le lit, les pas se font moins bruyants, ça serait une bonne idée de les suivre!")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Vous sortez de la cabane en gardant une distance avec les bandits mais surtout rester le plus silencieux possible...")
        thief_base()
    elif choice == "2":
        player_health -= 100
        slow_print("Vous décidez d'attaquer la troupe de bandit directement...")
        slow_print("à peine avoir abattu un bandit que les autres vous sautent dessus, d'autres bandits arrivent, ils sont trop nombreux...")
        input(f"Appuyer sur Enter pour continuer")
        check_health()
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        thief_coming()

#Attaque de la base des bandits ou ne pas tenter donc aller au village
def thief_base():
    global player_health
    slow_print(f"En suivant les bandits durant une bonne petite heure, vous apercevez un semblant de camp pour eux")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Vous remarquez qu'il se prépare pour entrer dans une grotte où le camp est basé")
    input(f"Vous attendez un bon moment et une dizaine de bandits rentre dans cette grotte!")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"C'est le moment d'attaquer stratègiquement leur camp vu que leur nombre a été réduit!")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Que faites-vous ?\n1.Profiter de l'opportunité et attaquer le camp des bandits!\n2.Ne rien tenter et vous enfuir sur le sentier le plus proche!")
    choice = input(f"Entrez votre choix ici:")
    if choice == "1":
        player_health -= 10
        slow_print(f"Vous profitez de l'occasion pour attaquer les bandits!")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Vous en achevez un directement depuis son dos, les bandits sont pris par surprise!")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Après plusieurs minutes d'acharnements, vous triomphez des bandits non préparés à votre attaque")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Vous avez prit quand même quelques coups, vous avez perdu 10 PV sur ce combat !")
        slow_print(f"Vous êtes à {player_health} PV")
        check_health()
        minotaur_fight()
    elif choice == "2":
        slow_print(f"Vous ne tentez rien de dangereux même le nombre est réduit !")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Vous prenez et suivez un sentier qui même vers l'inconnue...")
        in_village()
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        thief_base()

def minotaur_fight():
    global player_health
    slow_print(f"Après avoir pris d'assaut le camp de bandit, vous décidez d'aller voir ce qu'il se passe dans cette grotte pour qu'il envoie beaucoup de gens...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Vous entrez dans la grotte...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Vous avez pris une lanterne qui trainée pour pouvoir vous déplacez sans soucis dans cette profonde grotte")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"En avançant prudemment, vous commencez à entendre des cris au loins et des bruits qui ne sont pas lieu d'être dans une grotte normalement...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print("Vous apercevez de la lumière naturelle au loin\nVous foncez pour voir ce qu'il se passe et c'est un carnage...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Vous arrivez dans un sorte de temple aménagé dans cette grotte mais surtout tout les bandits massacrés ou déchiqueter...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Au loin, vous voyez une forme peu commune, ce n'est pas humain...\nvous remarquez qu'il y a une morphologie peu commune...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Son corps étant celui d'un taureau mais aussi d'un humain avec une tête de taureau mais surtout sa taille gigantesque, il doit bien faire au moins 3 METRES...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Pas le temps de réfléchir...\nQUE FAITES-VOUS ?!")
    choice = input(f"1.Essayer de confronter le MINOTAURE, peut être affaibli pas les bandits?\n2.Pendant qu'il est encore de dos, essayez de trouver un autre chemin!\nEntrer votre choix ici:")
    if choice == "1":
        player_health -= 30
        slow_print(f"Vous vous jetez sur le minotaure tant qu'il est de dos et l'asséner de coup avec {player_weapon}...")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Le minotaure est surpris de votre arrivé, il prend plusieurs coup mais il vous en donne aussi, c'est un combat sensationel")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Vous arrivez à remporter le combat de justesse, vous avez perdu 30PV...")
        slow_print(f"il vous reste {player_health} PV")
        check_health()
        input(f"Appuyer sur Enter pour continuer")
        treasure_end()
    elif choice == "2":
        player_health -= 50
        slow_print("Vous décidez d'éviter la confrontation avec le Minotaure!")
        input(f"Appuyer sur Enter pour continuer")
        slow_print("Vous cherchez une autre issues dans ce grand temple souterrain, vous remarquez une fissure assez large pour passer...")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"C'est compliqué mais vous avancez petit à petit, mais...")
        input(f"Appuyer sur Enter pour continuer")
        slow_print(f"Vous déclenchez un piège en vous aventurant dans cette fissure, le mur vous projette avec une force gigantesque en dehors de la fissure dans une grande salle")
        slow_print(f"Vous perdez 50 PV dù au coup et la chute")
        check_health()
        slow_print(f"il vous reste {player_health} PV")
        input(f"Appuyer sur Enter pour continuer")
        treasure_end()
    else:
        slow_print(f"Entrée incorrecte ou invalide. Veuillez Réessayer!")
        minotaur_fight()

def treasure_end():
    slow_print(f"Après avoir évité le pire et avoir survécu, vous avancez dans ce temple souterrain...")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Vous trouvez une salle avec une grande porte, à votre avis, c'est bien ce que cherché les bandits de base!")
    input(f"Appuyer sur Enter pour continuer")
    slow_print(f"Vous entrez dans une salle resplendissante avec en son centre un coffre serti d'or de partout\nVous méritez son contenu pour votre périple, pleins d'or et de bijours s'y trouve!")
    input(f"Appuyer sur Enter pour continuer")
    slow_print("Félicitations, vous avez atteins une des fins ! Réessayer pour découvrir les autres fin possible!")
    game_menu()

#Lancement du jeu
game_menu()