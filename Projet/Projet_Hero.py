import time
import sys
import pygame

#Fonction pour les textes qui defilent lentemenet
def slow_print(text, delay=0.035):
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()

#Variable des points de vie
player_health = 100

#fonction pour voir les points de vie du joueur
def check_health():
    global player_health
    if player_health <= 0:
        slow_print ("Défaite...")

#Menu du jeu
def game_menu():
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
        print('1.Commencez votre aventure !\n2.Explication du Jeu\n3.Quittez le jeu')
        if option == '1':
            start_game()
        elif option == '2':
            help_menu()
        elif option == '3':
            print('Fermeture du Jeu!')
            sys.exit()

#Help_menu Explication
def help_menu():
    slow_print('Le but du jeu est de vous en sortir de vivant de votre péripétie selon vox choix !')
    slow_print(f'Vous commencez la partie avec comme base {player_health} PV,si cela tombe à 0, vous avez perdu...')
    slow_print(f"Mais Attention ! Certains de vos choix vous seront bénéfiques tandis que d'autres vous nuieront comme une perte de vos points de vie ou la défaite directement! ")
    game_menu()

#Introduction + Nom
def start_game():
    slow_print('Bievenu(e) dans le monde de PythoLand Quest!')
    slow_print('Vous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!')
    slow_print('Votre quête commence ici dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies')
    slow_print('Faites attention ! Il faudra vous remplir de courage et y aller pour vous en sortir vivant,cela ne va pas être facile!')
    slow_print('Vos choix vous meneront vers la victoire mais aussi très souvent vers la défaite, Bonne chance...')
    slow_print('Mais avant tout quel est ton nom qui va "peut-être rentrer dans la légende...')
    player_name = input('Entrez votre nom:')
    slow_print(f'Très bien {player_name}, votre aventure commence dès maintenant,bonne chance...')
    dungeon_start()

def dungeon_start():
    pass

#Lancement du jeu
game_menu()