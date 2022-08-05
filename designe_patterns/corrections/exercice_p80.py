"""
Exercice de la page 80.

Enoncé:
    • Nous souhaitons créer des personnages pour un jeu vidéo.
    • Commerçant, un guerrier, et un mage.
    • Les personnages possèdent des caractéristiques communes et des
    spécificités. Par exemple commerçant a du charisme, guerrier une
    force et le mage un pouvoir.
    • En utilisant le pattern Prototype Implémentez les différentes classes.
"""

class Personnage:
    """
    Classe de base
    """
    def __init__(self, nom, caracteristiques):
        self.nom = nom
        self.caracteristiques = caracteristiques


class Guerrier(Personnage):
    """
    Classe de guerrier
    """
    def __init__(self, nom):
        super().__init__(nom, {"force": 10, "charisme": 0})


class Mage(Personnage):
    """
    Classe de mage
    """
    def __init__(self, nom):
        super().__init__(nom, {"pouvoir": 10, "charisme": 0})


class Commercant(Personnage):
    """
    Classe de commerçant
    """
    def __init__(self, nom):
        super().__init__(nom, {"charisme": 10, "force": 0})


def creer_personnage(nom, type):
    """
    Fonction qui permet de créer un personnage en fonction du type
    """
    if type == "guerrier":
        return Guerrier(nom)
    elif type == "mage":
        return Mage(nom)
    elif type == "commercant":
        return Commercant(nom)
    else:
        raise ValueError("Type de personnage inconnu")


if __name__ == "__main__":
    personnage = creer_personnage("Guerrier", "guerrier")
    print(personnage)
    personnage = creer_personnage("Mage", "mage")
    print(personnage)
    personnage = creer_personnage("Commercant", "commercant")