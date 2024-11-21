"""
Upgrade par rapport à la v1 :
Au démarrage, le programme doit lire le fichier accounts.txt
et "importer" les comptes (un compte par ligne dans le fichier).
Et avant la fermeture du programme, ce dernier doit MàJ le fichier texte.
"""

with open("accounts.txt") as fp:
    lines = fp.readlines()
accounts = {}
for line in lines:
    username, password = line.strip().split(":")
    accounts[username] = password

while True:
    choice = input("What do you want to do ? : ")
    if choice == "1":
        print("Create account :")
        username = input("Enter a username : ")
        password = input("Enter a password : ")
        if username in accounts:
            print("username already taken")
            continue
        accounts[username] = password
        print("Account created")
    elif choice == "2":
        print("Change password :")
        username = input("Enter the username : ")
        input_password = input("Enter the current password : ")
        new_password = input("Enter the new password : ")
        if username not in accounts:
            print("Username not found")
            continue
        if input_password != accounts[username]:
            print("Wrong password")
            continue
        accounts[username] = new_password
        print("Password updated")
    elif choice == "3":
        print("Delete account :")
        username = input("Enter the username : ")
        input_password = input("Enter the current password : ")
        if username not in accounts:
            print("Username not found")
            continue
        if input_password != accounts[username]:
            print("Wrong password")
            continue
        del accounts[username]
        print("Account deleted")
    elif choice == "4":
        print("Show usernames :")
        for username in accounts:
            print(username)
    elif choice == "5":
        print("Quit program")
        break
    else:
        print("Incorrect input.")
    print()
with open("accounts.txt", "w") as fp:
    for username, password in accounts.items():
        fp.write(f"{username}:{password}\n")

print("Program exited.")
