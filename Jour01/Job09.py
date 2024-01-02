class Produit:
    def __init__(self, nom, prixHT, TVA):
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        return self.prixHT * (1 + self.TVA / 100)

    def afficher(self):
        info = f"Nom : {self.nom}, Prix HT : {self.prixHT}, TVA : {self.TVA}"
        return info

    def modifierNom(self, nouveau_nom):
        self.nom = nouveau_nom

    def modifierPrixHT(self, nouveau_prixHT):
        self.prixHT = nouveau_prixHT

    def obtenirNom(self):
        return self.nom

    def obtenirPrixHT(self):
        return self.prixHT

    def obtenirTVA(self):
        return self.TVA

produit1 = Produit("Livre", 15, 5)
produit2 = Produit("Ordinateur", 1000, 20)
produit3 = Produit("Montre", 50, 10)

tva_produit1 = produit1.CalculerPrixTTC()
tva_produit2 = produit2.CalculerPrixTTC()
tva_produit3 = produit3.CalculerPrixTTC()

print("Produit 1 :", produit1.afficher())
print("Produit 2 :", produit2.afficher())
print("Produit 3 :", produit3.afficher())


produit1.modifierNom("Cahier")
produit1.modifierPrixHT(10)

produit2.modifierNom("PC Portable")
produit2.modifierPrixHT(1200)

produit3.modifierNom("Bracelet")
produit3.modifierPrixHT(60)


print("\nNouveaux prix des produits :")
print("Produit 1 - Nouveau prix HT :", produit1.obtenirPrixHT())
print("Produit 2 - Nouveau prix HT :", produit2.obtenirPrixHT())
print("Produit 3 - Nouveau prix HT :", produit3.obtenirPrixHT())
