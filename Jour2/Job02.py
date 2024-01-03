class Livre:
    
    def __init__(self, titre, auteur, nbp):
        
        self.__titre = titre 
        self.__auteur = auteur
        self.__nbp = nbp
        
    def mutateur(self, titre, auteur, nbp):
        
        self.__titre = titre
        self.__auteur = auteur
        self.__nbp = nbp
        
    def set_nb_pages(self, nouveau_nb_pages):
        if isinstance(nouveau_nb_pages, int) and nouveau_nb_pages > 0:
            self.__nb_pages = nouveau_nb_pages
        else:
            print("Erreur : Le nombre de pages doit être un nombre entier positif.")
        
    def afficher(self):
        print(f"Le titre du film est", self.__titre, " écrit par ", self.__auteur, " (ce livre contient )", self.__nbp, "pages.")
        

L = Livre("le jour se lève ", "didier lefevre", 200)
L.afficher()
        
L.mutateur("katana", "hong su", 190)
L.afficher()


L.mutateur("josiane", "gérard larcher",12)
L.afficher()
L.set_nb_pages(0)