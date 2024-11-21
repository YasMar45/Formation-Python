"""
utilisation de véhicules....
"""

# On imagine qu'un bibliothèque de véhicule
# a déjà été écrite pour nous (par qq'un d'autre)
import vehicule


class Brompton(vehicule.Velo):
    def __init__(self, couleur):
        super().__init__(couleur, 16.0)
        self.nom = 'SuperBrompton'



if __name__ == "__main__":
    print("Utilisation de véhicules...")

    # Ici, on ne fait qu'utiliser la classe déjà écrite pour nous
    velo1 = vehicule.Velo("rose", 22.0)
    velo1.acceler()
    velo1.acceler()
    velo1.enlever_peinture()
    print(velo1.get_etat())

    # Utilisation d'une nouvelle classe fille
    brompton1 = Brompton("rouge")
    brompton1.acceler()
    print(brompton1.get_etat())

