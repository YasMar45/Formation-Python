"""
result = print("hello")   #On lui envoie un objet quelconque, ce que l'on veut afficher dans la console
print(result)             #Elle renvoie None en réalité

number_of_users = len({"sylvain": "1234", "alice": "azerty"}) #Il ne peut pas lire plusieurs argurment (Lire les erreurs que Python nous donne !)
print(number_of_users)                                        #Il revoie bien une réponse (un int)"""

# Définitions des fonctions

def print_hello():
    print("hello")

def print_number_with_comma(number):
    float_value = float(number)
    integer_part = int(float_value)
    decimal_part = float_value - integer_part
    print(f"{integer_part},{str(decimal_part)[2:]}")

def power_of_two(x):
    result = x * x
    return result

def power(x, y):
    return x ** y

# Programme principal
# Une fonction peut être appelée plusieurs fois
print_hello()
print_hello()
# print_hello est une variable référençant vers un objet de type 'function'
print(type(print_hello))

print_number_with_comma(1.25)
result = print_number_with_comma(1) # La fonction ne renvoie rien donc result = None

result = power_of_two(4)
print(result)
result = power(2, 6)
print(result)
if result % 3 == 0:
    pass
