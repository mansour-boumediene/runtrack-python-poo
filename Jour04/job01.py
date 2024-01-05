class Personne:
    def __init__(self, age=14):
        self.age = age

    def afficherAge(self):
        print(f"L'âge de la personne est : {self.age}")

    def bonjour(self):
        print("Hello")

    def modifierAge(self, nouvel_age):
        self.age = nouvel_age


class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")

    def afficherAge(self):
        print(f"J'ai {self.age} ans")


class Professeur(Personne):
    def __init__(self, matiereEnseignee, age=14):
        super().__init__(age)
        self.matiereEnseignee = matiereEnseignee

    def enseigner(self):
        print("Le cours va commencer")


personne = Personne()
personne.afficherAge()
personne.modifierAge(25)
personne.afficherAge()
personne.bonjour()


eleve = Eleve()
eleve.afficherAge()
eleve.modifierAge(18)
eleve.afficherAge()
eleve.allerEnCours()


prof = Professeur("Mathématiques")
prof.afficherAge()
prof.modifierAge(35)
prof.afficherAge()
prof.enseigner()
personne = Personne()
eleve = Eleve()
eleve.afficherAge()