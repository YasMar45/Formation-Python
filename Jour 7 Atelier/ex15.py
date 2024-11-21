vowels = "aeiuo"

word = input("Veuillez rentrer une mot: ")

for letter in word:
    if letter in vowels:   # est-ce que lettre est une voyelle ?
        if letter.lower() in vowels:   # transforme la voyelle
            nature = "vowels"

    else:
        nature = "consonant"
    print(f"{letter}...{nature}")
