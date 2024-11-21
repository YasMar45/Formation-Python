# Jeu du pendu :
# Le joueur a 10 essais pour deviner le mot

# V1 : le mot à deviner ne contient pas plusieurs fois la même lettre
# Si le "user" entre plusieurs fois une mauvaise lettre, il perd à chaque fois 1 vie

word_to_guess = "baton"    #le mot a deviner
current_word = ["_"] *len(word_to_guess)                            #il va directement prend le nombre "_" à chercher avec la fonction len
life = 10                                                           #Variable pour la vie


while life > 0 and "_" in current_word:                             #La boucle va tourner tant que la vie est toujours au dessus de 0 et si il reste des "_"
    letter = input("Saisir une lettre:")
    if letter in word_to_guess:                                     #Si la lettre est dans le mot
        index = word_to_guess.index(letter)
        current_word[index] = letter
    else:                                                           #Si la lettre est pas dans le mot -1 vie
     life -= 1
    print(f"word_to_guess : {current_word}. Tu as {life} restant")


if "_" not in current_word:
    print("Tu as gagné")


else:                                                      #Quand la vie arrive à 0, "Partie Terminée"
    input("Perdu, partie terminée ! :(")

