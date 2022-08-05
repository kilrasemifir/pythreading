"""
Exercice de la page 67.

Enoncé:
    • En utilisant le pattern composite, réalisez une application qui permet
    de visualiser les fichiers / sous-dossiers d’un dossier donné.
    • L’application doit permettre d’exécuter un nombre d’opération
    quelque soit l’élément du dossier soit fichier ou sous-dossier.
    • Les opérations sont : ajout, déplacement, suppression
"""


class Dossier:
    """
    Classe de base. Il représente un dossier.
    """
    def __init__(self, nom):
        self.nom = nom
        self.enfants = []

    def __str__(self):
        return "{}/".format(self.nom)

    def ajouter(self, dossier):
        self.enfants.append(dossier)

    def supprimer(self, dossier):
        self.enfants.remove(dossier)

    def deplacer(self, dossier, dossier_destination):
        dossier_destination.ajouter(dossier)
        self.supprimer(dossier)

    def ls(self):
        print(self)
        for enfant in self.enfants:
            print(enfant)


class Fichier:
    """
    Classe de base. Il représente un fichier.
    """
    def __init__(self, nom):
        self.nom = nom

    def __str__(self):
        return "{}".format(self.nom)


if __name__ == "__main__":
    dossier = Dossier("dossier")
    fichier = Fichier("fichier")
    dossier.ajouter(fichier)
    dossier.ls()
    dossier.deplacer(fichier, Dossier("dossier_destination"))
    dossier.ls()