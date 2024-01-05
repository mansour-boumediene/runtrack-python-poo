class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur

    def getLongueur(self):
        return self.__longueur

    def setLongueur(self, longueur):
        self.__longueur = longueur

    def getLargeur(self):
        return self.__largeur

    def setLargeur(self, largeur):
        self.__largeur = largeur

    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    def surface(self):
        return self.__longueur * self.__largeur


class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)
        self.__hauteur = hauteur

    def getHauteur(self):
        return self.__hauteur

    def setHauteur(self, hauteur):
        self.__hauteur = hauteur

    def volume(self):
        return self.__hauteur * self.surface()

rect = Rectangle(5, 10)
print("Périmètre du rectangle:", rect.perimetre())
print("Surface du rectangle:", rect.surface())

parallelepipede = Parallelepipede(3, 4, 6)
print("Volume du parallélépipède:", parallelepipede.volume())
