from datetime import datetime
import csv

class Adresse:
    def __init__(self, _rue, _numero, _boite, _cp, _ville, _pays):
        self.rue = _rue
        self.numero = _numero
        self.boite = _boite
        self.cp = _cp
        self.ville = _ville
        self.pays = _pays

    def get_adresse_complete(self):
        return str(self.numero) + ", " + self.rue + " " + str(self.cp) + " " + self.ville + " " + self.pays

class Stagiaire:
    def __init__(self, _nom, _prenom, _rue, _numero, _boite, _cp, _ville, _pays, _date_de_naissance):
        self.nom = _nom
        self.prenom = _prenom
        self.domicile = Adresse(_rue, _numero, _boite, _cp, _ville, _pays)
        self.date_de_naissance = datetime.strptime(_date_de_naissance, "%d/%m/%Y")

    def get_cp(self):
        return self.domicile.cp

    def get_age(self):
        dateAujourdhui = datetime.now()
        differenceDate = dateAujourdhui - self.date_de_naissance
        age = int(differenceDate.days / 365.25)
        return age

# charger les données du fichier CSV dans une liste
stagiaires = []


# Ouverture du fichier en lecture de texte
# Pour l'instant : csvfile est considéré comme un bête fichier texte
with open('stagiaires.csv', mode='r', newline='') as csvfile:
    # L'objet lecteurStagiaires permettra d'interpréter le fichier texte
    # comme du CSV
    lecteurStagiaires = csv.reader(csvfile, delimiter=',', quotechar='"')
    # Première ligne (nom des colonnes) : on l'ignore...
    premiere_ligne = next(lecteurStagiaires)
    for ligne in lecteurStagiaires:
        # On suppose que le CSV sera toujours organisé de la même manière
        unStagiaire = Stagiaire(
            ligne[0], ligne[1], ligne[3], ligne[4], ligne[5], ligne[6], ligne[7], ligne[8], ligne[2]
        )
        stagiaires.append(unStagiaire)

for stagiaire in stagiaires:
    print(stagiaire.nom)

moyenne = 0
for i in range(len(stagiaires)):
    moyenne = moyenne + (stagiaires[i].get_age()/len(stagiaires))
print(moyenne)

for stagiaire in stagiaires:
    if (stagiaire.get_age()>35):
        print(stagiaire.prenom + " a plus de 35 ans")

for stagiaire in stagiaires:
    print(stagiaire.prenom + " " + stagiaire.nom)
    print(stagiaire.domicile.get_adresse_complete())

moyenne = 0
compteur = 0
for stagiaire in stagiaires:
    if (stagiaire.domicile.cp=="1050"):
        moyenne += stagiaire.get_age()
        compteur += 1
print(moyenne/compteur)