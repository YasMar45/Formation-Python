 # écrivez un programme qui affiche le nombre de nombres pairs
 #d'une liste

numbers = [1, 2, 14, 7, 9, 45, 18, 22, 61, 32, 46]
even = 0   #variable pour le nombre de nombres pairs

for x in numbers:     #Pour chaque nombre divisible (modulo) par 2 = 0 donc pas de reste, il rajoute +1 à even
    if x % 2 == 0:
        even +=1

print(f"il y a {even} nombres pairs dans liste")