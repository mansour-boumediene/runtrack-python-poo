class Animal:
    def __init__(self):
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        self.age += 1
        
        
    def nommer(self, nom):
        self.prenom = nom

mon_animal = Animal()

print("L'âge de l'animal :", mon_animal.age)

# age de l'alnimal aprés l'appelle de la méthode viellir  
mon_animal.vieillir()
print("Après avoir vieilli, l'âge de l'animal est  :", mon_animal.age)

mon_animal.nommer("Luna")
print("L'animal se nomme :", mon_animal.prenom)
