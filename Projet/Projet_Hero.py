import time
import sys
import pygame

#Fonction pour les textes qui defilent lentemenet
def slow_print(text, delay=0.05):
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
    print('1.Commencez votre aventure !\n2.Quittez le jeu')
    option = input('Entrer votre choix:')

    if option == '1':
        start_game()
    if option == '2':
        sys.exit()
    while option not in ['1', '2']:
        option = input('Entrer votre choix:')
        if option == '1':
            start_game()
        if option == '2':
            sys.exit()


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