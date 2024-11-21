"""
Upgrade par rapport à la v1 :
Au démarrage, le programme doit lire le fichier account.txt
et "importer" les comptes (un compte par ligne dans le ficher)
Et avant la fermeture du programme, ce dernier doit MàJ le fichier texte.
"""

with open("account.txt") as fp:
    lines = fp.readlines()

accounts = {}
for line in lines:
    #print(lines[:-1])
    username, password = line[:-1].split(":")    #il y a aussi le .strip qui enleve tout les trucs superflux et laisse que le str
    accounts[username] = password
print(accounts)


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
        print("Show usernames: ")
        for username in accounts:
            print(username)

    elif choice == "5":
        print("Quit program")
        break
    else:
        print("Incorrect input.")
    print()
with open("account.txt", "w") as fp:
    for username, password in accounts.items():
        fp.write(f"{username}:{password}\n")

print("Program exited.")