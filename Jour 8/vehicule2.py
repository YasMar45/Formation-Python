

class Velo:
    # "constructeur" de classe
    def __init__(self, couleur):
        self.couleur = couleur  # couleur est un attribut
        self.vitesse = 0.0  # vitesse est un autre attribut
        # Convention : attribut qui commence par "_", il ne faut pas l'utiliser
        # à l'extérieur de la classe
        self._diametre_roue_en_pouces = 24.0

    # Déclaration de METHODE de la classe Velo
    def acceler(self):
        self.vitesse += 2.0

    def changer_diametre_roue(self, nouveau_diametre):
        # test puis changement...
        if 16.0 <= nouveau_diametre <= 30.0:  # Diamètre OK
            self._diametre_roue_en_pouces = nouveau_diametre
        else:  # Diamètre absurde...
            print("Nope! Diamètre absurde - on garde les anciennes roues")

    # Autre méthode (qui ne retourne rien) - ne fait qu'agir sur la classe
    def enlever_peinture(self):
        self.couleur = 'alu'

    def calculer_diametre_roue_en_cm(self):
        return self._diametre_roue_en_pouces * 2.54

    def get_etat(self):
        return (f"Je suis un vélo de couleur {self.couleur}.\n"
                f"Diamètre de roues: {self._diametre_roue_en_pouces}in ({self.calculer_diametre_roue_en_cm()}cm en unités civilisées).\n"
                f"Vitesse actuelle: {self.vitesse}km/h")


if __name__ == "__main__":
    mon_velo1 = Velo("rose")
    mon_velo1.acceler()  # pas besoin de remettre velo1 en argument
    mon_velo1.changer_diametre_roue(50.0)
    mon_velo1.changer_diametre_roue(18.0)
    print(mon_velo1.get_etat())

    mon_velo2 = Velo('jaune')
    mon_velo2.changer_diametre_roue(16.0)
    print(mon_velo2.get_etat())


