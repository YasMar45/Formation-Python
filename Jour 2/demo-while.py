# Boucle while

number = int(input("Enter a number:"))

while number < 10:     #Reste dans la boucle en dessous à l'infini si en dessous de 10
    print(number)
    #number = number + 1     #Rajouter cela augmente le number de + 1 et il va s'arrêter donc à 9, incrémentation
    number += 1              #Notation + simple !
print("Out of the loop")