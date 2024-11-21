#Conditions de 2 facteurs ici en if only
grade = 15               #Rentrer la note désirée

if grade >= 16:
    print("Très Bien")
if 14 <= grade < 16:
    print("Bien")
if 12 <= grade < 14:
    print("Assez Bien")
if 10 <= grade < 12:
    print("Sans Mention")
if grade < 10:
    print("Echec")