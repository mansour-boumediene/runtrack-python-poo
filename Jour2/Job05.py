class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque
        self.__modele = modele
        self.__annee = annee
        self.__kilometrage = kilometrage
        self.__en_marche = False
        self.__reservoir = 50 

    def set_marque(self, nouvelle_marque):
        self.__marque = nouvelle_marque

    def get_marque(self):
        return self.__marque

    def set_modele(self, nouveau_modele):
        self.__modele = nouveau_modele

    def get_modele(self):
        return self.__modele

    def set_annee(self, nouvelle_annee):
        self.__annee = nouvelle_annee

    def get_annee(self):
        return self.__annee

    def set_kilometrage(self, nouveau_kilometrage):
        self.__kilometrage = nouveau_kilometrage

    def get_kilometrage(self):
        return self.__kilometrage

    def set_en_marche(self, etat):
        self.__en_marche = etat

    def get_en_marche(self):
        return self.__en_marche

    def demarrer(self):
        if self.__verifier_plein() > 5:
            self.__en_marche = True
            print("La voiture démarre.")
        else:
            print("Impossible de démarrer : réservoir trop bas.")

    
    def arreter(self):
        self.__en_marche = False
        print("La voiture s'arrête.")

    def __verifier_plein(self):
        return self.__reservoir


ma_voiture = Voiture("Toyota", "Corolla", 2020, 20000)


print("Niveau du réservoir :", ma_voiture._Voiture__verifier_plein())
ma_voiture.demarrer()


ma_voiture.arreter()