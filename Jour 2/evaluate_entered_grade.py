# Objectif : demander au user sa note entre 0 et 20
# Tant que le user ne rentre pas une note entre 0 et 20, lui redemander sa note
# Une fois que la note entréé est valide, afficher sa mention


grade = float(input("Entrer votre note:"))   #float car la note peut être une note à virgule

while not 0 <= grade <=20:
    grade = float(input("Note incorrete. Entrer votre note:"))  #Si la note n'est PAS entre 0 et 20, il aura un message d'erreur

if grade >= 16:
    print("Très Bien")
elif grade >= 14:
    print("Bien")
elif grade >= 12:
    print("Assez Bien")
elif grade >= 10:
    print("Sans Mention")
else:
    print("Echec")


