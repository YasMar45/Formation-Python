import time

player_name = ""

def slow_print(text, delay=0.08):
    for char in text:
        print(char, end="",flush=True)
        time.sleep(delay)
    print()


slow_print('Bievenu(e) dans le monde de PythoLand Quest!')
slow_print('Vous êtes un aventurier se réveillant dans une sorte de cellule sans savoir comment ni pourquoi?!')
slow_print('Votre quête commence ici dans cette cellule qui envoie vers un donjon très sombre illuminé par quelques bougies')
slow_print('Faites attention ! Il faudra vous remplir de courage et y aller pour vous en sortir vivant,cela ne va pas être facile!')
slow_print('Vos choix vous meneront vers la victoire mais aussi très souvent vers la défaite, Bonne chance...')
slow_print('Mais avant tout quel est ton nom qui va "peut-être rentrer dans la légende...')
player_name = input('Entrez votre nom:')
slow_print(f'Très bien {player_name}, votre aventure commence dès maintenant')