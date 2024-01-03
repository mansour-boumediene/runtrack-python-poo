class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande
        self.__plats_commandes = {}  
        self.__statut_commande = "En cours"

    def ajouter_plat(self, nom_plat, prix, statut="En cours"):
        self.__plats_commandes[nom_plat] = {"prix": prix, "statut": statut}

    def annuler_commande(self):
        self.__statut_commande = "Annulée"

    def __calculer_total(self):
        total = 0
        for plat in self.__plats_commandes.values():
            if plat["statut"] != "Annulée":
                total += plat["prix"]
        return total

    def afficher_commande(self):
        total = self.__calculer_total()
        print(f"Numéro de commande : {self.__numero_commande}")
        print("Plats commandés :")
        for nom_plat, plat in self.__plats_commandes.items():
            print(f"- {nom_plat}: {plat['prix']} $ ({plat['statut']})")
        print(f"Total à payer : {total} $")

    def calculer_tva(self, taux_tva):
        total = self.__calculer_total()
        tva = total * (taux_tva / 100)
        print(f"TVA à {taux_tva}% : {tva} $")


ma_commande = Commande("CMD001")

ma_commande.ajouter_plat("Pizza", 15)
ma_commande.ajouter_plat("Salade", 8)
ma_commande.ajouter_plat("Dessert", 5, "Terminé")

ma_commande.afficher_commande()
ma_commande.calculer_tva(10)

ma_commande.annuler_commande()
ma_commande.afficher_commande()
