class Personne:
    def __init__(self, nom, prenom):
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        return f"Je suis {self.prenom} {self.nom}"

# Instanciation de plusieurs personnes avec des valeurs choisies
personne1 = Personne("Doe", "John")
personne2 = Personne("Dupont", "Jean")


# Appel de la méthode SePresenter pour chaque personne
print(personne1.SePresenter())
print(personne2.SePresenter())
