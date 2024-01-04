class Personnage:
    def __init__(self, nom, vie=100):
        self.nom = nom
        self.vie = vie

    def attaquer(self, ennemi):
        ennemi.subirAttaque(10)
        print(f"{self.nom} attaque {ennemi.nom}!")
        print(f"{ennemi.nom} perd 10 points de vie.")

    def subirAttaque(self, degats):
        self.vie -= degats

class Jeu:
    def __init__(self):
        self.niveau = 1

    def choisirNiveau(self):
        self.niveau = int(input("Choisissez le niveau de difficulté (1 facile, 2 moyen, 3 difficile) : "))

    def lancerJeu(self):
        niveaux_vies = {1: 100, 2: 150, 3: 200}

        niveau_joueur = niveaux_vies.get(self.niveau, 100)
        niveau_ennemi = niveaux_vies.get(self.niveau, 100)

        joueur = Personnage("Joueur", niveau_joueur)
        ennemi = Personnage("Ennemi", niveau_ennemi)

        while joueur.vie > 0 and ennemi.vie > 0:
            joueur.attaquer(ennemi)

            if ennemi.vie <= 0:
                self.afficherResultat(ennemi, joueur)
                break

            ennemi.attaquer(joueur)

            if joueur.vie <= 0:
                self.afficherResultat(joueur, ennemi)
                break

    def afficherResultat(self, perdant, gagnant):
        print(f"{perdant.nom} a été vaincu!")
        print(f"{gagnant.nom} a gagné!")
        self.verifierSante(gagnant, perdant)

    def verifierSante(self, joueur, ennemi):
        print(f"Santé de {joueur.nom}: {joueur.vie}")
        print(f"Santé de {ennemi.nom}: {ennemi.vie}")


jeu = Jeu()
jeu.choisirNiveau()
jeu.lancerJeu()
