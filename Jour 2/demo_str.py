#message = "Hello world!"          #Si on veut mettre world entre " sans que Python nous bloque, on utilise des \ exemple : \"world\"
message = "bonjour hello aurevoir goodbye"
print(message)                    # \n ça va faire un saut de ligne dans la console

first_character = message[0]     #Ici on veut l'indice 0 de Hello world! donc le H
print(first_character)

sixth_character = message[5]     #Ici on veut la sixième indice, l'espace qui est considéré comme un caractère
print(sixth_character)

last_character = message[-1]     # à la place de compter pour avoir le dernier indice, on peut utiliser un indice négatif !
print(last_character)
print(message[-2])

second_word = message[8:12]      # on selection un indice précis vers un autre précis
print(second_word)
first_two_word = message[:13]    #Pas besoin de mettre un 0 pour commencer à prendre les indices si on veut commencer depuis le début
print(first_two_word)

last_two_word = message[14:]     #la même chose pour l'inverse donc si on veut de la fin jusqu'à l'indice voulu
print(last_two_word)

print(message[2:16:2])
print(message[::-1])            #comme ça il va faire des steps par derrière