class CompteBancaire:
    def __init__(self, numero_compte, nom, prenom, solde, decouvert=False):
        self.__numero_compte = numero_compte
        self.__nom = nom
        self.__prenom = prenom
        self.__solde = solde
        self.__decouvert = decouvert

    def afficher(self):
        print(f"Informations du compte : {self.__numero_compte} - {self.__nom} {self.__prenom}")
        self.afficherSolde()

    def afficherSolde(self):
        print(f"Solde actuel : {self.__solde}")

    def versement(self, montant):
        self.__solde += montant
        print(f"{montant}€ ont été versés. Nouveau solde : {self.__solde}")

    def retrait(self, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            print(f"{montant}€ ont été retirés. Nouveau solde : {self.__solde}")
        else:
            print("Solde insuffisant.")

    def agios(self, taux_agios):
        if self.__solde < 0:
            self.__solde *= (1 + taux_agios)
            print("Les agios ont été appliqués.")
        else:
            print("Pas d'agios appliqués.")

    def virement(self, compte_destinataire, montant):
        if self.__solde - montant >= 0 or self.__decouvert:
            self.__solde -= montant
            compte_destinataire.versement(montant)
            print(f"Virement de {montant}€ effectué avec succès.")
        else:
            print("Solde insuffisant pour le virement.")

compte1 = CompteBancaire("123456", "Dupont", "Jean", 500)
compte1.afficher()
compte1.retrait(200)
compte1.agios(0.05)

compte2 = CompteBancaire("789012", "Durand", "Marie", -100, True)
compte1.virement(compte2, 300)
compte2.afficher()
