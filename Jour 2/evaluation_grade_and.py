#Avec l'opération logique and ! revoin True si des deux coté s'ils sont True
grade = 15               #Rentrer la note désirée

if grade >= 16:
    print("Très Bien")
if 14 <= grade and grade < 16:
    print("Bien")
if 12 <= grade and grade < 14:
    print("Assez Bien")
if 10 <= grade and grade < 12:
    print("Sans Mention")
if grade < 10:
    print("Echec")