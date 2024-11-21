

# Classe mère (générale)
class Vehicule:
    # Construction d'un véhicule : couleur peut varier
    def __init__(
            self,
            couleur: str,
            diametre_roue_en_pouces: float,
            acceleration_step: float,
            nom: str,
    ):
        self.vitesse = 0.0  # Ici, on impose une vitesse nulle au départ
        self.couleur = couleur
        self._diametre_roue_en_pouces = diametre_roue_en_pouces
        self.acceleration_step = acceleration_step
        self.nom = nom

    def enlever_peinture(self):
        self.couleur = 'alu'

    def calculer_diametre_roue_en_cm(self):
        return self._diametre_roue_en_pouces * 2.54

    def acceler(self):
        self.vitesse += self.acceleration_step

    def get_etat(self):
        return (f"Je suis '{self.nom}' de couleur {self.couleur}.\n"
                f"Diamètre de roues: {self._diametre_roue_en_pouces}in ({self.calculer_diametre_roue_en_cm()}cm en unités civilisées).\n"
                f"Vitesse actuelle: {self.vitesse}km/h")


# Trottinette HERITE DE Véhicule
# Trottinette EST UN type particulier de véhicule
class Trottinette(Vehicule):  # parenthèses ici : opérateur d'HÉRITAGE
    # Pour une trotinette : on peut choisir UNIQUEMENT la couleur à la construction
    def __init__(self, couleur: str):
        # Appelle le constructeur de la classe mère
        super().__init__("intense_" + couleur, 6.0, 5.0, 'SuperTrot')


# Je veux pouvoir dire : "vélo EST UN véhicule"
class Velo(Vehicule):
    # "constructeur" de classe
    # :str est un typing hint (on indique que la couleur devra être donnée en tant que str)
    # Diamètre de la roue : par défaut, 24 pouces
    def __init__(self, couleur: str, diametre_roue_en_pouces: float):
        # On commence par construire la base = classe mère
        # (les concepts de base d'un véhicule en général)
        super().__init__(couleur, diametre_roue_en_pouces, 2.0, 'SuperVélo')

    def changer_diametre_roue(self, nouveau_diametre):
        # test puis changement...
        if 16.0 <= nouveau_diametre <= 30.0:  # Diamètre OK
            self._diametre_roue_en_pouces = nouveau_diametre
        else:  # Diamètre absurde...
            print("Nope! Diamètre absurde - on garde les anciennes roues")


# TODO classe Voiture...


if __name__ == "__main__":
    mon_velo1 = Velo("rose", 20.0)
    mon_velo1.acceler()  # pas besoin de remettre velo1 en argument
    mon_velo1.changer_diametre_roue(50.0)
    mon_velo1.changer_diametre_roue(18.0)
    print(mon_velo1.get_etat())

    mon_velo2 = Velo('jaune', 24.0)
    mon_velo2.changer_diametre_roue(16.0)
    print(mon_velo2.get_etat())

    ma_trot = Trottinette('noir')
    ma_trot.acceler()
    ma_trot.enlever_peinture()
    # On ne peut pas changer le diamètre de roue d'une trottinette !
    #     Donc cette méthode n'existe pas...
    # ma_trot.changer_diametre_roue(8.0)
    print(ma_trot.get_etat())

