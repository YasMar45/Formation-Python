mdp = input("Entrez votre mot de passe: ")
mdp_size = len(mdp)

if mdp_size == 0:
    print("Veuillez insérez un mot de passe")

elif mdp_size < 6:
    print("Sécurite du mot de passe trop faible")

elif mdp_size >= 8:
    print("Sécurité du mot de passe INCROYABLE")

elif mdp_size >= 6:
    print("Sécurite du mot de passe valide")

