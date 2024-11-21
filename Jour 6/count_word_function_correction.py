# Correction du prof

def count_words(sentence):
    words = sentence.split()
    word_counter = len(words)
    return word_counter

sentence = " hello how  are you \n bonsoir à tous  "

word_count = count_words(sentence)
print(word_count)

# La valeur renvoyée par la function est sotckée pour être réutilisée
if word_count > 5:
    print("The sentence is using more than 5 words")

