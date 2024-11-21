# Objectif: créer un programme utilisable via la console permettant de :
# 1. Créer un compte (paire username: password)
# 2. Modifier un mot de passe d'un compte exisant
# 3. Supprimer un compte existant
# 4. Afficher la liste de tous les pseudos (un pseudo par ligne)
# 5. Quitter le programme
#Le programme doit demander en boucle (tant que l'on ne souhaite pas quitter) ce que le "user" veut faire

#Les comptes et mot de passe dans "account"
account = {"Yassine": "1234"}

while True:
    print("Veuillez choisir ce que vous voulez faire !\n 1. Créer un compte \n 2. Modifier votre mot de passe\n 3. Supprimer un compte existant \n 4. Afficher la liste de tous les pseudos\n 5. Quittez le programme")
    choice = input("Votre choix:")
    #Les différents choix que le user a à disposition
    if choice == "1":
        print(f"Veuillez choisir un nom d'utilisateur")
        username = input("Nom du compte:")
        password = input(f"Veuillez choisir un mot de passe:")
        if username not in account:
            account[username] = password
            print("Compte crée")
        else:
            print("Username déjà utilisé")

    elif choice == "2":
        print("Change password")
        username = input("Enter the username: ")
        input_password = input("Enter the current password: ")
        new_password = input("Entre the new password: ")
        if username not in account:
            print("Username not found")
            continue
        if input_password != account[username]:
            print("Wrong Password!")
            continue
        account[username] = new_password
        print("Password Updated")

    elif choice == "3":
        print("Supprimer votre compte")
        username = input("Enter the username: ")
        input_password = input("Enter the current password: ")
        if username in account:
            if input_password == account[username]:
                del account[username]
                print("Account Delete")
            else:
                print("Incorrect Password. Cannot delete account")
        else:
            print("Username not found")

    elif choice == "4":
        for user in account:
            print(user)
        break

    elif choice == "5":
        print("Programme en course de fermeture")
        break              #Sortie de boucle inconditionnelle donc ne quitte pas le programme

    else:
        print("Entrée incorrect ! Veuillez réessayer !")
    print()

print("Sortie de Programme")