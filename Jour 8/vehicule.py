

class Velo:
    # "constructeur" de classe
    def __init__(self, couleur):
        self.couleur = couleur  # couleur est un attribut
        self.vitesse = 0.0  # vitesse est un autre attribut
        self.diametre_roue_en_pouces = 24.0

    # Déclaration de METHODE de la classe Velo
    def acceler(self):
        self.vitesse += 2.0

    # Autre méthode (qui ne retourne rien) - ne fait qu'agir sur la classe
    def enlever_peinture(self):
        self.couleur = 'alu'

    def calculer_diametre_roue_en_cm(self):
        return self.diametre_roue_en_pouces * 2.54


if __name__ == "__main__":
    # Code de test des classes....
    mon_velo1 = Velo("jaune")
    mon_velo1.acceler()  # pas besoin de remettre velo1 en argument
    print(f"Diamètre en cm (velo1) : {mon_velo1.calculer_diametre_roue_en_cm()}")
    print(f"{mon_velo1.couleur=} {mon_velo1.vitesse=}")

    mon_velo2 = Velo("rouge")
    mon_velo2.acceler()
    mon_velo2.acceler()
    # Velo.diametre_roue_en_pouces = 20.0  # CA n'A AUCUN SENS !
    mon_velo2.diametre_roue_en_pouces = 50.0  # serait très bizarre...
    print(f"Diamètre en cm (velo2) : {mon_velo2.calculer_diametre_roue_en_cm()}")
    print(f"{mon_velo2.couleur=} {mon_velo2.vitesse=}")

    # Code exécuté SEULEMENT SI
    # ce module est exécuté en tant
    # que script principal
    print('coucou (depuis module vehicule.py)')
else:
    print(f"{__name__=}")
