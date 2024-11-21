# Jeu du pendu :
# Le joueur a 10 essais pour deviner le mot

## V3 : le mot à deviner peut contenir plusieurs fois la même lettre
# Le programme doit traiter le cas oµ le "user" entre une lettre déjà entrée plus tôt

word_to_guess = "baton"    #le mot a deviner
current_word = ["_"] *len(word_to_guess)
life = 10  #variable pour la vie
letter_used = []      #Liste pour rentrer les mots utilisés


while life > 0 and "_" in current_word:                            #La boucle va tourner tant que la vie est toujours au dessus de 0 et si il reste des "_"
    letter = input(f"Vie restante:{life} \nSaisir une lettre:")    #Début de la partie avec la phrase qui revient + la vie diminue si incorrect
    letter_used.append(word_to_guess)                               #Enregistre les lettres déjà utilisé
    if letter in word_to_guess:
        pass
    else:
     life -= 1
     input(f"Mauvaise réponse ! Vie restante:{life} \nSaisir une lettre:")


if life == 0:                             #Quand la vie arrive à 0, "Partie Terminée"
    input("Perdu, partie terminée ! :(")