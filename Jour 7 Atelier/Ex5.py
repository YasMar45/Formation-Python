#Le but de cette exo est que l'on puisse rentrer notre Prénom et Age !
#Ensuite, afficher le Prénom et l'Age dans un seul text

name = input("Please enter your name: ")         #On demande le prenom de la personne
age = input("Please enter your age: ")           #On demande son age aussi
text = f"Hello {name}! You are {age} years old"  #On donne forme au texte qui renvoie les deux infos précédentes
print(text)                                      #On l'affiche sur le code
