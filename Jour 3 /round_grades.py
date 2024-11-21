 #écrivez un programme qui modifie une liste de note en arrondissant celles-ci à l'entier le + proche
 #Par exemple: 18.8 devient 19, 9.2 devient 9 et 10.5 devient 11

 # Est-il float? (if) si non il se passe rien, si oui dixième < 5 ou > 5 ?
 # Arrondir en dessous ! If  x - float(x) < 0.5:
 # Arrondir au-dessus ! Else float(x) > 0.5

grades = [10, 10.2, 11.8, 8.4, 5.5, 17, 19, 19.2, 19.8, 0.2, 14]  #les notes
i=0  #Variable qui va représenter l'indice à chaque iteration

for grade in grades:
    if type(grade) == float:   #Implémenter la logique d'arrondi

        if grade - int(grade) < 0.5:                #arrondi en dessous
            grades[i] = int(grade)
        else:                                       #arrondi au-dessus
            grades[i] = int(grade) + 1
    i += 1            #Dernière instruction de la boucle for
print(grades)



