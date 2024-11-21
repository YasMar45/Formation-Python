# écrire un programme qui affiche la mention d'un student
# S'il a + ou = à 16 : Très Bien
# S'il a + ou = à 14 mais moins de 16 : Bien
# S'il a + ou = à 12 mais moins de 14 : Assez Bien
# S'il a + ou = à 10 mais moins de 12 : Sans Mention
# S'il a moins de 10 : Echec

grade = 13.5               #Rentrer la note désirée

if grade >= 16:            # S'il a + ou = à 16 : Très Bien
    print("Très Bien")
elif grade >= 14:          # S'il a + ou = à 14 mais moins de 16 : Bien
    print("Bien")
elif grade >= 12:          # S'il a + ou = à 10 mais moins de 12 : Sans Mention
    print("Assez Bien")
elif grade >= 10:
    print("Sans Mention")  # S'il a moins de 10 : Echec
else:                        #Ici elif grade < 10 fonctionne aussi mais on préfère mettre else pour la simplicité
    print("Echec")

