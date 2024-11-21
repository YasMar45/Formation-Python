#6 erreurs à trouver!
#####################

#Combien de jours reste-t'il avant le 1er juillet ?
#Donner date actuelle ci-dessous
varJour = 24    #N° du jour
varMois = 6     #N° du mois

#Nombre de jours de chaque mois
joursMars = 31
joursAvril = 30
joursMai = 31
joursJuin = 30

#Cas selon le mois traité
if (varMois == 3) : #Mars
    joursRestantMars = joursMars-varJour
    joursTotaux = joursRestantsMars + joursAvril + joursMai + joursJuin + 1
    print("Il reste " + str(joursTotaux) + " jours avant le 1er juillet.")
if (varMois == 4):#Avril
    joursRestantsAvril = joursAvril-varJour
    joursTotaux = joursRestantsAvril + joursMai + joursJuin + 1
    print("Il reste " + str(joursTotaux) + " jours avant le 1er juillet.")
if (varMois ==5) : #Mai
    joursRestantsMai = joursMai - varJour
    joursTotaux = joursRestantsMai + joursJuin + 1
    print("Il reste " + str(joursTotaux) + " jours avant le 1er juillet.")
if (varMois == 6): #Juin
    joursRestantsJuin = joursJuin - varJour
    joursTotaux = joursRestantsJuin
    print("Il reste " + str(joursTotaux) + " jours avant le 1er juillet.")