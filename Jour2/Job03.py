class Livre:
    def __init__(self, titre, auteur, nb_pages):
        self.__titre = titre
        self.__auteur = auteur
        self.__nb_pages = nb_pages
        self.__disponible = True  

    
    def verification(self):
        return self.__disponible

  
    def emprunter(self):
        if self.verification():
            self.__disponible = False
            print("Le livre a été emprunté avec succès.")
        else:
            print("Le livre n'est pas disponible pour l'emprunt.")

 
    def rendre(self):

        if not self.verification():
            self.__disponible = True
            print("Le livre a été rendu.")
        else:
            print("Le livre n'a pas été emprunté.")

  
mon_livre = Livre("Harry Potter", "J.K. Rowling", 400)


print("Le livre est disponible ?", mon_livre.verification()) 


mon_livre.emprunter()


print("Le livre est disponible ?", mon_livre.verification()) 

mon_livre.rendre()


print("Le livre est disponible ?", mon_livre.verification()) 


