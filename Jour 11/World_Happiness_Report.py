import csv

class WHR:
    def __init__(self, _countryname, _region, _year, _lifeladder, _socialsupport, _generosity, _healthylifexpectancy, _freedom, _corruption, _confidence):
        self.countryname = _countryname
        self.region = _region
        self.year = _year
        self.lifeladder = _lifeladder
        self.socialsupport = _socialsupport
        self.generosity = _generosity
        self.healthyLifeExpectancy = _healthylifexpectancy
        self.freedom = _freedom
        self.corruption = _corruption
        self.confidence = _confidence

whrs = []

with open('World Happiness Report(1).csv', mode='r', newline='') as csvfile:

    lecteurWHR = csv.reader(csvfile, delimiter=',', quotechar='"')

    premiere_ligne = next(lecteurWHR)

    for ligne in lecteurWHR:
        uneligneWHR = WHR(
            ligne[0], ligne[1], ligne[2], ligne[3], ligne[5], ligne[8], ligne[6], ligne[7], ligne[9], ligne[12])
        whrs.append(uneligneWHR)

print(whrs[0].generosity)


moyenne = 0  #Ici on va calculer la moyenne de la générosité

for whr in whrs:
    if(whr.generosity != ''):   #On exclue les cases vides
        moyenne += float(whr.generosity)

print(moyenne/len(whrs))

somme = 0
compteur = 0

for whr in whrs:
    if(whr.healthyLifeExpectancy != ''):
        compteur += 1
        somme += float(whr.healthyLifeExpectancy)

print(somme/compteur)

for whr in whrs:
    print(f"La plus grande valeur est {int(max(whrs[5]))} ")