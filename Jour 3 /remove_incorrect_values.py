# "Retirer" d'une liste de note les valeurs incorrect
# Plus précisément, créer une nouvelle liste ne contenant pas les incorrectes de celle de départ
# Une valeur correcte est un nombre compris entre 0 et 20 (inclus)
# la liste originale ne doite pas être modifié

grades = [-11, 0, 10, 21, "19", "dix", 7, 7.5, 19.5, True, 14, False]
correct_grades = []

for cg in grades:
    if (type(cg) == int or type(cg) == float) and 0 <= cg <= 20:     #Vérifie d'abord ici si c'est bien un int ou un float et qu'ils soient entre 0 et 20 (inclus)
        correct_grades.append(cg)

print(correct_grades)

grades = [-11, 0, 10, 21, "19", "dix", 7, 7.5, 19.5, True, 14, False]
correct_grades = []
for cg in grades:
    if type(cg) == int or type(cg) == float:     #Vérifie d'abord ici si c'est bien un int ou un float
        if 0 <= cg <= 20:                        #Vérifie après si c'est bien un nombre compris entre 0 et 20 les deux compris
            correct_grades.append(cg)

print(correct_grades)


#BONUS

grades = [-11, 0, 10, 21, "19", "dix", 7, 7.5, 19.5, True, 14, False]    #Code en 2 ligne (pas de moi mais un pote)
c = [cr for cr in grades if type(cr) in (int, float) and 0 <= cr <= 20]

print(c)

print([cr for cr in [-11, 0, 10, 21, "19", "dix", 7, 7.5, 19.5, True, 14, False] if type(cr) in (int, float) and 0 <= cr <= 20])  #Code en 1 ligne (pas de moi mais un pote)