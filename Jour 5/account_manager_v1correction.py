"""
Objectif : créer un programme utilisable via la console permettant de :
1. Créer un compte (paire "username" : "password")
2. Modifier un mot de passe d'un compte existant
3. Supprimer un compte existant
4. Afficher la liste de tous les pseudos (un pseudo par ligne)
5. Quitter le programme

Le programme doit demander en boucle (tant que l'on ne souhaite pas quitter)
ce que le "user" veut faire.
"""

accounts = {}

while True:
    choice = input("What do you want to do ? : ")
    if choice == "1":
        print("Create account")
        username = input("Enter the username: ")
        password = input("Enter the current password: ")
        if username in accounts:
            print("Username already taken")
            continue
        accounts[username] = password
        print("account created")


    elif choice == "2":
        print("Change password")
        username = input("Enter the username: ")
        input_password = input("Enter the current password: ")
        new_password = input("Entre the new password: ")
        if username not in accounts:
            print("Username not found")
            continue
        if input_password != accounts[username]:
            print("Wrong Password!")
            continue
        accounts[username] = new_password
        print("Password Updated")

    elif choice == "3":
        print("Delete account")
        username = input("Enter the username: ")
        input_password = input("Enter the current password: ")
        if username not in accounts:
            print("Username not found")
            continue
        if input_password != accounts[username]:
            print("Wrong Password!")
            continue
        del accounts[username]
        print("Account deleted")

    elif choice == "4":
        print("Show usernames")
        for username in accounts:
            print(username)

    elif choice == "5":
        print("Quit program")
        break
    else:
        print("Incorrect input.")
print("Program exited.")
