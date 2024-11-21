#écrivez un programme qui compte le nombre de mots dans une phrase
#à faire avec une boucle for

sentence = "how are you doing"
counter = 1     #la Variable pour les espaces + 1

for letter in sentence:
    if letter == " ":          #Compter le nombre d'espace et faire +1 pour compter le nombre de mot dans une phrase
      counter +=1

#if counter != 0 or len(sentence) != 0:        #Cas particulier si la phrase est vide ou si il y a qu'un seul mot donc avec un counter = 0
    #counter += 1

print("le nombre de mot est de" ,counter)




