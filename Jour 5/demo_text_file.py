#Ouvrir (et ici lire) un fichier.txt

fp = open("demo.txt")
text = fp.read()
print(text)
fp.close()

#Ouvrir (et ici lire ligne par ligne) un fichier "pythiniquement"

with open("demo.txt") as fp:
    lines = fp.readlines()    #Lecture ligne par ligne avec cette commande
print(lines)
print("file has been closed")

with open("demo.txt") as fp:
    line1 = fp.readline()     #Lecture de chaque ligne individuellement
    line2 = fp.readline()
print(line1[:-1])
print(line2[:-1])

#Ouverture en écriture qui supprime le contenu pré existant
line_to_write = "bonjour monde\n"
with open("demo.txt", "w") as fp:
    fp.write(line_to_write)

#Ouverture en écriture qui ne supprime pas le contenu pré existant ma va "appender"/ajouter
with open("demo.txt", "a") as fp:
    fp.write("au revoir les gens\n")

#Ecriture (mode "append") de plusieurs lignes via une liste
with open("demo.txt", "a") as fp:
    fp.writelines(["sylvain\n", "john\n", "alice\n"])