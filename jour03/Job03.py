class Tache:
    def __init__(self, titre, description, statut="à faire"):
        self.titre = titre
        self.description = description
        self.statut = statut

class ListeDeTaches:
    def __init__(self):
        self.taches = []

    def ajouterTache(self, tache):
        self.taches.append(tache)

    def supprimerTache(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                self.taches.remove(tache)
                break

    def marquerCommeFinie(self, titre):
        for tache in self.taches:
            if tache.titre == titre:
                tache.statut = "terminée"
                break

    def afficherListe(self):
        for tache in self.taches:
            print(f"Titre: {tache.titre}, Description: {tache.description}, Statut: {tache.statut}")

    def filterListe(self, statut):
        filtered_list = [tache for tache in self.taches if tache.statut == statut]
        return filtered_list

tache1 = Tache("Faire les courses", "Acheter des légumes")
tache2 = Tache("Réviser pour l'examen", "Relire les chapitres 5 et 6")
tache3 = Tache("Faire du sport", "Jogging pendant 30 minutes")

liste_taches = ListeDeTaches()

liste_taches.ajouterTache(tache1)
liste_taches.ajouterTache(tache2)
liste_taches.ajouterTache(tache3)

print("Liste complète des tâches :")

liste_taches.marquerCommeFinie("Faire les courses")


print("\nTâches à faire :")
taches_a_faire = liste_taches.filterListe("à faire")
for tache in taches_a_faire:
    print(f"Titre: {tache.titre}, Description: {tache.description}, Statut: {tache.statut}")

liste_taches.supprimerTache("Faire du sport")


print("\nListe mise à jour des tâches :")
liste_taches.afficherListe()
