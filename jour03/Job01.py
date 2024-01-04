class Ville:
    def __init__(self, nom, nba):
        self.__nom = nom
        self.__nba = nba

    def get_population(self):
        return self.__nba

    def set_population(self, nba):
        self.__nba = nba


class Personne:
    def __init__(self, nom, age, ville):
        self.__nom = nom
        self.__age = age
        self.__ville = ville

    def ajouterPopulation(self):
        ville_actuelle_population = self.__ville.get_population()
        self.__ville.set_population(ville_actuelle_population + 1)



villeParis = Ville("Paris", 1000000)
print("Population de Paris :", villeParis.get_population())

villeMarseille = Ville("Marseille", 861635)
print("Population de Marseille :", villeMarseille.get_population())

john = Personne("John", 45, villeParis)
myrtille = Personne("Myrtille", 4, villeParis)
chloe = Personne("Chloé", 18, villeMarseille)


john.ajouterPopulation()
myrtille.ajouterPopulation()
chloe.ajouterPopulation()


print("Mise à jour de la population de Paris :", villeParis.get_population())
print("Mise à jour de la population de Marseille :", villeMarseille.get_population())



    

