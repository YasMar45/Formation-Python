

class Wallet:
    def __init__(self, amount, currency):
        self.original_amount = amount
        self.original_currency = currency
        self._rates_from_eur_to_other = {'EUR': 1.0, 'USD': 1.06, 'CZK': 25.29}
        # Vérification conformité de la devise
        if self.original_currency not in self._rates_from_eur_to_other.keys():
            print("!!!!! Devise non-gérée !!!!!!!")

    # Conversion vers une devise quelconque
    def convert_to(self, target_currency):
        if target_currency not in self._rates_from_eur_to_other.keys():
            print("!!!!! Devise non-gérée !!!!!!!")
            return -1.0
        amount_in_eur = self.original_amount / self._rates_from_eur_to_other[self.original_currency]
        return amount_in_eur * self._rates_from_eur_to_other[target_currency]


if __name__ == "__main__":

    # Ici, on est à l'extérieur de la classe ; on est ici
    # un UTILISATEUR (qui se fiche des mécanismes internes de la classe)
    wallet1 = Wallet(10.0, "CZK")
    resultat_conversion = wallet1.convert_to("USD")
    print(f"Résultat : {resultat_conversion:.2f} USD")
