#Définissez une fonction qui compte le nombre de mots
# d'un string et renvoie ce nombre

def count_words(string):
    words = string.split()    #en mettant rien il va compter le wide space en entier directement
    n_words = len(words)
    return n_words


print(count_words("Hello World"))
print(count_words("How are you doing to day ?"))
