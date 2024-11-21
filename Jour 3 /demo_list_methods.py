values = [100, 12, 53, 100, 45, 100, 74]
print(values)

#Ajout d'un élément à la fin de la liste
values.append(100)
print(values)

#Ajout d'un élément à une position donnée de la liste
values.insert(1, 0.5)
print(values)

#Suppression d'un élément de la liste via l'indice
values.pop(2)
print(values)

#Suppression d'un élément de la liste via sa valeur
values.remove(100)
print(values)  #ça enleve le premier 100

values.reverse()         #Ici on inverse la liste pour supprimer le 100 qui est dernier
values.remove(100)
values.reverse()
print(values)

values.sort()  #Trier la liste
print(values)

#Compte le nombre d'occurrences
count = values.count(100)
print(count)

values.extend([12, 15, 18])  #Etend la liste values en ajoutant les nouvelles valeurs
print(values)

index_of_100 = values.index(100) #Renvoie l'indice de la première occurrence
print(index_of_100)

