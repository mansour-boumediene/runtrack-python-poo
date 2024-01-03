class Rectangle:
    
    def __init__(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def mutateur(self, longueur, largeur):
        self.__longueur = longueur
        self.__largeur = largeur
        
    def afficher(self):
        print(f"La longeur est de ", self.__longueur, " et la largeur est de ", self.__largeur)
        
    
R = Rectangle(10,5)
R.afficher()

R.mutateur(19,7)
R.afficher()




