my_list_of_things = [1, "hello", 4.5, True, 5, "world", False]    #On peut mettre n'importe quoi dans une liste [] !
print(my_list_of_things[3])

grades = [10, 8, 14, 20, 17, 15, 7, 5, 16, 18]    #une liste (Rappel l'indice commence de 0 donc le 10, son indice est 0 !)
print(grades[1:-2])

grades = [10, 8, 14, 20, 17, 15, 7, 5, 16, 18]
print(grades[1:-2])

#On peut modifier les éléments d'une liste
fifth_grade = grades[4]     #Lecture du 5éme élément
grades[4] = 19             #Modification du 5eme élement
print(grades)
print(fifth_grade)
