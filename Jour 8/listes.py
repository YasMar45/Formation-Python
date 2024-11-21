

def acceler(vehicule):
    vehicule["vitesse"] += 10.0


if __name__ == "__main__":

    a = 2.0

    # ma_liste est une INSTANCE de classe "list"
    ma_liste = list()  # list est une CLASSE
    ma_liste.append("a")  # Ici, on fait une action (on appelle une fonction)
    ma_liste.append(12)  # appel à la METHODE "append"

    # ma_liste_2 est une autre INSTANCE de classe "list"
    mon_dict = dict()
    mon_dict["truc"] = "machin"
    mon_dict["truc2"] = "machin2"

    print(f"{ma_liste=}")
    print(f"{mon_dict=}")

    # On évite ça - on va plutôt créer une CLASSE vélo
    velo = dict()
    velo["vitesse"] = 10.0
    velo["couleur"] = "jaune"
    acceler(velo)
    print(f"{velo=}")


    pass
