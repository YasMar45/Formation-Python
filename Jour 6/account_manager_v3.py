"""
V3 : "découper le programme en fonctions
au minimum 6 fonctions (mais sans doute +) :
load_accounts()
create_account()
change_password()
delete_account()
show_usernames()
save_accounts()
"""
def load_accounts(filepath):
    with open(filepath) as fp:
        lines = fp.readlines()
    accounts = {}
    for line in lines:
        username, password = line.strip().split(":")
        accounts[username] = password
    return accounts

def create_account(accounts_dict):
    print("Create account :")
    username = input("Enter a username : ")
    password = input("Enter a password : ")
    if username in accounts_dict:
        print("username already taken")
        return
    accounts_dict[username] = password
    print("Account created")

def change_password(accounts_dict):
    print("Change password :")
    username = input("Enter the username : ")
    input_password = input("Enter the current password : ")
    new_password = input("Enter the new password : ")
    if username not in accounts_dict:
        print("Username not found")
        return
    if input_password != accounts_dict[username]:
        print("Wrong password")
        return
    accounts_dict[username] = new_password
    print("Password updated")

def delete_account(accounts_dict):
    print("Delete account :")
    username = input("Enter the username : ")
    input_password = input("Enter the current password : ")
    if username not in accounts_dict:
        print("Username not found")
        return
    if input_password != accounts_dict[username]:
        print("Wrong password")
        return
    del accounts_dict[username]
    print("Account deleted")

def show_usernames(accounts_dict):
    print("Show usernames :")
    for username in accounts_dict:
        print(username)

def save_accounts(filepath, accounts_dict):
    with open(filepath, "w") as fp:
        for username, password in accounts_dict.items():
            fp.write(f"{username}:{password}\n")

# Programme principal
def main():
    accounts = load_accounts("accounts.txt")
    while True:
        choice = input("What do you want to do ? : ")
        if choice == "1":
            create_account(accounts)
        elif choice == "2":
            change_password(accounts)
        elif choice == "3":
            delete_account(accounts)
        elif choice == "4":
            show_usernames(accounts)
        elif choice == "5":
            print("Quit program")
            break
        else:
            print("Incorrect input.")
        print()
        save_accounts("accounts.txt", accounts)


if __name__ == "__main__":
    main()