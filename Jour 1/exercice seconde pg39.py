#Réalisez un programme qui à partir d’un nombre quelconque de secondes (stockée dans la variable seconde) transforme ce nombre en sont équivalent heure:minute:seconde et l’affiche.

#Seconde en heures
sec = input("Entrez le nombres de secondes: ")
print(sec)

#transformer ça en heures !
heu = int(sec) / 3600
print(heu)

#transformer ça en minutes !
minu = int(sec) / 60
print("le nombre de minutes est de",minu,"")
