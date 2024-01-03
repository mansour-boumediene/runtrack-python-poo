class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom
        self.__prenom = prenom
        self.__numero_etudiant = numero_etudiant
        self.__nombre_credits = 0  

    def add_credits(self, credits):
        if credits > 0:
            self.__nombre_credits += credits
            print(f"{credits} crédits ajoutés avec succès.")
            self.__level = self.__studentEval()
        else:
            print("Erreur : Le nombre de crédits à ajouter doit être supérieur à zéro.")

    def get_total_credits(self):
        return self.__nombre_credits
    
    def __studentEval(self):
       if self.__nombre_credits >= 90:
           return "Excellent"
       elif self.__nombre_credits >= 80:
           return "Très bien"
       elif self.__nombre_credits >= 70:
           return "Bien"
       elif self.__nombre_credits >= 60:
           return "Passable"
       else:
           return "Insuffisant"

    def studentInfo(self):
       print(f"Nom = {self.__nom} Prénom = {self.__prenom} ID = {self.__numero_etudiant} Niveau = {self.__level}")



john_doe = Student("Doe", "John", 145)

john_doe.add_credits(10)
john_doe.add_credits(15)
john_doe.add_credits(5)

print(f"Le nombre de crédits de John Doe est de {john_doe.get_total_credits()} points.")
john_doe.studentInfo()


