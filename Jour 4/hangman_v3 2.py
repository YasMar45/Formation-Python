# mot à trouver
word = "test"

# partie trouvée
discovered = []

# lettres utilisées
used_letters = []

# tentatives restantes
attempts_left = 10

# initialisation du mot à trouver
for letter in word:
    discovered.append("_")

while "_" in discovered and attempts_left > 0:
    guess = input("Entrez une lettre :")
    # si lettre non essayé
    if guess not in used_letters:
        used_letters.append(guess)
        found_letter = False
        # parcours du mot à trouver
        for i in range(0, len(word)):
            # lettre trouvée dans le mot
            if word[i] == guess:
                discovered[i] = word[i]
                found_letter = True
        # si lettre présente
        if found_letter:
            # création du mot à afficher
            word_to_print = ""
            for letter in discovered:
                word_to_print += letter
            print(f"{guess} trouvé ! Nouveau mot : {word_to_print}")
        # lettre absente
        else:
            attempts_left -= 1
            print(f"{guess} non trouvé ! Tentatives restantes : {attempts_left}")
    # lettre déjà essayée
    else:
        print("Lettre déjà essayée !")

if attempts_left > 0:
    print("Victoire !")
else:
    print("Défaite...")