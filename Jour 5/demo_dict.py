#Collection non ordonnée   La "key"

users = {"sylvain": "azerty", "johh": "0000"} #Notre dictionnaire avec leur "key" et "value"

print(users)
print(users["sylvain"])         #Il va écrire la "value" de Sylvain, alternative à l'indice que l'on a vu précédement

# users [[1, 2, 3]] = 100       #La Key doit être un type non modifiable
# print(users)

users["alice"] = 1234 #Créer la paire "alice": "1234"
print(users)

for user in users:
    print(user)     #Print les Key

values = [2, 4, 6]
for index, value in enumerate(values, start=1): #by default start = 0
    print(f"indice: {index}, valeur : {value}")


for value in users.values():
    print(value)

for key in users.keys():
    print(key)

keys = list(users)
print(keys)
values = list(users.values())
print(values)

for key, value in users.items():  #Permet de récuperer les deux infos donc la key et value
    print(f"key: {key}, value: {value}")

users.setdefault("Joe")
print(users)

for name in ["ab", "cd", "ef"]:
    users.setdefault(name)

#print((users["Jean"]))  #Erreur vu qu'il y pas déjà value auparavant
print(users.get("Jean")) #Alors qu'ici on lui donne une value (si rien "None" apparaitra)

#"del accounts["sylvain"] Supprime




