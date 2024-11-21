# Réalisez un programme qui à partir diamètre d’un cercle en cm calcule sa surface en m²
# Input prend le diamètre en cm
# Le programme calcule l’aire (π × R²) en m² et l’affiche

# Input prend le diamètre en cm
Dia = input("Entrez le diamètre en cm : ")
print(Dia)
print(type(Dia))

#Rayon: Dia / 2
Rayon = int(Dia) / 2
print(Rayon)

#Aire = 3.14 * (Rayon ** 2)
Aire = 3.14 * (int(Rayon) ** 2)
print(Aire)

#Mètrecarré = Aire / 10000
mc = int(Aire) / 10000
print ("l'aire du cercle est de : ",mc, " m²")








